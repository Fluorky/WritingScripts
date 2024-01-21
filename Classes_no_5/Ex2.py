import logging

# Configure the logging module
logging.basicConfig(level=logging.DEBUG, filemode='w')

# Create a logger object
logger = logging.getLogger(__name__)

# Configure a custom log format
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a StreamHandler to display logs on the console for WARNING level and above
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(log_format)

# Create a FileHandler to save all logs at the DEBUG level in the app.log file
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_format)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Log messages of different types
logger.debug("This is a DEBUG message.")
logger.info("This is an INFO message.")
logger.warning("This is a WARNING message.")
logger.error("This is an ERROR message.")

# Close handlers to ensure all logs are saved before the program ends
console_handler.close()
file_handler.close()

