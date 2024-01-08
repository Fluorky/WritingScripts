import re

passwords = ['Apple34!rose', 'My87hou#4$', 'abc123', 'Applerose']
pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[*$%!&.]).{8,}$')

for password in passwords:
    if pattern.match(password):
        print(f"{password} - Correct password")
    else:
        print(f"{password} - Uncorrect password")
