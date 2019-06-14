import unittest
from password import Credentials

class TestCredentials(unittest.TestCase):
    """
    Class to test behaviour of the credentials class
    """
    def setUp(self):
        """
        Setup method that defines instructions
        """
        self.new_credentials = Credentials("Github","Kibet1816","@#soccerkibe1816")

    def test_init(self):
        """
        Test for correct initialization
        """
        self.assertEqual(self.new_credentials.account_name,"Github")
        self.assertEqual(self.new_credentials.username,"Kibet1816")
        self.assertEqual(self.new_credentials.password,"@#soccerkibe1816")

    def test_save_credentials(self):
        """
        Test to check whether app saves account credentials
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
    unittest.main()