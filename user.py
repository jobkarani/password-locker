class User:
    '''
    class that generates new instances of user
    '''
    user_list = []

    def __init__(self,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: New user username.
            password : New user password.
        '''

        self.username = username
        self.password = password

        def save_user(self):
            '''
            function to add a new user to the user list
            '''

            User.user_list.append(self)

        

