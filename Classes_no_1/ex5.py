import os

def main():

    folder_path = r'/Users/maciej/music'

    # Get a list of files in the folder
    file_names = os.listdir(folder_path)

    # Create a dictionary with file names and their sizes
    file_size_dict = {file: os.path.getsize(os.path.join(folder_path, file)) for file in file_names}

    # Sort the dictionary by file sizes (from largest to smallest)
    sorted_file_size_dict = dict(sorted(file_size_dict.items(), key=lambda item: item[1], reverse=True))

    # Display the sorted dictionary
    print("Sorted file sizes (from largest to smallest):")
    for file, size in sorted_file_size_dict.items():
        print(f"{file}: {size} bytes")


if __name__ == '__main__':
    main()
