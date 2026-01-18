import unittest

from roman_converter import num_to_roman,roman_to_num

class TestRomanCoverter(unittest.TestCase):

    def test_num_to_roman_basic(self):
        self.asserEqual(num_to_roman(73), "LXXIII")

if __name__ == "__Main__":
    unittest.main()