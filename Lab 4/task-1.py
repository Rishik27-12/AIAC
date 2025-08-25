import re

def is_valid_mobile_number(number):
    """
    Checks if the given mobile number is valid:
    - Starts with 6, 7, 8, or 9
    - Contains exactly 10 digits
    """
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, str(number)))

# Prompt user to enter a mobile number and check validity
user_input = input("Enter your 10-digit mobile number: ")
if is_valid_mobile_number(user_input):
    print("Valid mobile number.")
else:
    print("Invalid mobile number. It should start with 6, 7, 8, or 9 and contain exactly 10 digits.")

