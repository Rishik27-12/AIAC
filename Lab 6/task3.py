# task3.py

# Function to classify age group and check other conditions
def classify_age(age):
    if age < 0:
        return "Invalid age"
    else:
        if age <= 12:
            group = "Child"
        elif age <= 19:
            group = "Teen"
        elif age <= 59:
            group = "Adult"
        else:
            group = "Senior"

        # Additional condition: Check if age is even or odd
        if age % 2 == 0:
            parity = "Even age"
        else:
            parity = "Odd age"

        return f"Age Group: {group}, {parity}"

# Example usage
if __name__ == "__main__":
    age = int(input("Enter age: "))
    result = classify_age(age)
    print(result)