import unittest
from app.models import User


class TestUser(unittest.TestCase):
    """
    Test class to test the behaviour of the User class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.new_user = User(
            username='bolt254',
            name='dev seme',
            email='ian.ochenge@student.moringaschool.com',
            password='qwerty'
        )

    def test_no_access_password(self):
        """
        Test to check if the password is not accessible
        """
        with self.assertRaises(AttributeError):
            self.new_user.password