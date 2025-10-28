import sys

def calculator(A, B):
	"""Prints sum, difference, product, quotient, and remainder of two integers."""
	sum_ = A + B
	diff = A - B
	prod = A * B

	if B != 0:
		quot = A / B
		rem = A % B
	else:
		quot = "Error (division by zero)"
		rem = "Error (division by zero)"

	print(f"Sum: {sum_}")
	print(f"Difference: {diff}")
	print(f"Product: {prod}")
	print(f"Quotient: {quot}")
	print(f"Remainder: {rem}")

if __name__ == "__main__":

	if len(sys.argv) < 3:
		print("Usage: python script.py <int A> <int B>")
		sys.exit(0)

	if len(sys.argv) > 3:
		print("Error: exactly two arguments required")
		sys.exit(0)

	try:
		A = int(sys.argv[1])
		B = int(sys.argv[2])
	except ValueError:
		print("Error: both arguments must be integers")
		sys.exit(1)

	calculator(A, B)
