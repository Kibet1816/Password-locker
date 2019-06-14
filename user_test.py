import unittest
from password import User

class TestUser(unittest.TestCase):
    """
    Class for testing the behaviour of the user class
    """
    def setUp(self):
        """
        Setup method that defines instructions
        """
        self.new_user = User("Denis","Kibet","soccer5240")

    def test_init(self):
        """
        Test for correct initialization
        """
        self.assertEqual(self.new_user.first_name,"Denis")
        self.assertEqual(self.new_user.last_name,"Kibet")
        self.assertEqual(self.new_user.password,"soccer5240")


if __name__ == '__main__':
    unittest.main()
