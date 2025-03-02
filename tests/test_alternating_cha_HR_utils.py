from main_code.alternating_cha_HR import alternatingCharacters
import unittest

class AlternatingCharactersTest(unittest.TestCase):

    def test_single_char(self):
        s = "A"
        result = alternatingCharacters(s)
        self.assertEqual(result, 0)

    def test_long_alternating_string(self):
        s = "ABABABABABABABAB"
        result = alternatingCharacters(s)
        self.assertEqual(result, 0)

    def test_no_alternating(self):
        s = "AAAABBBB"
        result = alternatingCharacters(s)
        self.assertEqual(result, 6)

    def test_no_repeats(self):
        s = "ABCDEF"
        result = alternatingCharacters(s)
        self.assertEqual(result, 0)

    def test_even_length_alternating(self):
        s = "ABABAB"
        result = alternatingCharacters(s)
        self.assertEqual(result, 0)

    def test_single_change_needed(self):
        s = "AABABAB"
        result = alternatingCharacters(s)
        self.assertEqual(result, 1)

    def test_long_repeated_characters(self):
        s = "AAAAAAAAAAAAAAAAAAAAAA"
        result = alternatingCharacters(s)
        self.assertEqual(result, 21)

    def test_all_different_chars(self):
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = alternatingCharacters(s)
        self.assertEqual(result, 0)

    def test_odd_length_alternating(self):
        s = "ABABABA"
        result = alternatingCharacters(s)
        self.assertEqual(result, 0)

    def test_repeated_chars_in_between(self):
        s = "AABBBBA"
        result = alternatingCharacters(s)
        self.assertEqual(result, 4)
