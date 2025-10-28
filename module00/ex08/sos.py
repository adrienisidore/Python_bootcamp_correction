
import sys
import  string

morse = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

if len(sys.argv) == 1:
    print("Give me at least one string por favor")
    sys.exit(1)

if not all(all(c.isalnum() or c.isspace() for c in arg) for arg in sys.argv[1:]):
    print("Give me alphanumeric characters or spaces only por favor")
    sys.exit(1)

phrase = " ".join(sys.argv[1:]).upper()

for c in phrase:
    print(morse[c], end=" ")