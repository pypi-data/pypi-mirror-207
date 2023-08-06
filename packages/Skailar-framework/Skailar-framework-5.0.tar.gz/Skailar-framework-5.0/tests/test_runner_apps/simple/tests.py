from unittest import TestCase

from skailar.test import SimpleTestCase
from skailar.test import TestCase as SkailarTestCase


class SkailarCase1(SkailarTestCase):
    def test_1(self):
        pass

    def test_2(self):
        pass


class SkailarCase2(SkailarTestCase):
    def test_1(self):
        pass

    def test_2(self):
        pass


class SimpleCase1(SimpleTestCase):
    def test_1(self):
        pass

    def test_2(self):
        pass


class SimpleCase2(SimpleTestCase):
    def test_1(self):
        pass

    def test_2(self):
        pass


class UnittestCase1(TestCase):
    def test_1(self):
        pass

    def test_2(self):
        pass


class UnittestCase2(TestCase):
    def test_1(self):
        pass

    def test_2(self):
        pass

    def test_3_test(self):
        pass
