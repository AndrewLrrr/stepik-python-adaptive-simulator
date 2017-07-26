from unittest import TestCase
from base_rle_decode import decode_rle


class TestRleDecode(TestCase):
    def test1(self):
        self.assertEqual('aaabccccCCaB', decode_rle('3ab4c2CaB'))

    def test2(self):
        self.assertEqual('aaabcccccabbbbbbb', decode_rle('3ab5ca7b'))

    def test3(self):
        self.assertEqual('aaaaaaaaa', decode_rle('9a'))

    def test4(self):
        self.assertEqual('baaaaaaaaabb', decode_rle('b9a2b'))

    def test5(self):
        self.assertEqual('AAABCCB', decode_rle('3AB2CB'))

    def test6(self):
        self.assertEqual('aaabccb', decode_rle('3ab2cb'))

    def test7(self):
        self.assertEqual('', decode_rle(''))

    def test8(self):
        self.assertEqual('a', decode_rle('a'))

    def test9(self):
        self.assertEqual('baaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbb', decode_rle('b11a22b'))
