def decimal_to_octal(decimal_num):

    if decimal_num == 0:
        return "0"

    octal_num = ''
    while decimal_num > 0:
        reminder = decimal_num % 8
        octal_num = str(reminder) + octal_num
        decimal_num //= 8

    return octal_num
# ELLA EMMANUELLA JAPARI