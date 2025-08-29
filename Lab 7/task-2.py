def sort_list(data):
    return sorted(data)

# The original list mixes integers and strings, which cannot be compared directly in Python 3.
# To fix the error, use a list with elements of the same type, e.g., all integers or all strings.
items = [3, 1, 2, 5, 4]  # all integers
# Alternatively, if you want to sort strings:
# items = ["apple", "banana", "cherry"]
print(sort_list(items))