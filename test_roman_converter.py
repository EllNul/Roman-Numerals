import unittest

from roman_converter import int_to_roman, roman_to_int, RomanConversionError

class TestRomanConverter(unittest.TestCase):

    def test_int_to_roman_(self):
        self.assertEqual(int_to_roman(73), "LXXIII")

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("MMMDCXXV"), 3625)

    def test_invalid_integers(self):
        with self.assertRaises(RomanConversionError):
            int_to_roman(4000)

    def test_invalid_roman(self):
        with self.assertRaises(RomanConversionError):
            roman_to_int("ABC")

if __name__ == "__main__":
    unittest.main()
