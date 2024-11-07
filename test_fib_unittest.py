import unittest

from fib import fibonacci_iterative


class TestStringMethods(unittest.TestCase):

    def test_fib_9_is_34(self):
        self.assertEqual(fibonacci_iterative(9), 34)

    def test_split(self):
        with self.assertRaises(ValueError):
            fibonacci_iterative(-1)


if __name__ == '__main__':
    unittest.main()
