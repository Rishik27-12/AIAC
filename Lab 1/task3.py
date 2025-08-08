def reverse_string(s):
    """
    Returns the reversed version of the input string s.
    """
    return s[::-1]

# Example usage
if __name__ == "__main__":
    input_str = input("Enter a string to reverse: ")
    print("Reversed string:", reverse_string(input_str))