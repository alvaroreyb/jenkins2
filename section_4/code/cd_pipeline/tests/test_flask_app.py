#!/usr/bin/python

import sys
import os
sys.path.append(os.environ['WORKSPACE'])
import unittest
import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
 
if __name__ == "__main__":
    unittest.main()
