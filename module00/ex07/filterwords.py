# Notions :
# List comprehension

import sys
import string

if __name__ == "__main__":

	if len(sys.argv) != 3:
		print("ERROR: program requires 2 arguments — a string and an integer.")
		sys.exit(1)

	s = sys.argv[1]
	try:
		n = int(sys.argv[2])
		if n < 0:
			raise ValueError
	except ValueError:
		print("ERROR: second argument must be a non-negative integer.")
		sys.exit(1)

	words = [word.strip(string.punctuation) for word in s.split()]
	filtered = [word for word in words if len(word) > n]
	
	print(filtered)
