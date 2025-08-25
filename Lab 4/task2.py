def factorial(n):
    if n < 0:
        raise ValueError("Error: Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Ask the user to enter a number and print its factorial
try:
    user_input = int(input("Enter a number to find its factorial: "))
    print("Factorial:", factorial(user_input))
except ValueError as e:
    print(e)