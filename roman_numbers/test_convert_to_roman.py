from unittest import TestCase
from roman import convert_to_roman


class TestConvertToRoman(TestCase):
    def test_1(self):
        self.assertEqual(convert_to_roman(1), 'I')

    def test_4(self):
        self.assertEqual(convert_to_roman(4), 'IV')

    def test_5(self):
        self.assertEqual(convert_to_roman(5), 'V')

    def test_400(self):
        self.assertEqual(convert_to_roman(400), 'CD')

    def test_500(self):
        self.assertEqual(convert_to_roman(500), 'D')

    def test_600(self):
        self.assertEqual(convert_to_roman(600), 'DC')

    def test_650(self):
        self.assertEqual(convert_to_roman(650), 'DCL')

    def test_2325(self):
        self.assertEqual(convert_to_roman(2325), 'MMCCCXXV')

    def test_3494(self):
        self.assertEqual(convert_to_roman(3494), 'MMMCDXCIV')

