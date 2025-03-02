from main_code.alternating_cha_HR import alternatingCharacters
import unittest

class AlternatingCharactersTest(unittest.TestCase):

    def test_give_AAAA(self):
        s = 'AAAA'
        result = alternatingCharacters(s)
        self.assertEqual(result, 3)

    def test_give_BBBB(self):
        s = 'BBBB'
        result = alternatingCharacters(s)
        self.assertEqual(result, 3)

    def test_give_ABABABAB(self):
        s = 'ABABABAB'
        result = alternatingCharacters(s)
        self.assertEqual(result, 0)

    def test_give_AAABBB(self):
        s = "AAABBB"
        result = alternatingCharacters(s)
        self.assertEqual(result, 4)

    def test_give_BABABA(self):
        s = "BABABA"
        result = alternatingCharacters(s)
        self.assertEqual(result, 0)
