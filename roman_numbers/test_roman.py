from unittest import TestCase
from roman import convert_from_roman


class TestRoman(TestCase):
    def test_I(self):
        self.assertEqual(convert_from_roman('I'), 1)

    def test_V(self):
        self.assertEqual(convert_from_roman('V'), 5)

    def test_X(self):
        self.assertEqual(convert_from_roman('X'), 10)

    def test_L(self):
        self.assertEqual(convert_from_roman('L'), 50)

    def test_C(self):
        self.assertEqual(convert_from_roman('C'), 100)

    def test_D(self):
        self.assertEqual(convert_from_roman('D'), 500)

    def test_M(self):
        self.assertEqual(convert_from_roman('M'), 1000)

    def test_IX(self):
        self.assertEqual(convert_from_roman('IX'), 9)

    def test_IXX(self):
        self.assertEqual(convert_from_roman('IXX'), 19)

    def test_LIX(self):
        self.assertEqual(convert_from_roman('LIX'), 59)

    def test_MCCDLIX(self):
        self.assertEqual(convert_from_roman('MCCDLIX'), 1359)
