import unittest
from roman_converter import int_to_roman, roman_to_int

class TestRomanConverter(unittest.TestCase):

    def test_int_to_roman(self):
        self.assertEqual(int_to_roman(84), "LXXXIV")

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("MMMDCCXCII"), 3792)


if __name__ == "__main__":
     unittest.main()
