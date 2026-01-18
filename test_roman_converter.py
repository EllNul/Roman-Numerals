import unittest

from roman_converter import int_to_roman, roman_to_int

class TestRomanConverter(unittest.TestCase):

    def test_int_to_roman_(self):
        self.assertEqual(int_to_roman(73), "LXXIII")

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("MMMDCXXV"), 3625)

if __name__ == "__main__":
    unittest.main()