import unittest
from unittest import TestCase
from counting_strings import count_strings_frequency


class Test(TestCase):
    def test_count_strings_frequencies(self):
        self.assertEqual(count_strings_frequency("semicolon"),
                         {'s': 1, 'e': 1, 'm': 1, 'i': 1, 'c': 1, 'o': 2, 'l': 1, 'n': 1})


if __name__ == '__main__':
    unittest.main()
