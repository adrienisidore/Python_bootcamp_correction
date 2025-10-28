# Notions :
# try ... except

import sys

if len(sys.argv) != 2:
	print("Usage: python script.py <integer>")
	sys.exit(1)

try:
	number = int(sys.argv[1]) # fonction : appelle en interne la méthode spéciale __int__() si elle existe sur l’objet.
except ValueError:
	print("Error: argument must be an integer")
	sys.exit(1)

if number == 0:
	print("Zero")
elif number % 2 == 0:
	print("Even")
else:
	print("Odd")
