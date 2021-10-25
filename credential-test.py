import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    '''
    test class that defines the test cases for the credential class behaviour.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Instagram", "ayub", "ayub1234") #create credential object

    def test_init(self):
        '''
        tests if the objects are being initialized properly.
        '''
        self.assertEqual(self.new_credential.social_media, "Instagram")
        self.assertEqual(self.new_credential.account, "ayub")
        self.assertEqual(self.new_credential.password, "ayub1234")
        

    def test_save_credential(self):
        '''
        test case that checks if a credential is saved properly.
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):
        '''
        tearDown function that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    def test_save_multiple_credential(self):
        '''
        test case to check whether we can save multiple credentials
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Tiktok", "sly", "sly1234")
        test_credential.save_credential()

    def test_delete_credential(self):
        '''
        test case that checks if a credential can be removed.
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Tiktok", "sly", "sly1234")
        test_credential.save_credential()

        test_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)



if __name__ == '__main__':
    unittest.main()
