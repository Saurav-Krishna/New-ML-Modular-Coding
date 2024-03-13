import os , sys
from pathlib import Path
# logging
import logging

# required files and folders 
while True:
    project_name = input("Enter your project name: ")
    if project_name:
        break
# src/__init__.py
# src/componets/__init__.py    
list_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",

    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py",
    "requirements.txt",
    "requirements_dev.txt"
]

for file_path in list_files:
    file_path = Path(file_path)
    # defining dir 
    file_dir, filename = os.path.split(file_path)
    if file_dir:
        os.makedirs(file_dir, exist_ok=True) # skip if folder exists
    #open and generate files 
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
    else:
        logging.info(f"{file_path} already exists")
