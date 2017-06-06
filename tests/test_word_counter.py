from unittest import TestCase
from word_counter import word_counter


class TestWordCounter(TestCase):
    def test1(self):
        string = 'a aa abC aa ac abc bcd a'
        expected = {
            'bcd': 1,
            'ac': 1,
            'aa': 2,
            'a': 2,
            'abc': 2
        }
        self.assertEquals(expected, word_counter(string))

    def test2(self):
        string = 'a aa aa aaa aaa aaa aaaa aaaa aaaa aaaa'
        expected = {
            'a': 1,
            'aa': 2,
            'aaa': 3,
            'aaaa': 4,
        }
        self.assertEquals(expected, word_counter(string))

    def test3(self):
        string = 'A aa AA aaa AAA aAa aaaA Aaaa aAaa aAaa'
        expected = {
            'a': 1,
            'aa': 2,
            'aaa': 3,
            'aaaa': 4,
        }
        self.assertEquals(expected, word_counter(string))

    def test4(self):
        string = ''
        expected = {}
        self.assertEquals(expected, word_counter(string))

