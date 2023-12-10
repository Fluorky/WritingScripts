import re

text = """
jan.kowalski@example.com
maria.nowak@uniwersytet.edu.pl
niepoprawny-email@przyklad
kontakt@firma.org
jan.kowalski@example
"""

# Define a regular expression pattern for matching email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Find all matches in the text using the regular expression
matches = re.findall(email_pattern, text)

# Print the identified email addresses
for match in matches:
    print(match)
