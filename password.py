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
        Method to save user login details
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
        Method to save credentials
        """
        Credentials.credentials_list.append(self)