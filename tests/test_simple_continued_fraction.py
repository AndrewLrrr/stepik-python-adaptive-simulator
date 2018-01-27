from unittest import TestCase
from simple_continued_fraction import simple_continued_fraction


class TestSimpleContinuedFraction(TestCase):
    def test1(self):
        self.assertEqual([7, 1, 29], simple_continued_fraction('239/30'))

    def test2(self):
        self.assertEqual([4, 2, 6, 7], simple_continued_fraction('415/93'))

    def test3(self):
        self.assertEqual([0, 46, 2], simple_continued_fraction('2/93'))

    def test4(self):
        self.assertEqual([0], simple_continued_fraction('0/5'))
