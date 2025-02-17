def hexadecimal_to_octal(hexadecimal):
    hex_to_dec_dictionary = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    decimal_number = 0
    for base in hexadecimal:
        decimal_number = decimal_number * 16 + hex_to_dec_dictionary[base.upper()]

    if decimal_number == 0:
        return '0'

    octal_number = ''
    while decimal_number > 0:
        octal_value = decimal_number % 8
        octal_number = str(octal_value) + octal_number
        decimal_number //= 8

    return octal_number
