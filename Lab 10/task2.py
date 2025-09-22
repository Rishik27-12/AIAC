def area_of_rectangle(L: float, B: float) -> float:
    """Calculate the area of a rectangle.

    Args:
        L (float): The length of the rectangle.
        B (float): The breadth of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    if L <= 0 or B <= 0:
        raise ValueError("Length and breadth must be positive")
    return L * B
print(area_of_rectangle(10,20))
