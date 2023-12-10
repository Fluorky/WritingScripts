import re

def validate_polish_numbers(phone_number):
    # Define a regular expression pattern for matching Polish phone numbers
    polish_phone_pattern = r'^(\+48\s?)?(\d{3}[-.\s]?){2}\d{3}$'

    # Use re.match to check if the phone number matches the pattern
    match = re.match(polish_phone_pattern, phone_number)

    # Return True if there is a match, False otherwise
    return bool(match)

polish_test_data = [
    "+48 123 456 789",
    "123 456 789",
    "123-456-789",
    "123.456.789",
    "+48 123-456-789",
    "+48 123.456.789",
    "+48123456789",
    "48123456789",
    "+49 123 456 789"  # Niemiecki numer, nie powinien zostać zaakceptowany
]

# Test the phone numbers and print the results
for phone_number in polish_test_data:
    result = validate_polish_numbers(phone_number)
    print(f"{phone_number}: {result}")
