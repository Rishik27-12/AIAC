def classify_age_group(age):
    if age < 0:
        return "Invalid age"
    if age <= 12:
        return "Child"
    elif age <= 19:
        if age >= 13:
            return "Teen"
        else:
            return "Child"
    elif age <= 59:
        if age >= 20:
            return "Adult"
        else:
            return "Teen"
    else:
        if age >= 60:
            return "Senior"
        else:
            return "Adult"

def main():
    try:
        age = int(input("Enter age: "))
        group = classify_age_group(age)
        print(f"Age Group: {group}")
    except ValueError:
        print("Please enter a valid integer for age.")

if __name__ == "__main__":
    main()
