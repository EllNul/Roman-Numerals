import unittest

from roman_converter import num_to_roman,roman_to_num

class TestRomanCoverter(unittest.TestCase):

    def test_num_to_roman_basic(self):
        self.assertEqual(num_to_roman(73), "LXXIII")

    def test_roman_to_num_basic(self):
        self.assertEqual(roman_to_num("DLXI"), 561)

if __name__ == "__Main__":
    unittest.main()