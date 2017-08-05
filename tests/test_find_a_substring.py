from unittest import TestCase
from find_a_substring import find_a_substring


class TestFindASubstring(TestCase):
    def test1(self):
        text = 'abacabadaba'
        string = 'aba'
        self.assertEquals([0, 4, 8], find_a_substring(string, text))

    def test2(self):
        text = 'aaaa'
        string = 'aa'
        self.assertEquals([0, 1, 2], find_a_substring(string, text))

    def test3(self):
        text = 'abc'
        string = 'd'
        self.assertEquals([], find_a_substring(string, text))