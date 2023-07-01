class Recipe:
    all_ingredients = []
    
    # Initializes new object in Recipe class
    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None

    # Returns recipe name
    def get_name(self):
        return self.name

    # Sets new recipe name
    def set_name(self, name):
        self.name = name

    # Returns cooking time
    def get_cooking_time(self):
        return self.cooking_time

    # Sets new cooking time
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    # Adds ingredients to recipe's ingredients list and updates ingredients
    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()

   # Returns recipe's ingredients list
    def get_ingredients(self):
        return self.ingredients

    # Calculates difficulty of a recipe based on cooking time and number of ingredients
    def calculate_difficulty(self):
        cooking_time = self.cooking_time
        num_ingredients = len(self.ingredients)
    
        if cooking_time < 10 and num_ingredients < 4:
            difficulty = 'Easy'
        elif cooking_time < 10 and num_ingredients >= 4:
            difficulty = 'Medium'
        elif cooking_time >= 10 and num_ingredients < 4:
            difficulty = 'Intermediate'
        else:
            difficulty = 'Hard'
    
    # Returns recipe difficulty (or calculates difficulty if not already calculated)
    def get_difficulty(self):
        if self.difficulty == None:
            self.calculate_difficulty()
        return self.difficulty

    # Checks if an ingredient is in the recipe's ingredients list
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients
    
    # Adds recipe's ingredients to an ingredient master list (from all recipes) if not already on the master list
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)
            
    # Prints string representation of entire recipe
    def __str__(self):
        return f"Recipe Name: {self.name}\n \
        Ingredients: {', '.join(self.ingredients)}\n \
        Cooking Time: {self.cooking_time} minutes\n \
        Difficulty: {self.get_difficulty()}\n"

    # Searches for recipes with a specified ingredient
    # data = all recipes
    # search_term = ingredient from user input
    def recipe_search(data, search_term):
        print('Recipes that contain ' + search_term + ':\n')
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)

# Main code
tea = Recipe('Tea', 5)
tea.add_ingredients('Tea Leaves', 'Sugar', 'Water')
print(tea)

coffee = Recipe('Coffee', 5)
coffee.add_ingredients('Coffee Powder', 'Sugar', 'Water')
print(coffee)

cake = Recipe('Cake', 50)
cake.add_ingredients('Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk')
print(cake)

banana_smoothie = Recipe('Banana Smoothie', 5)
banana_smoothie.add_ingredients('Bananas', 'Peanut Butter', 'Sugar', 'Ice Cubes')
print(banana_smoothie)

recipes_list = [tea, coffee, cake, banana_smoothie]

for ingredient in ['Water', 'Sugar', 'Bananas']:
    Recipe.recipe_search(recipes_list, ingredient)

        


        
    