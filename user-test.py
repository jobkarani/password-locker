import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test case for the user class behaviour.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Job", "ayub09877", "jk@user.com") #create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username, "Job")
        self.assertEqual(self.new_user.password, "ayub09877")
        self.assertEqual(self.new_user.email, "jk@user.com")

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
        test_user = User("Jane", "jn8789", "wk@user.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        to test if we can remove a user from our user list.
        '''
        self.new_user.save_user()
        test_user = User("Jane", "jn8789", "wk@user.com")
        test_user.save_user()

        self.new_user.delete_user() #deleting a user object
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_username(self):
        '''
        to check if we can find a user by their username
        '''
        self.new_user.save_user()
        test_user = User("Jane", "jn8789", "wk@user.com")
        test_user.save_user()

        found_user = User.find_by_username("Jane")
        self.assertEqual(found_user.email, test_user.email)

    def test_user_exists(self):
        '''
        test to see if we can return a boolean if we cant find a user.
        '''
        self.new_user.save_user()
        test_user = User("Jane", "jn8789", "wk@user.com")
        test_user.save_user()

        user_exists = User.user_exists("wk@user.com")
        self.assertTrue(user_exists)


    def test_display_all_users(self):
        '''
        method that returns a list of all users saved.
        '''
        self.assertEqual(User.display_users(), User.user_list)



if __name__ == '__main__':
    unittest.main()