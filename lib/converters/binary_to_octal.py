def binary_to_octal(binary_num):
    binary_str = str(binary_num)

    while len(binary_str) % 3 != 0:
        binary_str = "0" + binary_str

    octal_str = ''
    for i in range(0 ,len(binary_str), 3):
        binary_group = binary_str[i:i + 3]
        octal_digit = int(binary_group, 2)
        octal_str += str(octal_digit)

    return int(octal_str)
