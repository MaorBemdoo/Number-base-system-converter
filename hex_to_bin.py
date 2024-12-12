def hex_to_binary(hex_str):

    hex_to_binary_dict = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    binary_str = ''
    for hex_digit in hex_str.upper():
        binary_str += hex_to_binary_dict[hex_digit]

    return binary_str

# Get  the input from the user
hex_input = input("Enter a hexadecimal number: ")

# Converts the hexadecimal number to binary
binary_output = hex_to_binary(hex_input)

# Print the output
print(f"The binary equivalent of {hex_input} is: {binary_output}")