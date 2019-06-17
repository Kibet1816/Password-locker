#!/usr/bin/env python3.6
from password import User
from password import Credentials

def create_login(firstname,lastname,password):
    """
    Function to create a new login
    """
    new_user = User(firstname,lastname,password)
    return new_user

def add_account(accname,username,password):
    """
    Function to add a new account and its credentials
    """
    new_credentials = Credentials(accname,username,password)
    return new_credentials

def save_user(user):
    """
    Function to save user login details
    """
    user.save_user()

def save_credentials(account):
    """
    Function to save account details
    """
    account.save_credentials()

def generate_password():
    """
    Function to create a password automatically
    """
    password = Credentials.generate_password()
    return password


def display_credentials():
    """
    Function to display account and credentials
    """
    return Credentials.credentials_list

def del_account(credential):
    """
    Function to delete an account
    """
    credential.delete_credentials()

def main():
    print("Welcome to password locker :)")
    print("What\'s your name?")
    name = input()

    while True:

        print(f"Hello {name}. Please use the short code :li to login")
    
        short_code = input().lower()

        if short_code == 'li':

            print('Login')
            print('*'*15)

            print("First name....")
            firstname = input()

            print("Last name....")
            lastname = input()

            print("Password....")
            password = input()

            save_user(create_login(firstname,lastname,password))
            print('\n')
            
            while True:

                print(f"Welcome {firstname}.Use the following commands: ca-Create a new account :da - Display all accounts :dl - Delete an account ")
                print('\n')
                shorter_code = input().lower()

                if shorter_code == 'ca':
                    print("Save new account credentials")
                    print('^'*10)

                    print('Name of the account.....')
                    accname = input()

                    print('Username.....')
                    username = input()
                     
                    print('Password....')
                    password = input()
                            

                    save_credentials(add_account(accname,username,password))
                    print('\n')
                    print(f'New account \'{accname}\' created')
                        

                elif shorter_code == 'da':
                    if display_credentials():
                        for credential in display_credentials():
                            print(f" Account name >> {credential.account_name}  \n Username >> {credential.username} \n password >> {credential.password} \n")
                            break
                elif shorter_code == 'dl':
                    pass


        else:
            print('\n')
            print('#'*8)
            print("Sorry :( .The command does not exist.Try again with :li")
            print('#'*8)
            print('\n')

if __name__ == '__main__':
    main()