
# Notions :
# Attribut spécial __name__
# Générateurs
# "is" sur objets
# string formatting

import sys
import string

# None est un objet donc on utilise "is" et pas "=="
def text_analyzer(txt=None):

	if txt is None:
		print("Error: no string provided")
		return
	if not isinstance(txt, str):
		print("Error: argument must be a string")
		return

	print(f"the text contains {sum(c.isalnum() for c in txt)} printable characters:")
	# compte le nb d'element c dans txt auquel on applique la fonction isupper()
	print(f"{sum(c.isupper() for c in txt)} upper letter(s)")
	# compte le nb d'element c dans txt auquel on applique la fonction islower()
	print(f"{sum(c.islower() for c in txt)} lower letter(s)")
	# compte le nb d'element c dans txt, c etant dans str.punctuation
	print(f"{sum(c in string.punctuation for c in txt)} punctuation marks")


# Script VS programme
# Programme: "python3 *nom_programme*"
	#1 - Sans __name__ == "__main__" execute de haut en bas (name recupere nom du module)
	#2 - Avec __name__ == "__main__" execute la fonction main
# Script: "python3 *enter*" + "import ... from ..."
	#Appel de fonction depuis l'intepreteur python

if __name__ == "__main__":

	if len(sys.argv) != 2:
		print("Error: enter a string please")
		sys.exit(1)

	arg = sys.argv[1] if len(sys.argv) == 2 else None
	text_analyzer(arg)