MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    text = ''
    for i in message:
        if i != ' ':
            text += MORSE_CODE_DICT[i.upper()] + ' '
        else:
            text += MORSE_CODE_DICT['/'] + ' '
    print(text)


def decrypt(message):
    text = ''
    code = [i for sign in message.split() for i in (sign, ' ')][:-1]
    for i in code:
        for key, value in MORSE_CODE_DICT.items():
            if i == value:
                text += key
    print(text.replace('/', ' '))


