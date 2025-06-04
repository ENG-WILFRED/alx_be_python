FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    # (fahrenheit - 32) * factor
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    # celsius * factor + 32
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if scale == 'F':
        converted = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted}°C")
    elif scale == 'C':
        converted = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted}°F")
    else:
        print("Invalid scale. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
