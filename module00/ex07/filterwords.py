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

	# On crée une table de traduction (dictionnaire) utilisée par la méthode
	# Chaque caractère de string.punctuation (par ex. '!', '.', ',', etc.) devient une clé dont la valeur est None
	translator = str.maketrans('', '', string.punctuation) # remplacer '' par '' et supprimer string.punctuation
	# .translate() est une methode qui parcourt un dictionnaire (table de traduction),
	# et remplace les mots par les valeurs dans le dict (ici suppression)
	clean_s = s.translate(translator)

	# Creer une liste des mots de clean_s
	words = clean_s.split()

	# Une list comprehension est une façon condensée d’écrire une boucle for qui construit une liste.
	# crée une nouvelle liste contenant tous les mots de words dont la longueur (len(word)) est supérieure à n

	# # words if len(word) > n : mots dans la taille > n
	# # for word in ... : word parcours words
	# # word ... : ce qu'on incorpore dans la liste.
	filtered = [word for word in words if len(word) > n]
	
	print(filtered)
