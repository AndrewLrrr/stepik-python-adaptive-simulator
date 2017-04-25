from unittest import TestCase
from base_rle_encode import encode_rle


class TestRleEncode(TestCase):
    def test_compress_sting_in_different_registers(self):
        self.assertEqual('3ab4c2CaB', encode_rle('aaabccccCCaB'))

    def test_compress_string_with_long_tail(self):
        self.assertEqual('3ab5ca7b', encode_rle('aaabcccccabbbbbbb'))

    def test_compress_string_of_same_letters(self):
        self.assertEqual('9a', encode_rle('aaaaaaaaa'))

    def test_compress_string_with_contains_same_letters_on_start_and_end(self):
        self.assertEqual('b9a2b', encode_rle('baaaaaaaaabb'))

    def test_compress_sting_in_uppercase(self):
        self.assertEqual('3AB2CB', encode_rle('AAABCCB'))

    def test_compress_sting_in_lower(self):
        self.assertEqual('3ab2cb', encode_rle('aaabccb'))

    def test_compress_empty_string(self):
        self.assertEqual('', encode_rle(''))

    def test_compress_one_char(self):
        self.assertEqual('a', encode_rle('a'))
