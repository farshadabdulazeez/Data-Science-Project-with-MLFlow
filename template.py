import os
from pathlib import Path
import logging

# Configure logging to display timestamps and messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = "mlProject"

# List of files and directories to be created
list_of_files = [
    ".github/workflows/.gitkeep",  # Keep GitHub workflows directory tracked
    f"src/{project_name}/__init__.py",  # Package initialization file
    f"src/{project_name}/components/__init__.py",  # Components package
    f"src/{project_name}/utils/__init__.py",  # Utilities package
    f"src/{project_name}/utils/common.py",  # Common utility functions
    f"src/{project_name}/config/__init__.py",  # Configuration package
    f"src/{project_name}/config/configuration.py",  # Configuration settings
    f"src/{project_name}/pipeline/__init__.py",  # Pipeline package
    f"src/{project_name}/entity/__init__.py",  # Entity package
    f"src/{project_name}/entity/config_entity.py",  # Configuration entity definitions
    f"src/{project_name}/constants/__init__.py",  # Constants package
    "config/config.yaml",  # Configuration file
    "params.yaml",  # Parameters file for model training
    "schema.yaml",  # Schema definition file
    "main.py",  # Main entry script
    "app.py",  # Application script (for API or web app)
    "Dockerfile",  # Docker container setup file
    "requirements.txt",  # Dependencies list
    "setup.py",  # Setup script for packaging
    "research/trials.ipynb",  # Jupyter notebook for research/experiments
    "templates/index.html",  # HTML template for UI
    "test.py"  # Testing script
]

# Iterate through the list and create required files and directories
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object for OS compatibility
    filedir, filename = os.path.split(filepath)  # Split directory and filename

    # Create directory if it doesn't exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create an empty file if it does not exist or if it is empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
