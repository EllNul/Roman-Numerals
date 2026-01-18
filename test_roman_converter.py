import unittest

from roman_converter import int_to_roman,roman_to_int

class TestRomanCoverter(unittest.TestCase):

    def test_int_to_roman_basic(self):
        self.assertEqual(int_to_roman(73),"LXXIII")

    def test_invalid_number(self):
        with self.assertRaises(Exception):
            int_to_roman(0)

if __name__ == "__Main__":
    unittest.main()