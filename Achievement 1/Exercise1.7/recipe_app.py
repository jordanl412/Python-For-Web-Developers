from sqlalchemy import create_engine, Column, or_
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def is_alpha_space_or_hyphen(s):
    return all(c.isalpha() or c.isspace() or c == '-' for c in s)

# Create an engine to connect to the database
engine = create_engine('mysql://cf-python:password@localhost/task_database')

# Generate and bind the Session class to the engine
Session = sessionmaker(bind=engine)

# Initialize the session object
session = Session()

# Create declarative base class
Base = declarative_base()

# Create Recipe class
class Recipe(Base):
    __tablename__ = 'final_recipes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
    # Define __repr__ method for a quick representation of the recipe
    def __repr__(self):
        return '<Recipe ID:' + str(self.id) + '-' + self.name + ', ' + self.difficulty + '>'
    # Define __str__ method for well-formatted version of the recipe
    def __str__(self):
        return '\nRecipe Name: ' + str(self.name) + \
        '\nCooking Time: ' + str(self.cooking_time) + ' minutes' + \
        '\nIngredients: ' + str(self.ingredients) + \
        '\nDifficulty: ' + str(self.difficulty)

    # Define method to calculate difficulty
    def calculate_difficulty(self):
        cooking_time = self.cooking_time
        num_ingredients = len(self.ingredients.split(', '))
        
        if cooking_time < 10 and num_ingredients < 4:
            self.difficulty = 'Easy'
        elif cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = 'Medium'
        elif cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = 'Intermediate'
        else:
            self.difficulty = 'Hard'
        return self.difficulty

    # Define method to retrieve ingredients string as a list
    def return_ingredients_as_list(self):
        ingredients_as_list = ''
        if self.ingredients == '':
            ingredients_as_list = []
            return ingredients_as_list
        else:
            ingredients_as_list = self.ingredients.split(', ')
            return ingredients_as_list
    
# Create corresponding table on the database
Base.metadata.create_all(engine)

# Create recipe function
def create_recipe():
    # Collect recipe name from user
    name = input('Recipe name: ')
    print()
    # Check that recipe name is alphanumeric and 50 characters or less
    while not is_alpha_space_or_hyphen(name) or (len(name) > 50):
        print()
        print('Recipe name can only include letters, spaces, and hyphens, and must be 50 characters or less.')
        print()
        name = input('Recipe name: ')
        print()
    # Collect cooking time from user
    cooking_time = input('Cooking time (in minutes): ')
    print()
    # Check that cooking time is numeric
    while not cooking_time.isnumeric():
        print()
        print('Cooking time must be a number.')
        print()
        cooking_time = input('Cooking time (in minutes): ')
        print()
    cooking_time = int(cooking_time)
    # Collect ingredients from user
    # Ask how many ingredients from user
    num_of_ingredients = input('Number of ingredients: ')
    # Check that number of ingredients is a numeric
    while not num_of_ingredients.isnumeric():
        print()
        print('Please enter a number.')
        print()
        num_of_ingredients = input('Number of ingredients: ')
        print()
    num_of_ingredients = int(num_of_ingredients)
    # Adding ingredients
    ingredients = []
    for i in range(num_of_ingredients):
        ingredient = input(f'\nEnter ingredient {i+1}: ')
        # Check that ingredient is alphabetical
        while not is_alpha_space_or_hyphen(ingredient):
            print()
            print('Ingredient can only include letters, spaces, and hyphens.')
            print()
            ingredient = input(f'\nEnter ingredient {i+1}: ')
            print()
        # Add ingredient to list of ingredients
        ingredients.append(ingredient)
    
    # Convert list of ingredients into a string separated by commas
    ingredients = ', '.join(ingredients)

    # Create new recipe object
    recipe_entry = Recipe(
        name=name,
        cooking_time=cooking_time,
        ingredients=ingredients
    )

    # Calculate difficulty of new recipe object
    recipe_entry.calculate_difficulty()

    # Add and commit changes to database
    session.add(recipe_entry)
    session.commit()
    print()
    print('Recipe saved.')
    print()

