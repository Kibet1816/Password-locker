import unittest
from password import User

class TestUser(unittest.TestCase):
    """
    Class for testing the behaviour of the user class
    """
    def setUp(self):
        self.new_user = User("Denis","Kibet","soccer5240")