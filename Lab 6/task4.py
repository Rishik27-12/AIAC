def sum_to_n(n):
    """
    Calculate the sum of the first n natural numbers.

    Args:
        n (int): The number up to which the sum is calculated.

    Returns:
        int: The sum of the first n natural numbers.
    """
    return n * (n + 1) // 2

# Example usage:
if __name__ == "__main__":
    n = 10
    print(f"Sum of first {n} numbers is {sum_to_n(n)}")