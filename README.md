# Python For Web Developers

## Exercise 1
1. Install Python
2. Set Up a Virtual Environment
3. Create a Python Script
4. Set Up IPython Shell
5. Export a Requirements File
6. Create a GitHub Repository

### Install Python
First, install Python on your system. Check your Python version by running the command `python3 --version` in the Terminal.

### Set Up a Virtual Environment
Set up a new virtual environment named "cf-python-base" by running the command `mkvirtualenv cf-python-base` in the Terminal.

### Create a Python Script
Install Visual Studio Code (or another text editor), and create a Python script "add.py". This script will take two numbers from the user input, add them, and print the result.

### Set Up IPython Shell
Set up IPython Shell in the virtual environment "cf-python-base". An IPython shell is similar to the regular Python REPL, with additional features like syntax highlighting, auto-indentation, and robust auto-complete features. Install the IPython Shell with the command `pip install ipython` in the Terminal.

### Export a Requirements File
Generate a “requirements.txt” file from your source environment. To do this, run `pip freeze > requirements.txt` in the Terminal. 
Next, create a new environment called “cf-python-copy” with the `mkvirtualenv cf-python-copy` command. To switch environments, simply use the command `workon <"new environment">`. Once you've moved to the cf-python-copy environment, install packages from the “requirements.txt” file by running the command `pip install -r requirements.txt`.

### Create a GitHub Repository
