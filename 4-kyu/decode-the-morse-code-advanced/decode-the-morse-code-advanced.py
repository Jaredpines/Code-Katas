import re
def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip('0')
    if not bits:
        return ""
    runs = re.split(r'(0+)', bits)
    rate = min(len(run) for run in runs if run)
    dot = '1' * rate
    dash = '1' * (3 * rate)
    char_sep = '0' * (3 * rate)
    word_sep = '0' * (7 * rate)
    decoded_words = []
    for word in bits.split(word_sep):
        decoded_chars = []
        for char in word.split(char_sep):
            elements = char.split('0' * rate)
            morse_char = "".join(['.' if el == dot else '-' for el in elements if el])
            if morse_char:
                decoded_chars.append(morse_char)
        decoded_words.append(" ".join(decoded_chars))
    return "   ".join(decoded_words)
​
def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    message = ""
    morseCode = morseCode.replace("   ", "  ")
    characters = morseCode.split(" ")
    for character in characters:
        if character == "":
            message += " "
        else:
            message += MORSE_CODE[character]
    return message
    return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
​