# View all recipes function
def view_all_recipes():
    # Retrieve all recipes from database
    all_recipes = session.query(Recipe).all()
    # If no recipes, inform the user and exit the function
    if len(all_recipes) == 0:
        print()
        print('There are no recipes in the database.')
        print()
        return None
    else:
        print()
        print('All recipes in the database:')
        print('----------------------------')
        for recipe in all_recipes:
            print(recipe)
            print()
    
# Search recipes by ingredients function
def search_by_ingredients():
    # Check if there are any recipe entries
    number_of_recipes = session.query(Recipe).count()
    if number_of_recipes == 0:
        print()
        print('There are no recipes to search!')
        print()
        return None
    results = session.query(Recipe.ingredients).all()
    # Add all ingredients to a list
    all_ingredients = []
    for recipe_ingredients_list in results:
        ingredients = recipe_ingredients_list[0].split(', ')
        for ingredient in ingredients:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    # Show user list of all ingredients
    print()
    print('All ingredients:')
    print('----------------')
    for index, ingredient in enumerate(all_ingredients):
        print(f'{index+1}. {ingredient}')
        print()
    # Ask user which ingredient to search for
    search_ingredients = input('Enter the number(s) of the ingredient(s) you want to search for, separated by spaces: ').split()
    for i in search_ingredients:
        if not i.isnumeric() or int(i) > len(all_ingredients):
            print()
            print('Sorry, that is not a valid ingredient number. Please select a number from the list above.')
            print()
            return None
    search_ingredients = [all_ingredients[int(i)-1] for i in search_ingredients]
    # Collect ingredient-containing recipes from database
    conditions_all = []
    conditions_any = []
    for ingredient in search_ingredients:
        like_term = '%' + ingredient + '%'
        conditions_all.append(Recipe.ingredients.like(like_term))
        conditions_any.append(Recipe.ingredients.like(like_term))
    recipes_all = session.query(Recipe).filter(*conditions_all).all()
    recipes_any = session.query(Recipe).filter(or_(*conditions_all)).all()

    print()
    print('The following recipes contain all searched ingredients:')
    print('-------------------------------------------------------')
    if len(recipes_all) == 0:
        print('None')
    for recipe in recipes_all:
        print(recipe)
    print()
    print('The following recipes contain at least one searched ingredient:')
    print('---------------------------------------------------------------')
    if len(recipes_any) == 0:
        print('None')
    for recipe in recipes_any:
        print(recipe)
    
