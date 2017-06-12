from unittest import TestCase
from fraction_of_maximum_score import fraction_of_maximum_score


class TestFractionOfMaximumScore(TestCase):
    @staticmethod
    def format(number):
        return '{0:.2f}'.format(number)

    def test1(self):
        scores = ['F', 'B', 'A', 'A', 'B', 'C', 'A', 'D']
        self.assertEqual('0.38', self.format(fraction_of_maximum_score(scores)))

    def test2(self):
        scores = ['B', 'C', 'B']
        self.assertEqual('0.00', self.format(fraction_of_maximum_score(scores)))

    def test3(self):
        scores = ['A', 'A', 'A']
        self.assertEqual('1.00', self.format(fraction_of_maximum_score(scores)))

    def test4(self):
        scores = ['A', 'D']
        self.assertEqual('0.50', self.format(fraction_of_maximum_score(scores)))
