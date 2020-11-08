import unittest
from unittest import mock
from unittest.mock import patch
import sys
import os
sys.path.insert(1, os.getcwd())
import app as wholeApp
from app import app
from app import socketio

class mocked(unittest.TestCase):
    def test_connect(self):
        client = socketio.test_client(app)
        res = client.get_received()
        self.assertEqual(res[0]["args"][0]["message"], "Server is up!")

    def test_home_page(self):
        user = app.test_client(self)
        response = user.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()