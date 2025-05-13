import unittest
from app import check_password_strength

class TestPasswordStrength(unittest.TestCase):

    def test_strong_password(self):
        self.assertTrue(check_password_strength("Abc123!@#"))

    def test_short_password(self):
        self.assertFalse(check_password_strength("Ab1!"))

    def test_missing_number(self):
        self.assertFalse(check_password_strength("Abcdefg!"))

    def test_missing_uppercase(self):
        self.assertFalse(check_password_strength("abc123!@#"))

    def test_missing_special(self):
        self.assertFalse(check_password_strength("Abc12345"))

if __name__ == '__main__':
    unittest.main()
