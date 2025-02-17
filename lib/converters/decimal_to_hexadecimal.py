def decimal_to_hexadecimal(decimal):
    decimal = int(decimal)
    hexadecimal = ""
    hex_digits = "0123456789ABCDEF"
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder]+hexadecimal
        decimal //= 16
    return hexadecimal
