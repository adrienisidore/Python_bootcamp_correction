

												# kata00
# Un tuple est une collection ordonnée et immuable d'éléments
# - iterable : on peut creer un iterateur et le parcourir
# - ordonné : chaque élément a une position fixe, accessible par index
# - immuable : on ne peut pas modifier, ajouter ou supprimer d'éléments
# - peut contenir plusieurs types différents (int, str, bool, etc.)
#   => à une position donnée, tu peux mettre n'importe quel type,
#      mais le type n'est pas imposé par le tuple lui-même
# Exemple : t = (1, "hello", True)
# deux methodes : .count(x) ==> nb de fois ou x apparait dans le tuple,  ou .index()

kata = (19, 42, 21)

# Affichage formaté
print(f"The 3 elements are: {kata[0]}, {kata[1]}, {kata[2]}")



												# kata01

# Un dictionnaire est une collection non ordonnée de paires clé/valeur
# - clé : identifie un élément unique (ici le langage)
# - valeur : donnée associée à la clé (ici le créateur)
# - .items() renvoie les couples clé/valeur pour pouvoir les parcourir
# f"..." est une f-string pour insérer directement les variables dans la chaîne

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

# Parcours du dictionnaire et affichage formaté : .items retourne une liste de tuple (un iterable)
# .keys() retourne les cles, .values() les valeurs (des iterables ==> succession de valeurs).
for (language, creator) in kata.items():
	print(f"{language} was created by {creator}")

for creator in kata.values():
	print(creator)

for languages in kata.keys():
	print(kata[languages])
# Un iterable peut etre transforme en liste
bonjour = list(kata.keys())
print(bonjour)
print(kata.keys())

												# kata02

kata = (2019, 9, 25, 3, 30)

# On récupère les valeurs : la virgule transfert les valeurs d'un element vers l'autre (tuple vers tuple)
(year, month, day, hour, minute) = kata
print(f"{month:02d}/{day:02d}/{year} {hour:02d}:{minute:02d}")


												# kata03

# {:->42} est une f-string formatée :
# - >42 : aligner le texte à droite sur 42 caractères
# - -   : remplir les espaces restants avec des tirets
# Cela permet que la ligne finale (et non l'objet) fasse exactement 42 caractères

kata = "The right format"
print(f"{kata:->42}")


												# kata04

kata = (0, 4, 132.42222, 10000, 12345.67)
mod, ex, dec1, integer, dec2 = kata
print(f"module_{mod:02d}, ex_{ex:02d} : {dec1:.2f}, {integer:.2e}, {dec2:.2e}")


