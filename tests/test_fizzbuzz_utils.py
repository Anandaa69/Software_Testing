from main_code.fizzbuzz import fizzbuzz
import unittest

class FizzBuzzNumberTest(unittest.TestCase):

    def test_give_3(self):
        num = 3
        result = fizzbuzz(num)
        self.assertEqual(result, "Fizz")

    def test_give_5(self):
        num = 5
        result = fizzbuzz(num)
        self.assertEqual(result, "Buzz")

    def test_give_15(self):
        num = 15
        result = fizzbuzz(num)
        self.assertEqual(result, "FizzBuzz")

    def test_give_4(self):
        num = 4
        result = fizzbuzz(num)
        self.assertEqual(result, "...")
