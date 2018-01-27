from unittest import TestCase
from koch_curve import koch_curve_turns


class TestKochCurveTurns(TestCase):
    def test1(self):
        expected = [60, -120, 60]
        self.assertEqual(expected, koch_curve_turns(1))

    def test2(self):
        expected = [60, -120, 60, 60, 60, -120, 60, -120, 60, -120, 60, 60, 60, -120, 60]
        self.assertEqual(expected, koch_curve_turns(2))
