import unittest
from user import User

class TestUser(unittest.TestClass):
    """
    Test class that defines test case for the user class behaviour.
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("Job","ayub09877") #create user object

        if __name__='__main__':
            unittest.main()