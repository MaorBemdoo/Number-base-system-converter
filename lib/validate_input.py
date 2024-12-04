def validate_input(value, from_base):
    if from_base == 'd':
        if not value.isdigit():
            print(f"Invalid decimal input: {value}. Only digits are allowed.")
    elif from_base == 'b':
        if not all(c in '01' for c in value):
            print(f"Invalid binary input: {value}. Only 0 and 1 are allowed.")
    elif from_base == 'o':
        if not all(c in '01234567' for c in value):
            print(f"Invalid octal input: {value}. Only digits 0-7 are allowed.")
    elif from_base == 'h':
        if not all(c in '0123456789abcdefABCDEF' for c in value):
            print(f"Invalid hexadecimal input: {value}. Only digits 0-9 and letters A-F are allowed.")
    else:
        print(f"Unsupported base: {from_base}")