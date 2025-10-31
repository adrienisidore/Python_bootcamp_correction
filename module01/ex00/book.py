
from datetime import datetime
from recipe import Recipe
# Contient une liste de recettes, appartenant a un des types suivants : starter, lunch et dessert
class Book:

	def __init__(self, name=None, last_update=None, creation_date=None, recipes_list=None):
		
		if not isinstance(name, str):
			raise TypeError("Book's name must be a string")
		self.name = name

		if last_update is not None and not isinstance(last_update, datetime):
			raise TypeError("last_update must be a datetime object")
		self.last_update = last_update if last_update else datetime.now()

		if creation_date is not None and not isinstance(creation_date, datetime):
			raise TypeError("creation_date must be a datetime object")
		self.creation_date = creation_date if creation_date else datetime.now()

		if recipes_list is None:
			self.recipes_list = {
				"starter": [],
				"lunch": [],
				"dessert": []
			}
		else:
			# check si recipe_list est un dict, et que chaque cle est une str
			if not isinstance(recipes_list, dict) or not all(isinstance(k, str) for k in recipes_list.keys()):
				raise TypeError("recipes_list must be a dictionnary with str-keys")
			expected_keys = {"starter", "lunch", "dessert"}# set : type natif de Python, represente un ensemble non ordonne d'elements uniques
			# check qu'il n'existe que 3 cles : "starter", "lunch", "dessert"
			if set(recipes_list.keys()) != expected_keys:
				raise ValueError("invalid recipes_list keys")
			# pour chaque tuple cle/valeur on check que ...
			for (key, value) in recipes_list.items():
				# la valeur est bien une liste
				if not isinstance(value, list):
					raise TypeError(f"{key} must be a list")
				# cette liste n'est compose que de Recipe
				if not all(isinstance(r, Recipe) for r in value):
					raise TypeError(f"all elements in {key} must be Recipe objects")
			self.recipes_list = recipes_list


	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		if not isinstance(name, str):
			raise ValueError("get_recipe_by_name takes str as argument")
		for (recipe_type, recipes) in self.recipes_list.items():
			for recipe in recipes:
				if recipe.name == name:
					return recipe
		return None


	def get_recipes_by_types(self, recipe_type):
		"""Gets all recipes names for a given recipe_type """
		if recipe_type not in {"starter", "lunch", "dessert"}:
			raise ValueError("invalid recipe_type, please enter : <starter> <lunch> <dessert>")
		return self.recipes_list[recipe_type]

	
	def add_recipe(self, recipe):
		"""Adds a recipe to the book and updates last_update"""
		if not isinstance(recipe, Recipe):
			raise TypeError(f"add_recipe only accepts Recipe objetcs")
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update = datetime.now()
