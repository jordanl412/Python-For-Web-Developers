recipes_list = []
ingredients_list = []

def take_recipe():
    name = input('Enter the name of the recipe: ')
    cooking_time = int(input('Enter the cooking time (in minutes): '))
    ingredients = []
    while True:
        ingredient = input('Enter an ingredient (enter "done" if you have finished): ')
        if ingredient == 'done':
            break
        else:
            ingredients.append(ingredient)
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    return recipe

n = int(input('How many recipes would you like to enter?'))

for r in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])
    difficulty = recipe['difficulty']

    if cooking_time < 10 and num_ingredients < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = 'Medium'
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Hard'

for recipe in recipes_list:
    print('Recipe: ', recipe['name'])
    print('Cooking Time (min): ', recipe['cooking_time'])
    print('Ingredients: ')
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print('Difficulty Level: ', recipe['difficulty'])
    print()

print('Ingredients Available Across All Recipes')
print('----------------------------------------')

ingredients_list.sort()
for ingredient in ingredients_list:
    print(ingredient)





