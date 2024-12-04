def binary_to_hexadecimal(binary):
    bin_to_hex_map = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }
    
    while len(binary) % 4 != 0:
        binary = "0" + binary  
    
    chunks = [binary[i:i+4] for i in range(0, len(binary), 4)]
    
    hexadecimal = "".join(bin_to_hex_map[chunk] for chunk in chunks)
    
    return hexadecimal