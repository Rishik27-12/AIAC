# develop a python function which prints the factorial of 1 to 10
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

for i in range(1, 11):
    print(f"Factorial of {i} is {factorial(i)}")
