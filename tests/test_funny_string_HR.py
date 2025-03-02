from main_code.funny_string_HR import funnyString
import unittest

class FunnyStringTest(unittest.TestCase):

    def test_give_a(self):
        s = "a"
        result = funnyString(s)
        self.assertEqual(result, "Funny") 

    def test_give_abc(self):
        s = "abc"
        result = funnyString(s)
        self.assertEqual(result, "Funny")

    def test_give_acb(self):
        s = "acb"
        result = funnyString(s)
        self.assertEqual(result, "Not Funny")

    def test_give_aa(self):
        s = "aa"
        result = funnyString(s)
        self.assertEqual(result, "Funny")

    def test_give_abcd(self):
        s = "abcd"
        result = funnyString(s)
        self.assertEqual(result, "Funny")

    def test_give_abba(self):
        s = "abba"
        result = funnyString(s)
        self.assertEqual(result, "Funny")

    def test_give_aegk(self):
        s = "aegk"
        result = funnyString(s)
        self.assertEqual(result, "Funny")

    def test_give_abacabadabacaba(self):
        s = "abacabadabacaba"
        result = funnyString(s)
        self.assertEqual(result, "Funny")

    def test_give_alphabet(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        result = funnyString(s)
        self.assertEqual(result, "Funny")

    def test_give_xyzyx(self):
        s = "xyzyx"
        result = funnyString(s)
        self.assertEqual(result, "Funny")