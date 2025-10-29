class Recipe:

	# variables de classe <ici>

	#constructeur
	def __init__(self, name=None, cooking_lvl=0, cooking_time=0, ingredients=None, description="", recipe_type=""):

		if not isinstance(name, str):
			raise TypeError("Recipe's name must be a string")
		if not isinstance(cooking_lvl, int):
			raise TypeError("cooking_lvl must be an integer")
		if not isinstance(cooking_time, int):
			raise TypeError("cooking_lvl must be an integer")
		if not isinstance(ingredients, list):
			raise TypeError("ingredients must be a list")
		# Checker que ingredients e
		if not all(isinstance(i, str) for i in ingredients):# all check si tous les elements sont true
			raise ValueError("each ingredient must be a string")			
		if not isinstance(description, str):
			raise TypeError("description must be a string")
		if not isinstance(recipe_type, str):
			raise TypeError("recipe_type must be a string")
		if name is None:
			raise ValueError("Give your recipe a name")
		if cooking_lvl not in range(1, 6):
			raise ValueError("cooking_lvl is between 1 and 5")
		if cooking_time < 0:
			raise ValueError("cooking time must be a positine integer")
		if recipe_type not in {"starter", "lunch", "dessert"}:
			raise ValueError("invalid recipe_type")
		
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients if ingredients else [] # Pour eviter que tous les ingredients partagent la meme liste
		self.description = description
		self.recipe_type = recipe_type

#Surcharge du casting str()
	def __str__(self):
		"""Returns the string to print with the recipe’s info"""
		return f"{self.name}"



