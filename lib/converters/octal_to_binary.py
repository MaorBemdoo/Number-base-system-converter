def octal_to_binary(octnum):
    oct_to_bin_map = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}

    octnum_str = str(octnum)
    if any(digit not in oct_to_bin_map for digit in octnum_str):
        return "Invalid Octal Digit"

    return ''.join(oct_to_bin_map[digit] for digit in octnum_str)
