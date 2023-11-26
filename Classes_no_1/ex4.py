import os
from collections import Counter

def main():
    folder_path = r'C:\Program Files\Mozilla Firefox'

    # Get a list of files in the folder
    file_names = os.listdir(folder_path)

    # Create a list of file extensions
    file_extensions = [os.path.splitext(file)[1] for file in file_names]

    # Use the Counter class to count the number of unique file extensions
    extensions_counter = Counter(file_extensions)

    # Display the results
    print(f"File extensions in folder {folder_path}:")
    for extension, count in extensions_counter.items():
        print(f"{extension}: {count} files")

if __name__ == '__main__':
    main()
