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

        