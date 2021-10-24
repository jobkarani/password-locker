class User:
    """
    class that generates new instances of user
    """
    user_list=[]

    def __init__(self,full_name,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            full_name: New user full name.
            username: New user username.
            password : New user password.
        '''

        self.full_name=full_name
        self.username=username
        self.password=password

        

