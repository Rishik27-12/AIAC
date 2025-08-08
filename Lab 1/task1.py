def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Example usage
input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")