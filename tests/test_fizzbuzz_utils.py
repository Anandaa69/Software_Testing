from main_code.fizzbuzz import fizzbuzz
import unittest

class FizzBuzzNumberTest(unittest.TestCase):

    def test_give_3(self):
        num = 3
        result = fizzbuzz(num)
        self.assertEqual(result, "Fizz")
