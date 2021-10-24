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
        self.new_user = User("Job", "ayub09877") #create user object

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

    def tearDown(self):
        '''
        tearDown function that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        to check if we save multiple users.
        '''
        self.new_user.save_user()
        test_user = User("Jane", "jn8789")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        to test if we can remove a user from our user list.
        '''
        self.new_user.save_user()
        test_user = User("Jane", "jn8789")
        test_user.save_user()

        self.new_user.delete_user() #deleting a user object
        self.assertEqual(len(User.user_list), 1)




if __name__ == '__main__':
    unittest.main()