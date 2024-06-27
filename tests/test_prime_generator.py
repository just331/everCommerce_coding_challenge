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
        self.assertTrue(is_prime(7919))
        self.assertFalse(is_prime(7920))

class TestPrimeGenerator(unittest.TestCase):
    def test_prime_generator(self):
        # general case for finding primes in range of nums
        self.assertEqual(prime_generator(1, 10), [2,3,5,7])