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
    
    def test_empty_string(self):
        s = ""
        k = 5
        result = caesarCipher(s, k)
        self.assertEqual(result, "")

    def test_no_shift(self):
        s = "abcdef"
        k = 0
        result = caesarCipher(s, k)
        self.assertEqual(result, "abcdef")

    def test_large_shift_value(self):
        s = "abc"
        k = 26
        result = caesarCipher(s, k)
        self.assertEqual(result, "abc")

    def test_wrap_around_upper_case(self):
        s = "XYZ"
        k = 5
        result = caesarCipher(s, k)
        self.assertEqual(result, "CDE")

    def test_wrap_around_lower_case(self):
        s = "xyz"
        k = 5
        result = caesarCipher(s, k)
        self.assertEqual(result, "cde")

    def test_mixed_case_and_special_characters(self):
        s = "aB1!cD"
        k = 3
        result = caesarCipher(s, k)
        self.assertEqual(result, "dE1!fG")

    def test_large_shift_with_wrapping(self):
        s = "abcXYZ"
        k = 30  # จะเลื่อนมากกว่า 26 ครั้ง
        result = caesarCipher(s, k)
        self.assertEqual(result, "efgBCD")

    def test_upper_case_and_numbers(self):
        s = "HELLO 123"
        k = 1
        result = caesarCipher(s, k)
        self.assertEqual(result, "IFMMP 123")

    def test_mixed_string_with_punctuation(self):
        s = "Hello, World!123"
        k = 2
        result = caesarCipher(s, k)
        self.assertEqual(result, "Jgnnq, Yqtnf!123")
        
