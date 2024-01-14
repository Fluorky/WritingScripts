import sys
import re
from datetime import datetime

def convert_dates(file_path, target_format):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            print("Original dates:")
            for line in lines:
                match = re.search(r'(\d{2}/\d{2}/\d{4})', line)
                if match:
                    original_date = match.group(1)
                    #print(line)
                    date_object = datetime.strptime(original_date, '%m/%d/%Y')
                    converted_date = date_object.strftime(target_format)
                    print(f"{line.replace(original_date, converted_date)}\n")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python date_converter.py <file_path> <target_format>")
        sys.exit(1)

    file_path = sys.argv[1]
    target_format = sys.argv[2]

    convert_dates(file_path, target_format)
