import numpy as np
import matplotlib.pyplot as plt


def _show(array: np.ndarray, title: str) -> None:
    """Display an array as an image in a matplotlib window."""
    plt.imshow(array)
    plt.title(title)
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    inverted = 255 - array
    _show(inverted, "Invert")
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red channel of the image received."""
    red = array.copy()
    red[:, :, 1] = red[:, :, 1] * 0
    red[:, :, 2] = red[:, :, 2] * 0
    _show(red, "Red")
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green channel of the image received."""
    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]
    _show(green, "Green")
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue channel of the image received."""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    _show(blue, "Blue")
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Turns the image received into shades of grey."""
    grey = array.copy()
    grey[:, :, :] = grey[:, :, 0:1] / 1
    _show(grey, "Grey")
    return grey
