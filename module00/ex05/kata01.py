# Notions :
# Dictionnaires

# Un dictionnaire est une collection de paires clé/valeur
# - clé : identifie un élément unique (ici le langage)
# - valeur : donnée associée à la clé (ici le créateur)
# - .items() renvoie les couples clé/valeur pour pouvoir les parcourir

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

# Parcours du dictionnaire et affichage formaté : .items retourne une liste de tuple (un iterable)
# .keys() retourne les cles, .values() les valeurs (des itérables ==> succession de valeurs).
for (language, creator) in kata.items():
	print(f"{language} was created by {creator}")

for creator in kata.values():
	print(creator)

for languages in kata.keys():
	print(kata[languages])

# # Un itérable peut etre transformé en liste
# bonjour = list(kata.keys())
# print(bonjour)
# print(kata.keys())