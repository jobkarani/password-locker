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


if __name__ == '__main__':
    unittest.main()
