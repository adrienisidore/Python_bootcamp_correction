import random
import string

def generator(text, sep=" ", option=None):
	"""
	Yield substrings of `text` split by `sep`.
	Only works with printable characters.
	"""
	if option is not None and option not in ("shuffle", "ordered", "unique"):
		raise ValueError("available option : 'shuffle', 'ordered', 'unique'")
	if not isinstance(text, str):
		raise TypeError("text must be a string")
	if not all(c in string.printable for c in text):
		raise ValueError("text contains non-printable characters")
	if not sep in string.printable:
		raise ValueError("sep contains non-printable character(s)")

	words = text.split(sep)
	if option == "shuffle":
		random.shuffle(words)
	elif option == "ordered":
		words.sort()
	elif option == "unique":
		# words = set(words)
		words = list(dict.fromkeys(words))


	for substring in words:
		yield substring
