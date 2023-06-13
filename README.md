# Python For Web Developers

## Exercise 1
1. [Install Python](#install-python)
2. [Set Up a Virtual Environment](#set-up-a-virtual-environment)
3. [Create a Python Script](#create-a-python-script)
5. [Set Up IPython Shell](#set-up-ipython-shell)
7. [Export a Requirements File](#export-a-requirements-file)
8. [Create a GitHub Repository](#create-a-github-repository)

### Install Python
First, install Python on your system. Check your Python version by running the command `python3 --version` in the Terminal.

![Step 1](./Exercise1.1/Screenshots/step_1_python_version.png)

### Set Up a Virtual Environment
Set up a new virtual environment named "cf-python-base" by running the command `mkvirtualenv cf-python-base` in the Terminal.

![Step 2](./Exercise1.1/Screenshots/step_2_new_environment.png)

### Create a Python Script
Install Visual Studio Code (or another text editor), and create a Python script "add.py". This script will take two numbers from the user input, add them, and print the result.

![Step 3a](./Exercise1.1/Screenshots/step_3_add.py_file_code.png)
![Step 3b](./Exercise1.1/Screenshots/step_3_add.py_file.png)

### Set Up IPython Shell
Set up IPython Shell in the virtual environment "cf-python-base". An IPython shell is similar to the regular Python REPL, with additional features like syntax highlighting, auto-indentation, and robust auto-complete features. Install the IPython Shell with the command `pip install ipython` in the Terminal.

![Step 4](./Exercise1.1/Screenshots/step_4_install_ipython.png)

### Export a Requirements File
Generate a “requirements.txt” file from your source environment. To do this, run `pip freeze > requirements.txt` in the Terminal. 
Next, create a new environment called “cf-python-copy” with the `mkvirtualenv cf-python-copy` command. To switch environments, simply use the command `workon <"new environment">`. Once you've moved to the cf-python-copy environment, install packages from the “requirements.txt” file by running the command `pip install -r requirements.txt`.

![Step 5a](./Exercise1.1/Screenshots/step_5(a)_pip_freeze_requirements.png)
![Step 5b](./Exercise1.1/Screenshots/step_5(b)_new_environment.png)
![Step 5c](./Exercise1.1/Screenshots/step_5(b)_pip_install_requirements.png)

### Create a GitHub Repository
Create a new GitHub Repository for the Achievement.

## Exercise 2
1. [Create Data Structure](#create-data-structure)
2. [Create Recipe 1](#create-recipe-1)
3. [Create Recipe List](#create-recipe-list)
4. [Create 4 More Recipes](#create-4-more-recipes)
5. [Print Lists of Ingredients](#print-lists-of-ingredients)

### Create Data Structure
Create a data structure named `recipe_1` that contains the following keys:
- `name` (str): Contains the name of the recipe
- `cooking_time` (int): Contains the cooking time in minutes
- `ingredients` (list): Contains a number of ingredients, each of the str data type

![Step 1](./Exercise1.2/step1_recipe_1.png)

_A dictionary is a suitable data structure for this step. It uses key-value pairs, which works for the name, cooking time, and ingredients keys while allowing different values depending on the specific recipe._

### Create Recipe 1
Make `recipe_1` carry the following attributes:
- Name: Tea
- Cooking time: 5 minutes
- Ingredients: Tea leaves, Sugar, Water

![Step 2](./Exercise1.2/step2_recipe_1.png)

### Create Recipe List
Create an outer structure called `all_recipes`, and then add `recipe_1` to it.

![Step 3](./Exercise1.2/step3_append_recipe_1.png)

_This outer structure will want to be sequential in nature, where multiple recipes can be stored and modified as required. Therefore, it is best to make it a list._

### Create 4 More Recipes
Create 4 more recipes (`recipe_2`, `recipe_3`, `recipe_4`, and `recipe_5`), an add them to `all_recipes`.

![Step 4](./Exercise1.2/step4_add_recipes.png)

### Print List of Ingredients
Print the ingredients of each recipe as five different lists.

![Step 5](./Exercise1.2/step5_print_ingredients.png)

