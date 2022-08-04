import unittest
from src.fizzbizz import *

class TestFizzbizz(unittest.TestCase):

    def test_fizz(self):
        number = fizzbizz(3)
        self.assertEqual("Fizz", number)

    def test_bizz(self):
        number = fizzbizz(10)
        self.assertEqual("Bizz", number)

    def test_fizzbizz(self):
        number = fizzbizz(15)
        self.assertEqual("Fizzbizz", number)

    def test_error(self):
        number = fizzbizz(4)
        self.assertEqual(str(number), number)