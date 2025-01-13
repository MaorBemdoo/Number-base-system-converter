def hexadecimal_to_decimal(hex_num):
    hex_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    hex_num = hex_num.upper()
    decimal_value = 0
    power = 0

    for digit in reversed(hex_num):
        if digit in hex_map:
            decimal_value += hex_map[digit] * (16 ** power)
            power += 1
        else:
            raise ValueError(f"Invalid character '{digit}' in hexadecimal number.")

    return decimal_value
