def octal_to_hexadecimal(octal):
    hex_dictionary = {
        0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
        6: '6', 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
        12: "C", 13: "D", 14: "E", 15: "F",
    }

    octal = int(octal)

    decimal = 0
    base_num = 1
    while octal > 0:
        remainder = octal % 10
        decimal += remainder * base_num
        octal //= 10
        base_num *= 8

    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_dictionary[remainder] + hexadecimal
        decimal //= 16

    return hexadecimal
