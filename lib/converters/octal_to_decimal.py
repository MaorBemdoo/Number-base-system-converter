def octal_to_decimal(octal_number):
    if '.' in octal_number:
        integer_part, fractional_part = octal_number.split('.')
    else:
        integer_part, fractional_part = octal_number, ''

    decimal = 0
    for power, digit in enumerate(reversed(integer_part)):
        decimal += int(digit) * (8 ** power)

    for power, digit in enumerate(fractional_part, start=1):
        decimal += int(digit) * (8 ** -power)

    return decimal