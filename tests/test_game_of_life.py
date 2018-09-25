from unittest import TestCase
from game_of_life import GameOfLife


class TestGameOfLife(TestCase):
    def test1(self):
        field = """
        .....
        ..X..
        ...X.
        .XXX.
        ....."""

        expected = '.....\n.....\n.X.X.\n..XX.\n..X..'

        ga = GameOfLife(5, 5, field)
        ga.next_generation()

        self.assertEqual(expected, ga.to_string())

    def test2(self):
        field = """
        .....
        .....
        .XXX.
        .....
        ....."""

        expected = '.....\n..X..\n..X..\n..X..\n.....'

        ga = GameOfLife(5, 5, field)
        ga.next_generation()

        self.assertEqual(expected, ga.to_string())

    def test3(self):
        field = """
        ...XX.
        .XX...
        ..X...
        XX....
        X..XX."""

        expected = '.X..XX\n.XX...\nX.X...\nXXXX.X\nXXXXX.'

        ga = GameOfLife(5, 6, field)
        ga.next_generation()

        self.assertEqual(expected, ga.to_string())

    def test4(self):
        field = """
        ......
        ......
        ......"""

        expected = '......\n......\n......'

        ga = GameOfLife(3, 6, field)
        ga.next_generation()

        self.assertEqual(expected, ga.to_string())
