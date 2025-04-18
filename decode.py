import sys

#create the morse code dictionary
dict = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---.': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '.-.-.-': '.', '--..--': ',', '---...': ':', '..--..': '?', '.----.': '\'', '-....-': '-', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-..-.': '\"', '-...-': '=', '.-.-.': '+'}

def contains_whitespace(in_string):
    for i in range(len(in_string)):
        if in_string[i].isspace():
            return True

    return False


#decodes from morse code into plain text
def morse_decode(string):
    retval = ""
    string = string.split(' ')
    for c in string:
        if c == '':
            if not retval.endswith(' '):
                retval += ' '
        elif c == '/':
            retval += ' '

        else:
            retval += dict[c]

    return retval

#turns emoji abominations into .-/ morse code
def dehomogenize(message):
    retval = ""
    message = message.strip()
    space_count = 0
    for c in message.split(' '):
        if len(c) == 1 and not contains_whitespace(c):
            retval += '.'
        elif len(c) == 3 and not contains_whitespace(c):
            retval += '-'
        elif c == '':
            space_count += 1
            if not retval.endswith(' '):
                retval += ' '

            if space_count >= 6:
                retval += "/ "
                space_count = 0
        else:
            print("invalid message:" + c)
            sys.exit(1)

        if c != '':
            space_count = 0
        
    return retval

#main
message = input("enter a message to translate from homegenized morse code: ")
message = dehomogenize(str(message))
print(message)
message = morse_decode(str(message))
print(message)
