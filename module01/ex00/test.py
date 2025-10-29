# from book import Book
# from recipe import Recipe

# def main():
# 	my_book = Book("Miam!")
# 	my_book.recipes_list["starter"].append(Recipe("Salad", 1, 10, ["lettuce", "tomato"], "", "starter"))
# 	my_book.recipes_list["lunch"].append(Recipe("Sandwich", 2, 15, ["bread", "ham"], "", "lunch"))
# 	my_book.recipes_list["dessert"].append(Recipe("Cake", 3, 60, ["flour", "sugar", "eggs"], "", "dessert"))
	

# if __name__ == "__main__":
# 	try:
# 		main()
# 	except Exception as e:
# 		print("Error:", e)


from datetime import datetime
from book import Book
from recipe import Recipe

def main():
	print("=== TEST INITIALISATION DU LIVRE ===")
	my_book = Book("Miam!")

	print(f"Book créé : {my_book.name}")
	print(f"Date de création : {my_book.creation_date}")
	print(f"Clés du cookbook : {list(my_book.recipes_list.keys())}")

	print("\n=== AJOUT DE RECETTES ===")
	salad = Recipe("Salad", 1, 10, ["lettuce", "tomato"], "Simple starter", "starter")
	sandwich = Recipe("Sandwich", 2, 15, ["bread", "ham"], "Quick lunch", "lunch")
	cake = Recipe("Cake", 3, 60, ["flour", "sugar", "eggs"], "Sweet dessert", "dessert")

	my_book.add_recipe(salad)
	my_book.add_recipe(sandwich)
	my_book.add_recipe(cake)

	print("Recettes ajoutées avec succès.")
	print(f"Dernière mise à jour : {my_book.last_update}")

	print("\n=== AFFICHAGE PAR TYPE ===")
	for t in ["starter", "lunch", "dessert"]:
		recipes = my_book.get_recipes_by_types(t)
		print(f"{t.capitalize()} recipes:", [r.name for r in recipes])

	print("\n=== RECHERCHE PAR NOM ===")
	name = "Cake"
	found = my_book.get_recipe_by_name(name)
	if found:
		print(f"Recette trouvée : {found.name}, durée : {found.cooking_time} min")
	else:
		print(f"Aucune recette trouvée pour {name}")

	print("\n=== TEST ERREURS ===")
	try:
		my_book.add_recipe("not_a_recipe")
	except Exception as e:
		print("Error:", e)

	try:
		my_book.get_recipes_by_types("dinner")
	except Exception as e:
		print("Error:", e)

if __name__ == "__main__":
	main()
