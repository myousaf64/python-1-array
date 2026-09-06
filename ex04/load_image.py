import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> np.ndarray:
    """Load a JPG image, print its shape, and return its RGB pixels."""
    if not isinstance(path, str):
        raise TypeError("path must be a str")
    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError(f"{path}: only JPG and JPEG files are supported")
    try:
        with Image.open(path) as image:
            pixels = np.array(image.convert("RGB"))
    except FileNotFoundError:
        raise FileNotFoundError(f"{path}: no such file")
    except UnidentifiedImageError:
        raise ValueError(f"{path}: the file is not a readable image")
    except OSError as error:
        raise OSError(f"{path}: {error}")
    print(f"The shape of image is: {pixels.shape}")
    return pixels
