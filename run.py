from user import User
from credentials import Credential

def create_user(username, password, email):
    '''
    function to create a new user.
    Args:
       username: New user username.
        password : New user password.
        email : New user email.
    '''
    new_user = User(username, password, email)
    return new_user

def save_user(user):
    '''
    function to save user
    '''
    User.save_user()

def delete_user(user):
    '''
    function to delete a user
    '''
    User.delete_user(user)

def find_user(username):
    '''
    method that takes in a name and returns a username that matches that name.
    '''
    return User.find_by_username(username)

def check_existing_user(email):
    '''
    method that checks if a user exists from the user list.
    '''
    return User.user_exists(email)

def create_user_info(social_media, account, password):
    '''
    function to delete user credentials
    '''
    new_user_info = Credential(social_media, account, password)
    return new_user_info

def save_user_info(info):
    '''
    function to save user info
    '''
    return Credential.save_credential(info)

def display_users_info(username):
    '''
    function to display user info
    '''
    return Credential.display_credential()


def display_all_users():
    '''
    function to display all users
    '''
    return User.display_users()


