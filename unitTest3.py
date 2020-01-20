import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual('a'*4, 'aaaa')


if __name__ == '__main__':
    unittest.main()
