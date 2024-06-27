import unittest
from utils import is_prime
from prime_generator import prime_generator


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(7900))
        self.assertTrue(is_prime(7919))
        self.assertFalse(is_prime(7920))


class TestPrimeGenerator(unittest.TestCase):
    def test_prime_generator(self):
        # general case for finding primes in range of nums
        self.assertEqual(prime_generator(1, 10), [2, 3, 5, 7])
        # inverse range general case
        self.assertEqual(prime_generator(10, 1), [2, 3, 5, 7])
        # case for finding primes in range of 7900 - 7920
        self.assertEqual(prime_generator(7900, 7920), [7901, 7907, 7919])
        # inverse range case for above range
        self.assertEqual(prime_generator(7900, 7920), [7901, 7907, 7919])
        # primes between 1 - 100
        self.assertEqual(prime_generator(1, 100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                                                   41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
