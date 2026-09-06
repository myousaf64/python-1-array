import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_transpose(array: np.ndarray) -> np.ndarray:
    """Return the transpose of a 2D array, written without a library."""
    if array.ndim != 2:
        raise ValueError("the array to transpose must be 2D")
    height, width = array.shape
    return np.array([[array[y][x] for y in range(height)]
                     for x in range(width)], dtype=array.dtype)


def main():
    """Load animal.jpeg, cut a square, transpose it, and display it."""
    try:
        pixels = ft_load("animal.jpeg")
        square = pixels[100:500, 450:850, 0]
        print(f"The shape of image is: {square.shape}")
        print(square)
        rotated = ft_transpose(square)
        print(f"New shape after Transpose: {rotated.shape}")
        print(rotated)
        plt.imshow(rotated, cmap="gray")
        plt.show()
    except Exception as error:
        print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
