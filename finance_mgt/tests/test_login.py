import unittest
from auth.auth_service import login_user

class TestLogin(unittest.TestCase):

    def test_login_success(self):
        result = login_user("jayashree","1234")
        self.assertTrue(result)

    def test_login_fail(self):
        result = login_user("jayashree","wrong")
        self.assertFalse(result)