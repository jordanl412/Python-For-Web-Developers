import mysql.connector

# Initialize connection object
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'cf-python',
    passwd = 'password'
)

# Initialize a cursor
cursor = conn.cursor()

# Create a database
cursor.execute('CREATE DATABASE IF NOT EXISTS task_database')

# Allow script to access database
cursor.execute('USE task_database')

#Create a table called Recipes
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
    )''')

# Main Menu code
def main_menu(conn, cursor):
    choice = ''
    # Loop running through Main Menu
    # Continues until user chooses 'quit'
    while(choice != 'quit'):
        print()
        print('Main Menu')
        print('==========================')
        print('What would you like to do? Pick a number:')
        print('  1. Create a new recipe')
        print('  2. Search for a recipe by ingredient')
        print('  3. Update an existing recipe')
        print('  4. Delete a recipe')
        print('  5. View all recipes'
        )
        print('Type "quit" to exit the program.')
        print()
        choice = input('Your choice: ')
        print()

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            view_all_recipes(conn, cursor)


# Definition for create_recipe
def create_recipe(conn, cursor):
    name = input('Recipe name: ')
    cooking_time = int(input('Cooking time (in minutes): '))
    ingredients = []
    #Get ingredients from user
    while True:
        ingredient = input('Enter an ingredient (or enter "done" if you have finished): ')
        if ingredient == 'done':
            break
        else:
            ingredients.append(ingredient)
    difficulty = calculate_difficulty(cooking_time, ingredients)
    ingredients = ', '.join(ingredients)
    cursor.execute('INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)', 
                    (name, ingredients, cooking_time, difficulty))
    conn.commit()
    print('Recipe saved successfully!')
    print()

def calculate_difficulty(cooking_time, ingredients):
    cooking_time = cooking_time
    num_ingredients = len(ingredients)
    
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = 'Medium'
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Hard'
    return difficulty

# Defintion for search_recipe
def search_recipe(conn, cursor):
    all_ingredients = []
    # Stores entire list of ingredients available into results
    cursor.execute('SELECT ingredients FROM Recipes')
    results = cursor.fetchall()
    # Iterates through results list and for each recipe ingreidents tuple
    for recipe_ingredients_list in results:
        # Iterates through reciple ingredients tuple
        for recipe_ingredients in recipe_ingredients_list:
            # Split each recipe ingredients tuple
            recipe_ingredients_split = recipe_ingredients.split(', ')
            # Adds ingredient to all_ingredients
            all_ingredients.extend(recipe_ingredients_split)
            
    # Remove all duplicates from the list
    all_ingredients = list(dict.fromkeys(all_ingredients))

    # Show all available ingredients in all_ingredients
    all_ingredients_list = list(enumerate(all_ingredients))

    print('List of all ingredients: ')
    print('-------------------------')

    for index, tup in enumerate(all_ingredients_list):
        print(str(tup[0]+1) + '. ' + tup[1])

    try:
        # User picks a number (index) for corresponding ingredient, stored as search_ingredient
        ingredient_searched_number = input('Enter the number next to the ingredient you want to search for: ')
        ingredient_searched_index = int(ingredient_searched_number) - 1
        search_ingredient = all_ingredients_list[ingredient_searched_index][1]
        print()
        print('Searching for recipes with', search_ingredient, '...')
        print()

    except:
        print('An unexpected error occurred. Make sure to select a number from the list of ingredients.')

    else:
        # Searches for rows in the table that contain search_ingredient in the ingredients column
        print('The recipe(s) below include(s)', search_ingredient)
        print('-----------------------------------------------------')

        cursor.execute('SELECT * FROM Recipes WHERE ingredients LIKE %s', ('%' + search_ingredient + '%', ))

        results_recipes_with_ingredient = cursor.fetchall()
        for row in results_recipes_with_ingredient:
            print('ID: ', row[0])
            print('Name: ', row[1])
            print('Ingredients: ', row[2])
            print('Cooking Time: ', row[3])
            print('Difficulty: ', row[4])
            print()


    

# Definition for update_recipe
def update_recipe(conn, cursor):
    # Fetch all recipes in the database
    view_all_recipes(conn, cursor)

    # User picks a recipe by ID
    print()
    recipe_id_to_update = int(input('Select the ID of the recipe you want to update: '))

    # User selects what part of the recipe to update
    print()
    print('Update Options')
    print('--------------')
    print('1. Recipe name')
    print('2. Cooking time')
    print('3. Ingredients')
    print()
    column_to_update = int(input('Select the number of the item to update: '))

    # If user selects 1. recipe name
    if column_to_update == 1:
        updated_value = str(input('Enter the updated recipe name: '))
        cursor.execute('UPDATE Recipes SET name = %s WHERE id = %s', (updated_value, recipe_id_to_update))
        conn.commit()
        print('Recipe name updated.')

    # If user selects 2. cooking time
    elif column_to_update == 2:
        updated_value = int(input('Enter the updated cooking time (in minutes): '))
        cursor.execute('UPDATE Recipes SET cooking_time = %s WHERE id = %s', (updated_value, recipe_id_to_update))
        cursor.execute('SELECT ingredients FROM Recipes WHERE id = %s', (recipe_id_to_update,))
        ingredients = cursor.fetchall()[0][0].split(', ')
        difficulty = calculate_difficulty(updated_value, ingredients)
        cursor.execute('UPDATE Recipes SET difficulty = %s WHERE id = %s', (difficulty, recipe_id_to_update))
        conn.commit()
        print('Recipe cooking time updated.')
    
    # If user selects 3. ingredients
    elif column_to_update == 3:
        new_ingredients = input('Enter the updated ingredients: ')
        cursor.execute('UPDATE Recipes SET ingredients = %s WHERE id = %s', (new_ingredients, recipe_id_to_update))
        cursor.execute('SELECT cooking_time FROM Recipes WHERE id = %s', (recipe_id_to_update))
        cooking_time = cursor.fetchall()[0][0]
        difficulty = calculate_difficulty(cooking_time, new_ingredients.split(', '))
        cursor.execute('UPDATE Recipes SET difficulty = %s WHERE id = %s', (difficulty, recipe_id_to_update))
        conn.commit()
        print('Recipe ingredients updated.')

# Definition for delete_recipe
def delete_recipe(conn, cursor):
    view_all_recipes(conn, cursor)
    id_to_delete = int(input('Enter the ID of the recipe you wish to delete: '))
    cursor.execute('DELETE FROM Recipes WHERE id = %s', (id_to_delete,))
    conn.commit()
    print()
    print('Recipe deleted.')

# Definition for view_all_recipes
def view_all_recipes(conn, cursor):
    cursor.execute('SELECT * FROM Recipes')
    all_recipes_results = cursor.fetchall()
    print('All Recipes: ')
    print('=============')
    for row in all_recipes_results:
        print('ID: ', row[0])
        print('Name: ', row[1])
        print('Ingredients: ', row[2])
        print('Cooking Time (in minutes): ', row[3])
        print('Difficulty: ', row[4])
        print()


# Call main_menu
main_menu(conn, cursor)