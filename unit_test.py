import unittest

class SimpleTest(unittest.TestCase):
    # Return True or false
    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()