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

def show_credentials():
    """
    Function to display account and credentials
    """
    return Credentials.display_credentials

def del_account(credential):
    """
    Function to delete an account
    """
    credential.delete_credentials()
