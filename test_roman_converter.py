
import unittest

from roman_converter import num_to_roman, roman_to_num

class TestRomanConverter(unittest.TestCase):

    def test_num_to_roman(self):
        self.assertEqual(num_to_roman(52), "LII")

if __name__ == '__main__':
    unittest.main()