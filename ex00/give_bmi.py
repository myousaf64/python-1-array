def _check_list(values: list, name: str) -> None:
    """Raise if values is not a list of int or float."""
    if not isinstance(values, list):
        raise TypeError(f"{name} must be a list")
    for item in values:
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            raise TypeError(f"{name} must hold only int or float")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Return the BMI of each person as a list of floats."""
    _check_list(height, "height")
    _check_list(weight, "weight")
    if len(height) != len(weight):
        raise ValueError("height and weight must have the same size")
    if len(height) == 0:
        raise ValueError("height and weight must not be empty")
    for value in height:
        if value <= 0:
            raise ValueError("height must be greater than 0")
    return [w / (h * h) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for each BMI value above the limit."""
    _check_list(bmi, "bmi")
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an int")
    return [value > limit for value in bmi]
