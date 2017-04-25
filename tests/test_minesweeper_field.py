from unittest import TestCase
from minesweeper_field import MineField


class TestMineField(TestCase):
    def test_field_4_4(self):
        field = [
            '..*.',
            '**..',
            '..*.',
            '....'
        ]

        expected = [
            '23*1',
            '**32',
            '23*1',
            '0111'
        ]

        mine_field = MineField(4, 4, [list(row) for row in field])

        self.assertEqual(expected, [row for row in mine_field])

    def test_field_6_4(self):
        field = [
            '.*..',
            '**.*',
            '..*.',
            '..**',
            '**.*',
            '.***',
        ]

        expected = [
            '3*31',
            '**4*',
            '24*4',
            '24**',
            '**7*',
            '3***',
        ]

        mine_field = MineField(6, 4, [list(row) for row in field])

        self.assertEqual(expected, [row for row in mine_field])

    def test_field_4_6(self):
        field = [
            '.*....',
            '**.*..',
            '..*...',
            '..***.',
        ]

        expected = [
            '3*3110',
            '**4*10',
            '24*531',
            '02***1',
        ]

        mine_field = MineField(4, 6, [list(row) for row in field])

        self.assertEqual(expected, [row for row in mine_field])