# develop a python function which calculates the power bill for a given number of units and make it so that units cost different for different type of customers
def calculate_power_bill(units, customer_type):
    """
    Calculates the power bill for a given number of units and customer type.

    Args:
        units (float): Number of units consumed.
        customer_type (str): Type of customer. Should be 'residential', 'commercial', or 'industrial'.

    Returns:
        float: Total bill amount.
    """
    # Define rate slabs for different customer types
    rates = {
        'residential': [(100, 1.5), (100, 2.5), (100, 4), (float('inf'), 6)],
        'commercial':  [(100, 2.0), (100, 3.5), (100, 5), (float('inf'), 7)],
        'industrial':  [(100, 2.5), (100, 4.0), (100, 6), (float('inf'), 8)]
    }

    customer_type = customer_type.lower()
    if customer_type not in rates:
        raise ValueError("Invalid customer type. Choose from 'residential', 'commercial', or 'industrial'.")

    bill = 0
    remaining_units = units
    for slab_units, rate in rates[customer_type]:
        if remaining_units > 0:
            units_in_slab = min(remaining_units, slab_units)
            bill += units_in_slab * rate
            remaining_units -= units_in_slab
        else:
            break
    return bill

if __name__ == "__main__":
    try:
        units = float(input("Enter the number of units consumed: "))
        if units < 0:
            print("Units cannot be negative.")
        else:
            print("Customer types: residential, commercial, industrial")
            customer_type = input("Enter customer type: ").strip().lower()
            total_bill = calculate_power_bill(units, customer_type)
            print(f"Total power bill for {units} units ({customer_type}) is: ₹{total_bill:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
