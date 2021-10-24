import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test class that defines test case for the user class behaviour.
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Job","ayub09877") #create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username, "Job")
        self.assertEqual(self.new_user.password, "ayub09877")

    def test_save_user(self):
        '''
        test case that tests if the user is being saved properly
        '''
        self.new_user.save_user()

        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()