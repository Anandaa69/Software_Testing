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

    def test_give_neg_3(self):
        num = -3
        result = fizzbuzz(num)
        self.assertEqual(result, "Fizz")

    def test_give_10(self):
        num = 10
        result = fizzbuzz(num)
        self.assertEqual(result, "Buzz")

    def test_give_30(self):
        num = 30
        result = fizzbuzz(num)
        self.assertEqual(result, "FizzBuzz")

    def test_give_100(self):
        num = 100
        result = fizzbuzz(num)
        self.assertEqual(result, "Buzz")

    def test_give_101(self):
        num = 101
        result = fizzbuzz(num)
        self.assertEqual(result, "...")

    def test_give_large_number(self):
        num = 99999999
        result = fizzbuzz(num)
        self.assertEqual(result, "Fizz")

    def test_give_large_buzz(self):
        num = 100000
        result = fizzbuzz(num)
        self.assertEqual(result, "Buzz")
