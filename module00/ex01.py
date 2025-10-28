import sys

if len(sys.argv) < 2:
	print("Usage: python exec.py <string>")
	sys.exit(0)

# input_string = " ".join(sys.argv[1:]) # sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] ... (pas d'espaces en debut ou fin de chaine)
# reversed_string = input_string[::-1] # [start:stop:step] -> nouvel objet par slicing : du debut a la fin avec, avec pas -1
# swapped_string = reversed_string.swapcase() # transforme en majuscule
# print(swapped_string)

print(" ".join(sys.argv[1:])[::-1].swapcase())