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