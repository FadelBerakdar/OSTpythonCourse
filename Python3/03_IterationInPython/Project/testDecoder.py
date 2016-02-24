#!/usr/bin/env python

# By: Fadel Berakdar
# Date: 10 Nov 2015

import unittest
from decoder import Alphabator
from string import ascii_uppercase


class TestAlpha(unittest.TestCase):

    def test_easy26(self):
        a = Alphabator(range(1, 27))
        self.assertEqual(list(ascii_uppercase), list(a))

    def test_upper_range(self):
        a = Alphabator(range(40, 50))
        self.assertEqual(list(range(40, 50)), list(a))

    def test_various_objects(self):
        l = ["python", object, ascii_uppercase, 10, Alphabator]
        a = list(Alphabator(l))
        self.assertNotEqual(l[3], a[3])
        self.assertEqual("J", a[3])
        self.assertTrue(isinstance(a[1], object))


if __name__ == "__main__":
    unittest.main()
