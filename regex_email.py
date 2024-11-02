import re

def validate_email(email):
    # Define the regex pattern for a valid email
    pattern = r"^(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,})$"
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email, re.IGNORECASE):
        return True
    else:
        return False

# Test the function with some email addresses
emails = [
    "user@example.com",
    "username@domain.co.in",
    "user.name+tag@domain.com",
    "user@domain",
    "user@.com",
    "user@domain.com",
    "user@domain.c",
    "user@domain-toolongextension",
    "user@sub-domain.example.com"
]

for email in emails:
    if validate_email(email):
        print(f"{email} is a valid email.")
    else:
        print(f"{email} is not a valid email.")
