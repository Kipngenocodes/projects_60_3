import unittest
from password_unitest import validate_password  

class TestPasswordValidation(unittest.TestCase):

    def test_valid_passwords(self):
        self.assertTrue(validate_password("Password123!"))
        self.assertTrue(validate_password("StrongPass1@"))
        self.assertTrue(validate_password("Another#Pass2"))
        self.assertTrue(validate_password("Valid$Password3"))

    def test_invalid_passwords(self):
        self.assertFalse(validate_password("password123!"))     # Missing uppercase
        self.assertFalse(validate_password("PASSWORD123!"))     # Missing lowercase
        self.assertFalse(validate_password("Password!@"))       # Missing digit
        self.assertFalse(validate_password("Password123"))      # Missing special character
        self.assertFalse(validate_password("Pass1!"))           # Less than 8 characters
        self.assertFalse(validate_password(""))                 # Empty password

# Run the tests
if __name__ == "__main__":
    unittest.main()
