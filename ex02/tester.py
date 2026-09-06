from load_image import ft_load


def main():
    """Load the subject image and print its pixels."""
    try:
        print(ft_load("landscape.jpg"))
    except Exception as error:
        print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
