import sys

# Vérifie qu'il y a exactement un argument
if len(sys.argv) != 2:
	print("Usage: python script.py <integer>")
	sys.exit(1)

try:
	number = int(sys.argv[1]) # tente un recasting
except ValueError:
	print("Error: argument must be an integer")
	sys.exit(1)

if number == 0:
	print("Zero")
elif number % 2 == 0:
	print("Even")
else:
	print("Odd")
