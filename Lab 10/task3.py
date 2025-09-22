def calculate_percentage(amount, percent):
    """Calculate the percentage of a given amount."""
    return amount * percent / 100
# Example usage with descriptive variable names and inline comments

# Define the amount and the percentage to calculate
total_amount = 500
percentage_value = 20

# Calculate the percentage of the total_amount
calculated_percentage = calculate_percentage(total_amount, percentage_value)

# Print the result with a descriptive message
print(f"{percentage_value}% of {total_amount} is {calculated_percentage}")

amount = 200
percent = 15
result = calculate_percentage(amount, percent)
print(result)