# Notions :
# Tuples

# Un tuple est une collection ordonnée et immuable d'éléments
# - itérable : on peut creer un iterateur et le parcourir
# - ordonné : chaque élément a une position fixe, accessible par index
# - immuable : on ne peut pas modifier, ajouter ou supprimer d'éléments
# - peut contenir plusieurs types différents (int, str, bool, etc.)
#   => à une position donnée, tu peux mettre n'importe quel type,
#      mais le type n'est pas imposé par le tuple lui-même
# Exemple : t = (1, "hello", True)

kata = (19, 42, 21)

# Affichage formaté
print(f"The 3 elements are: {kata[0]}, {kata[1]}, {kata[2]}")