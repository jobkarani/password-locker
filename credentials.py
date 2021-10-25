import random
import string

class Credential:

    credential_list = []

    def __init__(self, social_media, account, password):
        '''
        function helps us define properties of our objects
        '''
        self.social_media = social_media
        self.account = account
        self.password = password 

    def save_credential(self):
        '''
        function to save user credentials
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        function to delete user credentials
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def display_credential(cls):
        '''
        function to display all user credentials
        '''
        return cls.credential_list

    def generate_password(length = 6, password = string.digits + string.letters)
    '''
    function to generate a random password
    '''
    generated_password = ''.join(random.choice(password) for i in range(length))
    return generated_password