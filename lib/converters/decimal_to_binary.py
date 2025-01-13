def decimal_to_binary(decimal_number):
    decimal_number=int(decimal_number)
    if decimal_number == 0:
        return "0"
    binary = ""
    while decimal_number > 0:
        binary = str(decimal_number % 2) + binary 
        decimal_number //= 2

    return binary
    
