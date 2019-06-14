import unittest
from password import Credentials

class TestCredentials(unittest.TestCase):
    """
    Class to test behaviour of the credentials class
    """
    def setUp(self):
        self.new_credentials = Credentials("Github","Kibet1816","@#soccerkibe1816")