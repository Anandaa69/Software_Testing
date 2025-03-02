from main_code.number import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_all_non_primes(self):
        prime_list = [4, 6, 8]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_mixed_primes_and_non_primes(self):
        prime_list = [2, 4, 3, 6, 5]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_large_number_is_non_prime(self):
        prime_list = [7899787232321]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_large_numbers_is_prime(self):
        prime_list = [879879874125, 123123454535322, 213358039485309485343]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
