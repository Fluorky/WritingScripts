import sys
import re

def egrep(pattern, file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if re.search(pattern, line):
                    print(line, end='')
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python egrep.py <pattern> <file_path>")
        sys.exit(1)

    pattern = sys.argv[1]
    file_path = sys.argv[2]

    egrep(pattern, file_path)
