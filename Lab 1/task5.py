def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            return num_lines
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

# Example usage
filename = 'rishi.txt'  # Replace with your file path
num_lines = count_lines_in_file(filename)
if num_lines is not None:
    print(f"Number of lines in '{filename}': {num_lines}")