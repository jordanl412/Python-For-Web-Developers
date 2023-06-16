import pickle

def take_recipe():
    name = input('Enter recipe name: ')
    cooking_time = int(input('Enter cooking time (in minutes): '))
    ingredients = []

    #Get ingredients from user
    while True:
        ingredient = input('Enter an ingredient (or enter "done" if you have finished): ')
        if ingredient == 'done':
            break
        else:
            ingredients.append(ingredient)
    
    #Create recipe dictionary with name, cooking time, and ingredients
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }

    #Calculate difficulty of recipe
    difficulty = calc_difficulty(recipe)

    #Add difficulty to reicpe dictionary
    recipe['difficulty'] = difficulty

    #Print recipe dictionary
    return recipe

#Define function to calculate recipe difficulty
def calc_difficulty():
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

filename = input('Enter the filename where you\'ve stored your recipes: ')
try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
        print('Recipes loaded successfully!')
#If file doesn't exist, print a message and create a new dictionary
except FileNotFoundError:
    print('File doesn\'t exist - creating a new dictionary.')
    data = {'recipes_list': [], 'all_ingredients': []}
#If there is an unexpected error, print a message and create a new dictionary
except:
    print('An unexpected error occurred - creating a new dictionary.')
    data = {'recipes_list': [], 'all_ingredients': []}
#If no error occurs, close the file
else: file.close()
#If file exists, extract the recipes_list and all_ingredients from the dictionary
finally: 
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

#Get number of recipes to add from user
n = int(value('Enter the number of recipes you\'d like to add: '))

#Take recipes and append to recipes_list
for i in range(n):
    recipe = take_recipe()

    #Update all_ingredients with new ingredients
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

    #Add recipe to recipes list
    recipes_list.append(recipe)

#Save recipes_list and all_ingredients to data dictionary
data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}

#Save the dictionary to a user-specified file
filename = input('Enter the file name where you\'d like to store your recipes: ')
with open(filename, 'wb') as file:
    pickle.dump(data, file)
    print('Recipes saved successfully!')
    file.close()