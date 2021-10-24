class User:
    '''
    class that generates new instances of user
    '''
    user_list = []

    def __init__(self,username,password,email):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: New user username.
            password : New user password.
            email : New user email.
        '''

        self.username = username
        self.password = password
        self.email = email

    def save_user(self):
            '''
            function to add a new user to the user list
            '''
            User.user_list.append(self)  

    def delete_user(self):
        '''
        method deletes a saved user from the user list.
        '''

        User.user_list.remove(self)  

    @classmethod
    def find_by_username(cls, username):
        '''
        method that takes in a name and returns a name that matches that name.
        Args:
            username:name to search for
        Returns:
            user of person that matches the username.
        '''
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def user_exists(cls, email):
        '''
        method that checks if a user exists from the user list.
        Args:
            email:email to search if it exists.
        Returns:
            Boolean: true or false depending if the user exists.
        '''
        for user in cls.user_list:
            if user.email == email:
                return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

        

