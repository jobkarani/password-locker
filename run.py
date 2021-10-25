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

def 