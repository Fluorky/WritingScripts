import os

def calculate_directory_size(start_path='.'):
    total_size = 0
    total_files = 0
    total_dirs = 0
    largest_dirs = []

    for root, dirs, files in os.walk(start_path):
        total_dirs += 1
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
            total_files += 1

    # Find the three largest directories
    dir_sizes = [(dir, sum(os.path.getsize(os.path.join(root, f)) for f in files)) for root, dirs, files in os.walk(start_path)]
    largest_dirs = sorted(dir_sizes, key=lambda x: x[1], reverse=True)[:3]

    return total_size, total_files, total_dirs, largest_dirs

# Use the function to calculate the directory size (default is the current directory)
total_size, total_files, total_dirs, largest_dirs = calculate_directory_size()

# Print the results
print(f"Total size of files: {total_size} B")
print(f"Number of files: {total_files}")
print(f"Number of directories: {total_dirs}")
print("Three largest directories:")
for dir_info in largest_dirs:
    print(f"  Directory: {dir_info[0]}, Size: {dir_info[1]} B")
