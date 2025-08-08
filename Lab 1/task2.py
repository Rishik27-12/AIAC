def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage:
while True:
    user_input = input("Enter number of terms: ")
    try:
        n_terms = int(user_input)
        if n_terms < 0:
            print("Please enter a non-negative integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
fib_seq = fibonacci_sequence(n_terms)
print(f"Fibonacci sequence up to {n_terms} terms:")
print(fib_seq)