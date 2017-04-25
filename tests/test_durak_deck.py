from unittest import TestCase
from durak_deck import get_winner


class TestDurakDeck(TestCase):
    def test_can_get_first_winner(self):
        self.assertEqual('First', get_winner('AH JH', 'D'))

    def test_can_get_second_winner(self):
        self.assertEqual('First', get_winner('AH JH', 'S'))

    def test_can_get_draw(self):
        self.assertEqual('Error', get_winner('7C 10H', 'S'))