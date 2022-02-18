import sys

#create the morse code dictionary
dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---.', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', ':': '---...', '?': '..--..', '\'': '.----.', '-': '-....-', '/': '-..-.'}

#encodes a string into morse code
def morse_encode(string):
    retval = ""
    for c in string:
        if c == ' ':
            retval += "/ "
            continue
        
        retval += dict[c] + ' '

    return retval

#turn actual morse code into horrendous emoji abominations:
def homogenize(message, char):
    retval = ""
    for c in message:
        if c == '.':
            retval += char + ' '
        elif c == '-':
            retval += char + char + char + ' '
        elif c == ' ':
            retval += '  '
        elif c == '/':
            retval += '  '
        else:
            print("invalid message")
            sys.exit(1)
        
    return retval

#main
message = input("enter a message to translate into morse code: ")
message = morse_encode(message.lower())
print(message)
char = input("enter a character to build the morse code out of: ")
output = homogenize(message, char)
print(output)
