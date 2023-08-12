
def decimal_to_base(decimal_num, base):
    hex_chars = "0123456789ABCDEF"
    result = ""

    # Convert integer part
    integer_part = int(decimal_num)
    if integer_part != 0:
        while integer_part > 0:  # Use a loop to calculate the remainders and build the result
            remainder = integer_part % base
            # Convert remainder to a character and add to the left of the result
            result = hex_chars[remainder] + result
            # print(result)
            integer_part //= base  # Update decimal_num for the next iteration
    else:
        result = "0"

    result += "."  # Add decimal point
    print(result)
    # Convert fractional part
    fractional_part = decimal_num - int(decimal_num)
    precision = 5  # Choose the number of digits for precision
    while fractional_part > 0 and precision > 0:
        fractional_part *= base
        digit = int(fractional_part)
        # print(result)
        result += hex_chars[digit]  # result = result + hex_chars[digit]
        # print(result)
        fractional_part -= digit
        precision -= 1

    return result


def base_to_decimal(base_num, base):
    hex_chars = "0123456789ABCDEF"
    base_num = base_num.upper()  # Convert to uppercase for case-insensitive matching
    decimal_result = 0

    integer_part, fractional_part = base_num.split(".")

    # Convert integer part to decimal
    power = len(integer_part) - 1
    for digit in integer_part:
        decimal_result += hex_chars.index(digit) * (base ** power)
        power -= 1

    # Convert fractional part to decimal
    power = -1
    for digit in fractional_part:
        decimal_result += hex_chars.index(digit) * (base ** power)
        power -= 1

    return decimal_result


def show_calculation_visual(base_num, base, decimal_result, is_decimal_to_base=True):
    print(
        f"Calculating {'Decimal to Base' if is_decimal_to_base else 'Base to Decimal'} conversion:")
    print(f"Input: {base_num} (Base {base})")

    base_num_str = str(base_num)  # Convert input to string for processing

    if is_decimal_to_base:
        print("\nDecimal to Base Conversion:")
        integer_part, fractional_part = base_num_str.split(".")
        print("\nInteger Part Calculation:")
        power = len(integer_part) - 1
        for digit in integer_part:
            digit_value = int(digit, base)
            contribution = f"{digit_value} * ({base}^{power})"
            print(f"{contribution:^20} = {digit_value * (base ** power)}")
            power -= 1

        print("\nFractional Part Calculation:")
        power = -1
        for digit in fractional_part:
            digit_value = int(digit, base)
            contribution = f"{digit_value} * ({base}^{power})"
            print(f"{contribution:^20} = {digit_value * (base ** power)}")
            power -= 1

    else:
        print("\nBase to Decimal Conversion:")
        print("\nInteger Part Calculation:")
        power = len(base_num_str.split(".")[0]) - 1
        for digit in base_num_str.split(".")[0]:
            digit_value = int(digit, base)
            contribution = f"{digit_value} * ({base}^{power})"
            print(f"{contribution:^20} = {digit_value * (base ** power)}")
            power -= 1

        print("\nFractional Part Calculation:")
        power = -1
        for digit in base_num_str.split(".")[1]:
            digit_value = int(digit, base)
            contribution = f"{digit_value} * ({base}^{power})"
            print(f"{contribution:^20} = {digit_value * (base ** power)}")
            power -= 1

    print("\nFinal Result:")
    print(f"{' + '.join(str(int(digit, base)) + ' * (' + str(base) + '^' + str(power) + ')' for digit, power in zip(base_num_str.replace('.', ''), range(len(base_num_str) - 1, -1, -1)))} = {decimal_result}")


def show_conversion_visual(decimal_input, base_input):
    base_result = decimal_to_base(decimal_input, base_input)
    decimal_result = base_to_decimal(base_result, base_input)

    print("Visual for Decimal to Base Conversion:")
    show_calculation_visual(decimal_input, base_input, base_result)

    print("\n---------------------------------\n")

    print("Visual for Base to Decimal Conversion:")
    show_calculation_visual(base_result, base_input, decimal_result, False)


if __name__ == "__main__":
    try:
        decimal_input = float(input("Enter a decimal number: "))
        base_input = int(input("Enter a base value: "))

        # Check if base_input is valid
        if base_input not in [2, 8, 10, 16]:
            raise ValueError(
                'Base must be either of the following values: 2, 8, 10, 16.')

        # Check for negative decimal_input
        if decimal_input < 0:
            raise ValueError("Please enter a non-negative integer.")

        # Call the decimal_to_base function with the correct parameters
        base_result = decimal_to_base(decimal_input, base_input)
        print(f"Converted result: {base_result}")

        # Converting back to decimal
        decimal_result = base_to_decimal(base_result, base_input)
        print(f"Converted back to decimal: {decimal_result}")

        show_conversion_visual(decimal_input, base_input)

    except ValueError as e:
        print(f"Error: {e}")
