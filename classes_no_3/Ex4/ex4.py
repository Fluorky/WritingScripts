import re

# Function to transform date formats
def transform_date(match):

  
    day, month, year = match.groups()
    print("month",len(month))
    print("year",len(year))
    print("day",len(day))
    print(" ")
    if(len(year)==4):
        if(int(month)<=12):
            return f"{day}/{month}/{year}"
        else:
            return f"{month}/{day}/{year}"
    else:
        if(int(month)<=12):
         return f"{year}/{month}/{day}"
        else:
         return f"{month}/{year}/{day}"


    

# Read content from daty.txt
with open("daty.txt", "r") as file:
    content = file.read()

# Define regular expression patterns for different date formats
date_patterns = [
    r"(\d{2})[-./](\d{2})[-./](\d{4})",   # DD-MM-YYYY, MM/DD/YYYY, YYYY/MM/DD
    r"(\d{4})[-./](\d{2})[-./](\d{2})"    # YYYY-MM-DD, YYYY/MM/DD
]

# Process each date pattern and transform the dates
for pattern in date_patterns:
    content = re.sub(pattern, transform_date, content)

# Print the transformed content
print(content)
