import sys
import random

#create the morse code dictionary
dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---.', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', ':': '---...', '?': '..--..', '\'': '.----.', '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '\"': ".-..-.", '=': '-...-', '+': '.-.-.'}

#encodes a string into morse code
def morse_encode(string):
    retval = ""
    for c in string:
        if c == ' ':
            retval += "/ "
            continue
        
        retval += dict[c] + ' '

    return retval

def pick_char(chars_list):
    index = random.randint(0, len(chars_list) - 1)
    return chars_list[index]

#turn actual morse code into horrendous emoji abominations:
def homogenize(message, chars):
    retval = ""
    for c in message:
        if c == '.':
            retval += pick_char(chars) + ' '
        elif c == '-':
            retval += pick_char(chars) + pick_char(chars) + pick_char(chars) + ' '
        elif c == ' ':
            retval += '  '
        elif c == '/':
            retval += '  '
        else:
            print("invalid message")
            sys.exit(1)
        
    return retval

def read_chars():
    result = []
    raw_in = input("enter a list of characters to build the morse code out of:")
    for character in raw_in:
        if not character.isspace():
            result.append(character)

    return result

#main
message = input("enter a message to translate into morse code: ")
message = morse_encode(message.lower())
print(message)
chars = read_chars()
output = homogenize(message, chars)
print(output)
