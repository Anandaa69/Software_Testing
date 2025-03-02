from main_code.two_cha_HR import alternate
import unittest

class AlternatingCharactersTest(unittest.TestCase):

    def test_single_char(self):
        s = "a"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_two_different_chars(self):
        s = "ab"
        result = alternate(s)
        self.assertEqual(result, 2)

    def test_two_same_chars(self):
        s = "aa"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_three_chars_with_alternation(self):
        s = "aba"
        result = alternate(s)
        self.assertEqual(result, 3)

    def test_three_chars_without_alternation(self):
        s = "aaa"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_four_chars_with_alternation(self):
        s = "abab"
        result = alternate(s)
        self.assertEqual(result, 4)

    def test_four_chars_without_alternation(self):
        s = "aabb"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_multiple_chars_with_alternation(self):
        s = "abcabc"
        result = alternate(s)
        self.assertEqual(result, 4)

    def test_multiple_chars_without_alternation(self):
        s = "aaabbb"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_empty_string(self):
        s = ""
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_long_string_with_alternation(self):
        s = "ababababab"
        result = alternate(s)
        self.assertEqual(result, 10)

    def test_long_string_without_alternation(self):
        s = "aaabbbaaabbb"
        result = alternate(s)
        self.assertEqual(result, 0)