# Edit recipe function
def edit_recipe():
    # Check if there are any recipe entries
    number_of_recipes = session.query(Recipe).count()
    if number_of_recipes == 0:
        print()
        print('There are no recipes to search!')
        print()
        return None
    # Show the user all recipes (recipe id and name)
    results = session.query(Recipe.id, Recipe.name).all()
    print()
    print('All recipes:')
    print('------------')
    for result in results:
        print(f'{result[0]}. {result[1]}')
        print()
    # User picks recipe by id
    chosen_id = input('Enter the number of the recipe you want to edit: ')
    while not chosen_id.isnumeric():
        print()
        print('Please enter a number from the list above.')
        print()
        chosen_id = input('Enter the number of the recipe you want to edit: ')
        print()
    # Retrieve and print recipe to edit
    recipe_to_edit = session.query(Recipe).filter_by(id=chosen_id).first()
    print()
    print('Recipe to edit:')
    print('---------------')
    print(recipe_to_edit)
    print()
    print('Edit options:')
    print('\t1. Recipe Name')
    print('\t2. Cooking Time')
    print('\t3. Ingredients')
    print()
    # User selects which attribute to edit
    attribute_to_edit = input('Select the number of the attribute you want to edit: ')
    while not attribute_to_edit.isnumeric() or int(attribute_to_edit) > 3:
        print()
        print('Please select a number from the list above.')
        print()
        attribute_to_edit = input('Select the number of the attribute you want to edit: ')
        print()
    # Edit recipe name
    if attribute_to_edit == '1':
        print()
        new_name = input('Enter the updated recipe name: ')
        while not is_alpha_space_or_hyphen(new_name) or (len(new_name) > 50):
            print()
            print('Recipe name can only include letters, spaces, and hyphens, and must be 50 characters or less.')
            print()
            new_name = input('Enter the updated recipe name: ')
            print()
        recipe_to_edit.name = new_name
    # Edit cooking time
    if attribute_to_edit == '2':
        print()
        new_cooking_time = input('Enter the updated cooking time (in minutes): ')
        while not new_cooking_time.isnumeric():
            print()
            print('Cooking time must be a number.')
            print()
            new_cooking_time = input('Enter the updated cooking time (in minutes): ')
            print()
        recipe_to_edit.cooking_time == int(new_cooking_time)
    # Edit ingredients
    elif attribute_to_edit == '3':
        print()
        new_ingredients_number = input('How many ingredients do you want to add? ')
        new_ingredients = []
        for i in range(int(new_ingredients_number)):
            print()
            ingredient = input(f'Enter ingredient {i+1}: ')
            while not is_alpha_space_or_hyphen(ingredient):
                print()
                print('Ingredients can only include letters, spaces, and hyphens')
                print()
                ingredient = input('Enter ingredient ' + (i+1) + ': ')
                print()
            new_ingredients.append(ingredient)
        new_ingredients = ', '.join(new_ingredients)
        recipe_to_edit.ingredients = new_ingredients
    # Edit difficulty based on new cooking time or ingredients
    recipe_to_edit.calculate_difficulty()
    session.commit()
    print()
    print('Recipe updated!')
    print()

# Delete recipe function
def delete_recipe():
    # Check if there are any recipe entries
    number_of_recipes = session.query(Recipe).count()
    if number_of_recipes == 0:
        print()
        print('There are no recipes to search!')
        print()
        return None
    # Show the user all recipes (recipe id and name)
    results = session.query(Recipe.id, Recipe.name).all()
    print()
    print('All recipes:')
    print('------------')
    for result in results:
        print(f'{result[0]}. {result[1]}')
        print()
    # User picks recipe by id
    chosen_id = input('Enter the number of the recipe you want to delete: ')
    while not chosen_id.isnumeric():
        print()
        print('Please enter a number from the list above.')
        print()
        chosen_id = input('Enter the number of the recipe you want to delete: ')
        print()
    # Retrieve and print recipe to edit
    recipe_to_delete = session.query(Recipe).filter_by(id=chosen_id).first()
    print()
    print('Recipe to delete:')
    print('---------------')
    print(recipe_to_delete)
    print()
    verify_delete = input('Are you sure you want to delete this recipe? Enter "yes" or "no": ')
    if verify_delete == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print()
        print('Recipe deleted.')
        print()
    elif verify_delete == 'no':
        print()
        print('Recipe not deleted.')
        print()
        return None
    else:
        print()
        print('Please type either "yes" or "no".')
        print()
        verify_delete = input('Are you sure you want to delete this recipe? Enter "yes" or "no": ')
        print()
    
# Main Menu code
def main_menu():
    choice = ''
    # Loop running through Main Menu
    # Continues until user chooses 'quit'
    while(choice != 'quit'):
        print()
        print('Main Menu')
        print('==========================')
        print('What would you like to do?')
        print('1. Create a new recipe')
        print('2. View all recipes')
        print('3. Search for recipes by ingredient(s)')
        print('4. Update an existing recipe')
        print('5. Delete a recipe')
        print('Type "quit" to exit the program.')
        print()
        choice = input('Enter a menu option number, or type "quit": ')
        print()

        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredients()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == 'quit':
            print()
            print('Exiting...')
            session.close()
            engine.dispose()
            break
        else:
            print()
            print('Invalid choice. Please enter a number from the list above, or type "quit".')
            print()
            choice = input('Enter a menu option number, or type "quit": ')

# Call main_menu function
if __name__ == '__main__':
    main_menu()


    











            








    

    

