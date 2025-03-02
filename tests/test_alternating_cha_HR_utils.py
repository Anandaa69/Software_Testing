from main_code.alternating_cha_HR import alternatingCharacters
import unittest

class AlternatingCharactersTest(unittest.TestCase):

    def test_give_AAAA(self):
        s = 'AAAA'
        result = alternatingCharacters(s)
        self.assertEqual(result, 'A')

    def test_give_BBBB(self):
        s = 'BBBB'
        result = alternatingCharacters(s)
        self.assertEqual(result, 'A')