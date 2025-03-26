import os
import sys
import logging

# Define the logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory and file path for logs
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Define the log message format
    handlers=[
        logging.FileHandler(log_filepath),  # Log messages to a file
        logging.StreamHandler(sys.stdout)   # Log messages to the console
    ]
)

# Create a logger instance for the project
logger = logging.getLogger("mlProjectLogger")