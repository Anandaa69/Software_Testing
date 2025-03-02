from main_code.caesar_cipher_HR import caesarCipher
import unittest

class CaesarCipherTest(unittest.TestCase):

    def test_give_abc_k1(self):
        s = "abc"
        k = 1
        result = caesarCipher(s, k)
        self.assertEqual(result, "bcd")

    def test_give_xyz_k3(self):
        s = "xyz"
        k = 3
        result = caesarCipher(s, k)
        self.assertEqual(result, "abc")

    def test_give_Hello_World_k5(self):
        s = "Hello, World!"
        k = 5
        result = caesarCipher(s, k)
        self.assertEqual(result, "Mjqqt, Btwqi!")

    def test_give_special_cha(self):
        s = "1234!@#"
        k = 500
        result = caesarCipher(s, k)
        self.assertEqual(result, "1234!@#")

    def test_give_python3_9(self):
        s = "Python 3.9"
        k = 3
        result = caesarCipher(s, k)
        self.assertEqual(result, "Sbwkrq 3.9")

    def test_give_aZz(self):
        s = "aZz"
        k = 2
        result = caesarCipher(s, k)
        self.assertEqual(result, "cBb")