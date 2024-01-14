import sys
import re

def count_keywords(file_path, *keywords):
    keyword_counts = {keyword: 0 for keyword in keywords}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                for keyword in keywords:
                    matches = re.findall(r'\b{}\b'.format(re.escape(keyword)), line, flags=re.IGNORECASE)
                    keyword_counts[keyword] += len(matches)

        print(f"Keyword counts in file {file_path}:")
        for keyword, count in keyword_counts.items():
            print(f"{keyword}: {count}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python count_words_from_file.py <file_path> <keyword1> <keyword2> ...")
        sys.exit(1)

    file_path = sys.argv[1]
    keywords = sys.argv[2:]

    count_keywords(file_path, *keywords)
