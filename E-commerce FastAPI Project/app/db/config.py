import logging

# Configure logging settings for the application
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",  # Log message format
    handlers=[
        logging.FileHandler("app.log"),  # Log messages to a file named 'app.log'
        logging.StreamHandler()          # Also output log messages to the console
    ]
)

# Create a logger instance for the 'ecommerce' application
logger = logging.getLogger("ecommerce")