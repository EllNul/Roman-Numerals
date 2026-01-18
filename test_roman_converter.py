import unittest
from roman_converter import int_to_roman, roman_to_int

class TestRomanConverter(unittest.TestCase):

    # -----------------------------
    # Tests: int → Roman
    # -----------------------------
    def test_int_to_roman_basic(self):
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(9), "IX")
        self.assertEqual(int_to_roman(58), "LVIII")
        self.assertEqual(int_to_roman(1994), "MCMXCIV")

    # -----------------------------
    # Tests: Roman → int
    # -----------------------------
    def test_roman_to_int_basic(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("LVIII"), 58)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)

    # -----------------------------
    # Tests: invalid integers
    # -----------------------------
    def test_invalid_integers(self):
        with self.assertRaises(Exception):
            int_to_roman(0)

        with self.assertRaises(Exception):
            int_to_roman(4000)

        with self.assertRaises(Exception):
            int_to_roman("hello")

    # -----------------------------
    # Tests: invalid Roman numerals
    # -----------------------------
    def test_invalid_roman_strings(self):
        with self.assertRaises(Exception):
            roman_to_int("ABC")

        with self.assertRaises(Exception):
            roman_to_int("IIV")

        with self.assertRaises(Exception):
            roman_to_int("")

        with self.assertRaises(Exception):
            roman_to_int(123)


if __name__ == "__main__":
    unittest.main()