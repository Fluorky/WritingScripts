import os
import sys

def folder_report(directory_path):
    total_size = 0
    total_files = 0
    total_directories = 0

    try:
        for root, dirs, files in os.walk(directory_path):
            total_directories += len(dirs)
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
                total_files += 1

        print(f"Directory: {directory_path}")
        print(f"Total size: {total_size} bytes")
        print(f"Total number of files: {total_files}")
        print(f"Total number of directories: {total_directories}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python folder_report.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    folder_report(directory_path)
