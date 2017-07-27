from unittest import TestCase
from length_statistic import length_statistic
from collections import OrderedDict


class TestLengthStatistic(TestCase):
    def test1(self):
        expected = OrderedDict(sorted({
                      1: 1,
                      2: 2,
                      3: 4,
                      4: 4
                    }.items()))
        self.assertEquals(expected, length_statistic('a bb a, ccc cd. Abcd bb! CDE AAAA BBBB abcd'))

    def test2(self):
        expected = OrderedDict(sorted({
                      2: 2,
                      4: 2,
                      5: 1,
                      6: 2,
                      8: 1,
                      9: 2
                    }.items()))
        self.assertEquals(expected, length_statistic('Beautiful is better than ugly. Explicit is better than implicit.'))

    def test3(self):
        expected = OrderedDict(sorted({
                      2: 2,
                      4: 2,
                      5: 1,
                      6: 2,
                      8: 1,
                      9: 2
                    }.items()))

        self.assertEquals(expected, length_statistic('Beautiful   is   better than ugly. Explicit is    better than    implicit.'))

