import pickle

#Define function to display each individual recipe
def display_recipe(recipe):
    print('Recipe: ', recipe['name'])
    print('Cooking Time (mins): ', recipe['cooking_time'])
    print('Ingredients: ')
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print('Difficulty: ', recipe['difficulty'])
    print()

#Define function to search for recipes with a user-specified ingredient
def search_ingredient(data):
    #Print list of all ingredients
    print('Available ingredients: ')
    for index, ingredient in enumerate(data['all_ingredients']):
        print(index, ingredient)
    print()
    #Allow user to pick ingredient number from the list above
    try:
        ingredient_searched = data['all_ingredients'][
            int(input('Enter the corresponding number of the ingredient you want to search for: '))
        ]
    except:
        print('Invalid input.')
        return
    else:
        #Return recipes that include the searched ingredient
        matching_recipes = []
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                matching_recipes.append(recipe)
        #Display matching recipes
        print('The following recipes contain ', ingredient_searched, ': ')
        for recipe in matching_recipes:
            display_recipe(recipe)

#Ask user for name of file where recipes are stored
filename = input('Enter the filename where you\'ve stored your recipes: ')

try:
    file = open(filename, 'rb')
    data = pickle.load(file)
except FileNotFoundError:
    print('That file does not exist.')
else:
    search_ingredient(data)
finally:
    print('Happy cooking!')
    file.close()

