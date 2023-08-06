import random
from typing import TypeVar

import torch
import torchvision.transforms.functional as V
from PIL.Image import Image as PILImage
from torch import Tensor, nn
from torchvision.transforms import InterpolationMode

Image = TypeVar("Image", Tensor, PILImage)

NormParams = tuple[float, float, float]

# Default image normalization parameters.
MEAN: NormParams = 0.48145466, 0.4578275, 0.40821073
STD: NormParams = 0.26862954, 0.26130258, 0.27577711


def square_crop(img: Image) -> Image:
    img_width, img_height = V.get_image_size(img)
    height = width = min(img_height, img_width)
    top, left = (img_height - height) // 2, (img_width - width) // 2
    return V.crop(img, top, left, height, width)


def square_resize_crop(img: Image, size: int, interpolation: InterpolationMode = InterpolationMode.NEAREST) -> Image:
    img_width, img_height = V.get_image_size(img)
    min_dim = min(img_width, img_height)
    height, width = int((img_width / min_dim) * size), int((img_height / min_dim) * size)
    img = V.resize(img, [height, width], interpolation)
    top, left = (height - size) // 2, (width - size) // 2
    return V.crop(img, top, left, size, size)


def upper_left_crop(img: Image, height: int, width: int) -> Image:
    return V.crop(img, 0, 0, height, width)


def rescale(x: Image, scale: float, min_val: float, do_checks: bool = False) -> Image:
    assert isinstance(x, Tensor), "Rescale must operate on a tensor"
    assert x.dtype.is_floating_point, "Rescale got non-floating point input tensor"
    if do_checks:
        min_val, max_val = x.min().item(), x.max().item()
        assert min_val >= 0 and max_val <= 1, "Rescale input has values outside [0, 1]"
    return x * scale + min_val


def convert_image_to_rgb(image: PILImage) -> PILImage:
    return image.convert("RGB")


def normalize(t: Tensor, *, mean: NormParams = MEAN, std: NormParams = STD) -> Tensor:
    return V.normalize(t, mean, std)


def denormalize(t: Tensor, *, mean: NormParams = MEAN, std: NormParams = STD) -> Tensor:
    mean_tensor = torch.tensor(mean, device=t.device, dtype=t.dtype)
    std_tensor = torch.tensor(std, device=t.device, dtype=t.dtype)
    return (t * std_tensor[None, :, None, None]) + mean_tensor[None, :, None, None]


def normalize_shape(t: Tensor) -> Tensor:
    dims = t.shape[0]
    if dims == 3:
        return t
    if dims == 1:
        return t.repeat_interleave(3, dim=0)
    if dims > 3:
        return t[:3]
    raise NotImplementedError(dims)


def random_square_crop(img: Image) -> Image:
    img_width, img_height = V.get_image_size(img)
    height = width = min(img_height, img_width)
    top, left = random.randint(0, img_height - height), random.randint(0, img_width - width)
    return V.crop(img, top, left, height, width)


def random_square_crop_multi(imgs: list[Image]) -> list[Image]:
    img_dims = V.get_image_size(imgs[0])
    assert all(V.get_image_size(i) == img_dims for i in imgs[1:])
    img_width, img_height = img_dims
    height = width = min(img_width, img_height)
    top, left = random.randint(0, img_height - height), random.randint(0, img_width - width)
    return [V.crop(i, top, left, height, width) for i in imgs]


def make_size(img: Image, ref_size: tuple[int, int]) -> Image:
    """Converts an image to a specific size, zero-padding smaller dimension.

    Args:
        img: The input image
        ref_size: The reference size, as (width, height)

    Returns:
        The resized image
    """

    img_c, (img_w, img_h), (ref_w, ref_h) = V.get_image_num_channels(img), V.get_image_size(img), ref_size
    if img_h / img_w < ref_h / ref_w:  # Pad width
        new_h, new_w = (img_h * ref_w) // img_w, ref_w
    else:
        new_h, new_w = ref_h, (img_w * ref_h) // img_h
    img = V.resize(img, [new_h, new_w], InterpolationMode.BILINEAR)
    new_img = img.new_zeros(img_c, ref_h, ref_w)
    start_h, start_w = (ref_h - new_h) // 2, (ref_w - new_w) // 2
    new_img[:, start_h : start_h + new_h, start_w : start_w + new_w] = img
    return new_img


def make_same_size(img: Image, ref_img: Image) -> Image:
    """Converts an image to the same size as a reference image.

    Args:
        img: The input image
        ref_img: The reference image

    Returns:
        The input image resized to the same size as the reference image,
            zero-padding dimensions which are too small
    """

    ref_w, ref_h = V.get_image_size(ref_img)
    return make_size(img, (ref_w, ref_h))


class SquareResizeCrop(nn.Module):
    __constants__ = ["size", "interpolation"]

    def __init__(self, size: int, interpolation: InterpolationMode = InterpolationMode.NEAREST) -> None:
        """Resizes and crops an image to a square with the target shape.

        Generally SquareCrop followed by a resize should be preferred when using
        bilinear resize, as it is faster to do the interpolation on the smaller
        image. However, nearest neighbor resize on the larger image followed by
        a crop on the smaller image can sometimes be faster.

        Args:
            size: The square height and width to resize to
            interpolation: The interpolation type to use when resizing
        """

        super().__init__()

        self.size = int(size)
        self.interpolation = InterpolationMode(interpolation)

    def forward(self, img: Image) -> Image:
        return square_resize_crop(img, self.size, self.interpolation)


class UpperLeftCrop(nn.Module):
    __constants__ = ["height", "width"]

    def __init__(self, height: int, width: int) -> None:
        """Crops image from upper left corner, to preserve image intrinsics.

        Args:
            height: The max height of the cropped image
            width: The max width of the cropped image
        """

        super().__init__()

        self.height, self.width = height, width

    def forward(self, img: Image) -> Image:
        return upper_left_crop(img, self.height, self.width)


class RescaleImage(nn.Module):
    __constants__ = ["min_val", "scale", "do_checks"]

    def __init__(self, min_val: float, max_val: float, do_checks: bool = True) -> None:
        """Rescales an image from (0, 1) to some other scale.

        Args:
            min_val: The scale if `max_val` is None, otherwise the min value
            max_val: The maximum value
            do_checks: If set, check the input tensor ranges (can disable for
                more efficient image loading)
        """

        super().__init__()

        self.min_val, self.scale, self.do_checks = min_val, max_val - min_val, do_checks

    def forward(self, x: Image) -> Image:
        return rescale(x, self.min_val, self.scale, self.do_checks)
