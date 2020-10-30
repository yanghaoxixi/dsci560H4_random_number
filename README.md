# Random number generator
Same as repository for hw2, generate 1000 random number and visualize it. But this is for hw4, which will be implement on virtual environment and Binder.

## Brief intro
- a.py is to generate 1000 random number X between 0~100
- b.py is to generate corresponding 1000 number Y = 3 * X + 6
- c.py is to visualization numbers generated in a.py and b.py

## Virtual environment creation
### Step 1: create a blank virtual environment and name it dsci560H4
- `pip install virtualenv` to install package of virtual environment
- `py -m venv dsci560H4` to create a virtual environment called dsci560H4

### Step 2: Activate the environment and install the dependencies 
- `.\dsci560H4\Scripts\activate` to activate the virtual environment for implement scripts.
![screenshot](/screenshot/activated.png)
- `pip install matplotlib` to install package matplotlib for visualization
![screenshot](/screenshot/matplot1.png)

### Step 3: Run the script for number generator in activated environment
- `python c.py` to run scripts generating number and visualizatioin
- screenshot for generating number
![screenshot](/screenshot/generating_number.png)
- screenshot for visualization
![screenshot](/screenshot/visualization.png)

### Step 4: Extract the dependencies and compare with packages manually installed
- `pip freeze > requirements.txt` to save the dependencies into file requirements.txt
![screenshot](/screenshot/freeze.png)
- **Comparison:** I only manually installed matplotlib package for implement visualization, but when I extracted dependencies, I found there are many packages installed. This is because package matplotlib is based on other packages to work, such as numpy. So, even though I only installed one package, many packages will be install indeed.

## Binder badge to notebook
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yanghaoxixi/dsci560H4_random_number/main?filepath=run_visualization.ipynb)
