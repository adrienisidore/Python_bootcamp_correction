from generator import generator

def main():
	for word in generator("Hey Hey guys! This is Adrien.", sep=" "):
		print(word)
	print()
	for word in generator("Hey Hey guys! This is Adrien.", sep=" ", option="shuffle"):
		print(word)
	print()
	for word in generator("Hey Hey guys! This is Adrien.", sep=" ", option="ordered"):
		print(word)
	print()
	for word in generator("Hey Hey guys! This is Adrien.", sep=" ", option="unique"):
		print(word)

if __name__ == "__main__":
	main()