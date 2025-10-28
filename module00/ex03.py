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
	# pour chaque element c dans txt auquel on applique la fonction isupper()
	print(f"{sum(c.isupper() for c in txt)} upper letter(s)")
	# pour chaque element c dans txt auquel on applique la fonction islower()
	print(f"{sum(c.islower() for c in txt)} lower letter(s)")
	# pour chaque element c dans txt, c etant dans str.punctuation
	print(f"{sum(c in string.punctuation for c in txt)} punctuation marks")


# Partie exécutable seulement si c'est lancé depuis le terminal (protection) et pas importe
# Python donne à chaque fichier exécuté une variable automatique __name__
# et si le fichier est exécuté directement, Python définit : __name__ = "__main__"
# Si le fichier est importé depuis un autre, alors : __name__ = "nom_du_module"

if __name__ == "__main__":
	# main() # pour lancer directement depuis la console
	# Si plus d'un argument est fourni → erreur
	if len(sys.argv) != 2:
		print("Error: enter a string please")
		sys.exit(1)

	# Récupérer l’argument s’il existe
	arg = sys.argv[1] if len(sys.argv) == 2 else None
	text_analyzer(arg)