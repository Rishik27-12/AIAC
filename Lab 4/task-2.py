def factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    Returns 1 for n == 0.
    Prints an error message and returns None for negative numbers.
    """
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    n = int(input("Enter a non-negative integer to compute its factorial: "))
    print(f"Factorial of {n} is {factorial(n)}")
    n = int(input("Enter a non-negative integer to compute its factorial: "))
    result = factorial(n)
    if result is not None:
        n = int(input("Enter a non-negative integer to compute its factorial: "))
        result = factorial(n)
        if result is not None:
            print(f"Factorial of {n} is {result}")
            # INSERT_YOUR_CODE
def main():
    while True:
        try:
            n = int(input("Enter a non-negative integer to compute its factorial (or type 'exit' to quit): "))
        except ValueError:
            print("Invalid input. Please enter a non-negative integer or 'exit' to quit.")
            continue
        result = factorial(n)
        if result is not None:
            print(f"Factorial of {n} is {result}")

if __name__ == "__main__":
    main()
