import unittest
from main import check_age

class TestMain(unittest.TestCase):
    def test_check_age(self):
        self.assertEqual(check_age(20), 'You are an adult')
        self.assertEqual(check_age(16), 'You are a teenager')

if __name__ == '__main__':
    unittest.main()
