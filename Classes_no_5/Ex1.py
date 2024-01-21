import logging

# Configure the logging module
logging.basicConfig(level=logging.INFO)

# Create a logger object
logger = logging.getLogger(__name__)

# Log messages of different types
logger.info("This is an INFO message.")
logger.warning("This is a WARNING message.")
logger.error("This is an ERROR message.")
