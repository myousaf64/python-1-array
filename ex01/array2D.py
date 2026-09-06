import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of a 2D list, then return a sliced copy of it."""
    if not isinstance(family, list) or len(family) == 0:
        raise TypeError("family must be a non-empty list")
    for row in family:
        if not isinstance(row, list):
            raise TypeError("family must be a list of lists")
        if len(row) != len(family[0]):
            raise ValueError("every row must have the same size")
    if isinstance(start, bool) or not isinstance(start, int):
        raise TypeError("start must be an int")
    if isinstance(end, bool) or not isinstance(end, int):
        raise TypeError("end must be an int")
    array = np.array(family)
    print(f"My shape is : {array.shape}")
    sliced = array[start:end]
    print(f"My new shape is : {sliced.shape}")
    return sliced.tolist()
