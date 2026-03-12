import unittest
from auth.auth_service import register_user

class TestRegister(unittest.TestCase):

    def test_valid_registration(self):
        result = register_user("jayashree", "1234")
        self.assertTrue(result)

    def test_empty_username(self):
        result = register_user("", "1234")
        self.assertFalse(result)