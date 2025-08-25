import re

def is_valid_mobile(number):
    # Check if the number starts with 6, 7, 8, or 9 and has exactly 10 digits
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, number))

# Ask the user to enter a mobile number
user_input = input("Enter your mobile number: ")
if is_valid_mobile(user_input):
    print("Valid mobile number.")
else:
    print("Invalid mobile number.")
