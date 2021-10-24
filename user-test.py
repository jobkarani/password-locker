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

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user,"Job")
        self.assertEqual(self.new_user,"ayub09877")




        if __name__='__main__':
            unittest.main()