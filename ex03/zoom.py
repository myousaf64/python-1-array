import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    """Load animal.jpeg, zoom on a 400x400 square, and display it."""
    try:
        pixels = ft_load("animal.jpeg")
        print(pixels)
        zoom = pixels[100:500, 450:850, 0:1]
        print(f"New shape after slicing: {zoom.shape}")
        print(zoom)
        plt.imshow(zoom[:, :, 0], cmap="gray")
        plt.show()
    except Exception as error:
        print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
