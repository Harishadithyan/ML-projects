import logging
import os
from datetime import datetime

# Log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  # You can use DEBUG, WARNING, ERROR, etc.
    format="[%(asctime)s] [%(levelname)s] [Line:%(lineno)d] - %(message)s",
     level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)

if __name__=="main":
    logging.info("Logging setup complete!")