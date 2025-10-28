# Notions :
# Nested dictionnaries

# Un dictionnaire peut avoir des clés de differents types

# ----- Initialisation du cookbook -----
cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


# ----- 1. Afficher toutes les recettes -----
def print_all_recipes():
	"""Print all recipe names in the cookbook."""
	if not cookbook:
		print("The cookbook is empty.")
	else:
		print("Recipes available:")
		for name in cookbook:
			print(name)


# ----- 2. Afficher les détails d'une recette -----
def print_recipe_details(name):
	"""Print details of a given recipe name."""
	recipe = cookbook.get(name)
	if recipe is None:
		print(f"Recipe '{name}' not found.")
		return
	print(f"\nRecipe for {name}:")
	print(f"Ingredients list: {', '.join(recipe['ingredients'])}")
	print(f"To be eaten for {recipe['meal']}.")
	print(f"Takes {recipe['prep_time']} minutes of cooking.\n")

# ----- 3. Supprimer une recette -----
def delete_recipe(name):
	"""Delete a recipe from the cookbook."""
	if name in cookbook:
		del cookbook[name]
		print(f"Recipe '{name}' deleted.")
		print(f" Length : {len(cookbook)}")
	else:
		print(f"Recipe '{name}' not found.")


# ----- 4. Ajouter une recette depuis l’entrée utilisateur -----
def add_recipe():
	"""Add a new recipe based on user input."""
	name = input("Enter a recipe name: ")
	ingredients = input("Enter ingredients separated by commas: ").split(',')
	ingredients = [i.strip() for i in ingredients]  # supprime les espaces
	meal = input("Enter meal type (e.g., lunch, dinner, dessert): ")
	try:
		prep_time = int(input("Enter preparation time (in minutes): "))
		if prep_time < 0:
			raise ValueError
	except ValueError:
		print("Invalid preparation time. Must be a non-negative integer.")
		return

	cookbook[name] = {
		"ingredients": ingredients,
		"meal": meal,
		"prep_time": prep_time
	}
	print(f"Recipe '{name}' added successfully!")

# ----- Main interactive program -----
def main():
	print("Welcome to the Python Cookbook !")
	while True:
		print("List of available options:")
		print("1: Add a recipe")
		print("2: Delete a recipe")
		print("3: Print a recipe")
		print("4: Print the cookbook")
		print("5: Quit")
		choice = input("Please select an option:\n>> ").strip()

		if choice == "1":
			add_recipe()
		elif choice == "2":
			name = input("Please enter a recipe name to delete:\n>> ").strip()
			delete_recipe(name)
		elif choice == "3":
			name = input("Please enter a recipe name to get its details:\n>> ").strip()
			print_recipe_details(name)
		elif choice == "4":
			print_all_recipes()
		elif choice == "5":
			print("Cookbook closed. Goodbye !")
			break
		else:
			print("Sorry, this option does not exist.\n")

# ----- Entry point -----
if __name__ == "__main__":
	main()