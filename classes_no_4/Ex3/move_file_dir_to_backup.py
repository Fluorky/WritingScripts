import sys
import shutil
import os
from datetime import datetime

def backup_files(file_paths, backup_dir=None):
    if not backup_dir:
        backup_dir = os.path.join(os.getcwd(), 'backup_dir')

    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    for file_path in file_paths:
        try:
            base_name = os.path.basename(file_path)
            name, extension = os.path.splitext(base_name)
            new_name = f"{name}_{timestamp}{extension}"
            destination = os.path.join(backup_dir, new_name)
            shutil.copy2(file_path, destination)
            print(f"Backup created: {destination}")
        except Exception as e:
            print(f"Error copying {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python move_file_dir_to_backup.py <file_path1> <file_path2> ... [-d <backup_dir>]")
        sys.exit(1)

    file_paths = sys.argv[1:-2] if sys.argv[-2] == '-d' else sys.argv[1:]
    backup_dir_index = sys.argv.index('-d') + 1 if '-d' in sys.argv else None
    backup_dir = sys.argv[backup_dir_index] if backup_dir_index else None

    backup_files(file_paths, backup_dir)
