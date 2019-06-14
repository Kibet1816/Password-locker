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

