import os
import sys

# Define the path to the directory you want to check
directory_path = '/path/to/your/directory'

# Check the existence of the directory
if os.path.exists(directory_path):
    print(f"The directory '{directory_path}' exists.")
else:
    # Print an error message and exit the program with the appropriate error code
    print(f"The directory '{directory_path}' does not exist. Program terminated.")
    sys.exit(1)  # Set the error code to 1 (you can choose a different error code)

# Continue if the directory exists
print("Continuation of the program after checking the directory.")
