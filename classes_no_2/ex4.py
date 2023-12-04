import os

def generate_directory_tree(start_path='.', indent=''):
    # Use os.walk to traverse directories and files
    for root, dirs, files in os.walk(start_path):
        # Print the directory name with the appropriate indentation
        print(f"{indent}Directory: {os.path.basename(root)}")

        # Print files in the current directory with the appropriate indentation
        for file in files:
            print(f"{indent}  File: {file}")

        # Recursively call the function for each subdirectory
        for dir in dirs:
            next_path = os.path.join(root, dir)
            generate_directory_tree(next_path, indent + '  ')

# Use the function to generate the directory structure (default is the current directory)
generate_directory_tree()
