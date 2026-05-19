import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')
project_name = "DataScienceProject"

list_of_files = [
  ".github/workflows/.gitkeep", # .gitkeep is a placeholder file to keep the empty folders in git
  f"src/{project_name}/__init__.py",
  f"src/{project_name}/components/__init__.py", # for any library and any components needed in the project
  f"src/{project_name}/utils/__init__.py", # for any utility functions
  f"src/{project_name}/utils/common.py", # for any common utility functions
  f"src/{project_name}/config/__init__.py", # for any configuration related files
  f"src/{project_name}/config/configuration.py", 
  f"src/{project_name}/pipeline/__init__.py", # for any pipeline related files
  f"src/{project_name}/entity/__init__.py", # for training pipeline related
  f"src/{project_name}/entity/config_entity.py", 
  f"src/{project_name}/constants/__init__.py", 
  "config/config.yaml", # for any configuration related files
  "schema.yaml", 
  "params.yaml", # for any parameters related files
  "main.py", # for running the project
  "Dockerfile", # for dockerizing the project
  "setup.py", # for installing the project as a package
  "research/research.ipynb", # for any research related files
  "templates/index.html",
  "app.py"
]

for filepath in list_of_files:
  filepath = Path(filepath)
  filedir, filename = os.path.split(filepath)
  if filedir != "":
    os.makedirs(filedir, exist_ok=True)
    logging.info(f"Creating directory: {filedir} for file: {filename}")
  if not os.path.exists(filepath):
    with open(filepath, "w") as f:
      pass
    logging.info(f"Creating file: {filepath}")
  else:
    logging.info(f"File already exists: {filepath}")