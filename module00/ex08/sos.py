import  sys
import  string

morse_values_alpha = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", 
                ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..--", "...-",
                ".--", "-..-", "-.--", "--.."]

morse_values_numbers = [i * '.' + (5 - i) * '-' for i in range(5)] + [i * '-' + (5 - i) * '.' for i in range(5)]

morse_values = morse_values_alpha + morse_values_numbers

morse_keys = string.ascii_lowercase + string.digits

morse = dict(zip(morse_keys, morse_values)) # => conversion d'un iterateur en iterable

# zip renvoie un iterateur de tuples
"""
z = zip([1, 2, 3], ['a', 'b'])
print(type(z))            # <class 'zip'>
print(list(z))            # [(1, 'a'), (2, 'b')]
"""

def main():
    if len(sys.argv) <= 1:
        return print("Error: wrong number of args") or 1
    bigs = ' '.join(sys.argv[1:])
    i = 0
    while i in range(len(bigs)):
        if bigs[i] == ' ':
            print('/', end = "")
        elif bigs[i].isalnum():
            if bigs[i].isupper():
                print(morse[bigs[i].lower()], end = "")
            else:
                print(morse[bigs[i]], end = "")
        i += 1
    print("")
    return 0

if __name__ == "__main__":
    main()
