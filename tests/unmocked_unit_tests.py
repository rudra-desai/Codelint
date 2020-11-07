import unittest
import sys
import os
sys.path.insert(1, os.getcwd())

class unmocked(unittest.TestCase):
    def test_print(self):
        print("This works")

if __name__ == '__main__':
    unittest.main()