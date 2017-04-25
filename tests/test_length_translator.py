from unittest import TestCase
from length_translator import translator


class TestLengthTranslator(TestCase):
    @staticmethod
    def exponential_format(length):
        return '{:.2e}'.format(length)

    def test_from_mile_to_km(self):
        self.assertEqual(self.exponential_format(24.90), translator(15.5, 'mile', 'km'))

    def test_from_cm_to_inch(self):
        self.assertEqual(self.exponential_format(39.37), translator(100, 'cm', 'inch'))

    def test_from_inch_to_cm(self):
        self.assertEqual(self.exponential_format(100), translator(39.37, 'inch', 'cm'))

    def test_from_mm_to_cm(self):
        self.assertEqual(self.exponential_format(10), translator(100, 'mm', 'cm'))

    def test_from_km_to_mile(self):
        self.assertEqual(self.exponential_format(1000), translator(1609, 'km', 'mile'))

    def test_from_cm_to_foot(self):
        self.assertEqual(self.exponential_format(100), translator(3048, 'cm', 'foot'))

    def test_from_m_to_yard(self):
        self.assertEqual(self.exponential_format(109.361), translator(100, 'm', 'yard'))

    def test_from_yard_to_m(self):
        self.assertEqual(self.exponential_format(100), translator(109.361, 'yard', 'm'))

    def test_from_foot_to_cm(self):
        self.assertEqual(self.exponential_format(3048), translator(100, 'foot', 'cm'))

    def test_from_yard_to_foot(self):
        self.assertEqual(self.exponential_format(300), translator(100, 'yard', 'foot'))

    def test_from_foot_to_yard(self):
        self.assertEqual(self.exponential_format(100), translator(300, 'foot', 'yard'))
