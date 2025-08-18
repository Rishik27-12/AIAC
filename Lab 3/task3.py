# develop a python function which calculates the power bill for a given number of units
def calculate_power_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + ((units - 100) * 2.5)
    elif units <= 300:
        bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
    else:
        bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 6)
    return bill

try:
    units = float(input("Enter the number of units consumed: "))
    if units < 0:
        print("Units cannot be negative.")
    else:
        total_bill = calculate_power_bill(units)
        print(f"Total power bill for {units} units is: ₹{total_bill:.2f}")
except ValueError:
    print("Please enter a valid number for units.")
