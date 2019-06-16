import string,random
class User:
    """
    Class to define login details for the user in the application
    """
    user_list = []

    def __init__(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        """
        Function to save user login details
        """
        User.user_list.append(self)


class Credentials:
    """
    Class to define credentials for the different accounts
    """
    credentials_list = []

    def __init__(self,account_name,username,password):

        self.account_name = account_name
        self.username = username
        self.password = password

    def save_credentials(self):
        """
        Function to save credentials
        """
        Credentials.credentials_list.append(self)

    @classmethod
    def find_by_name(cls,name):
        """
        Function that takes a the name of an account and returns the account object
        """
        for account in cls.credentials_list:
            if account.account_name == name:
                return account

    @classmethod
    def generate_password(num):
        """
        Function to generate password
        """
        password = ''

        for x in range(num):
            x = random.randint(0,99)
            password += string.printable[x]
        return password

    @classmethod
    def display_credentials(cls):
        """
        Function to display accounts and their credentials
        """
        return cls.credentials_list

    def delete_credentials(self):
        """
        Function to delete account credentials
        """
        Credentials.credentials_list.remove(self)
