#Develop a python program to find the sum of even and odd numbers from user input
def sum_even_odd_from_user_input():
    numbers = []
    first_input = input("Enter count or space-separated numbers: ")
    try:
        n = int(first_input)
        for i in range(n):
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
    except ValueError:
        parts = first_input.strip().split()
        numbers = [int(p) for p in parts]
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum

# Example usage:
# even_sum, odd_sum = sum_even_odd_from_user_input()
# print("Sum of even numbers:", even_sum)
# print("Sum of odd numbers:", odd_sum)


if __name__ == "__main__":
    even_sum, odd_sum = sum_even_odd_from_user_input()
    print("Sum of even numbers:", even_sum)
    print("Sum of odd numbers:", odd_sum)
