# ist356fall25
Course Content for IST356


## Contents:

- Syllabus: `syllabus.md` 
- Course Setup Information: `0-intro` folder
- Course topics in each numbered folder: `1-python, 2-ui, 3-data` etc...

## Using the repository

### Student Information

- As a public repository, you have permissions to pull code and get updates
- You **do not** have permissions to update this code on Github. 

### Getting Updates

If your content code is updated, here's how you get it in VS Code:

1. Open your Terminal in VS Code: menu => Terminal => New Terminal
2. In the terminal, enter the command: `git fetch --all` to download the latest updates.
3. Next in the terminal, enter the command: `git reset --hard origin/main` to merge the changes into your local repository and force your working directory to match the update.
   
1. Download the pip dependencies: `uv pip install -r requirements.txt` Ensure you are in the correct python intrepreter. 

### Requirements

The packages necessary to run the code here are found in `requirements.txt` install using `pip` or `uv`as follows:

1. From VS Code, open a terminal: menu => Terminal => New Terminal
2. In the terminal, enter `uv pip install -r requirements.txt`
3. Alternatively `uv pip install --system -r requirements.txt`
