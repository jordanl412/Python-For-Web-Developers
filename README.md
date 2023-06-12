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

![Step 5a](./Exercise1.1/Screenshots/step_5_pip_freeze_requirements.png)
![Step 5b](./Exercise1.1/Screenshots/step_5_new_environment.png)
![Step 5c](./Exercise1.1/Screenshots/step_5_pip_install_requirements.png)

### Create a GitHub Repository
Create a new GitHub Repository for the Achievement.
