# develop a python function for temperature conversion
def convert_temperature(value, from_unit, to_unit):
    """
    Converts temperature between Celsius, Fahrenheit, and Kelvin.

    Args:
        value (float): The temperature value to convert.
        from_unit (str): The unit of the input temperature ('celsius', 'fahrenheit', 'kelvin').
        to_unit (str): The unit to convert to ('celsius', 'fahrenheit', 'kelvin').

    Returns:
        float: The converted temperature value.
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # Convert input to Celsius first
    if from_unit == 'celsius':
        celsius = value
    elif from_unit == 'fahrenheit':
        celsius = (value - 32) * 5/9
    elif from_unit == 'kelvin':
        celsius = value - 273.15
    else:
        raise ValueError("Invalid from_unit. Choose from 'celsius', 'fahrenheit', 'kelvin'.")

    # Convert from Celsius to target unit
    if to_unit == 'celsius':
        return celsius
    elif to_unit == 'fahrenheit':
        return celsius * 9/5 + 32
    elif to_unit == 'kelvin':
        return celsius + 273.15
    else:
        raise ValueError("Invalid to_unit. Choose from 'celsius', 'fahrenheit', 'kelvin'.")

# Example usage
if __name__ == "__main__":
    print("Temperature Converter")
    try:
        value = float(input("Enter the temperature value: "))
        from_unit = input("Enter the unit to convert from (Celsius, Fahrenheit, Kelvin): ").strip()
        to_unit = input("Enter the unit to convert to (Celsius, Fahrenheit, Kelvin): ").strip()
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit.capitalize()} is {result:.2f} {to_unit.capitalize()}")
    except ValueError as e:
        print(f"Error: {e}")


