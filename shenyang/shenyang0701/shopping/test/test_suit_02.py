import unittest


class MyTestCase(unittest.TestCase):

    def test_something(self):
        print("02-01")
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
