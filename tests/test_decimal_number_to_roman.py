from unittest import TestCase
from decimal_number_to_roman import decimal_number_to_roman


class TestDecimalNumberToRoman(TestCase):
    def test1(self):
        self.assertEqual('IX', decimal_number_to_roman(9))

    def test2(self):
        self.assertEqual('III', decimal_number_to_roman(3))

    def test3(self):
        self.assertEqual('MCMLXXXIV', decimal_number_to_roman(1984))

    def test4(self):
        self.assertEqual('MMM', decimal_number_to_roman(3000))

    def test5(self):
        self.assertEqual('LXXXVIII', decimal_number_to_roman(88))

    def test6(self):
        self.assertEqual('XXXVI', decimal_number_to_roman(36))

    def test7(self):
        self.assertEqual('XCIII', decimal_number_to_roman(93))
