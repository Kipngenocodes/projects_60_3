import re

def validate_password(password):
    # Define the regex pattern for a strong password
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    # Use re.match to check if the password matches the pattern
    if re.match(pattern, password):
        return True
    else:
        return False

# Test the function with some passwords
passwords = [
    "Password123!",       # Valid password
    "password123",        # Missing uppercase and special character
    "PASSWORD123",        # Missing lowercase and special character
    "Password!",          # Missing digit
    "Pass123!",           # Less than 8 characters
    "StrongPass1!"        # Valid password
]

for password in passwords:
    if validate_password(password):
        print(f"{password} is a valid password.")
    else:
        print(f"{password} is not a valid password.")
