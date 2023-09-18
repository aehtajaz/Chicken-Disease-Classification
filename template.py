# Import necessary libraries and modules
import os
from pathlib import Path
import logging 

# Configure the logging system
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = "Chicken-Disease-Classifier"

# Define a list of files and directories
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",

    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Iterate through the list of files and directories
for filePath in list_of_files:
    # Convert the file path string into a Path object
    filePath = Path(filePath)
    
    # Separate the file path into directory path and file name
    filedir, filename = os.path.split(filePath)
    
    # Check if the directory path is not empty
    if filedir != "":
        # Create the directory if it doesn't exist
        os.makedirs(filedir, exist_ok=True)
        
        # Log the creation of the directory
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
        
    # Check if the file doesn't exist or is empty
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0):
        # Create an empty file
        with open(filePath, "w") as f:
            pass
            
            # Log the creation of the empty file
            logging.info(f"Creating empty file: {filePath}")
            
    else:
        # Log that the file already exists
        logging.info(f"{filename} is already exists")