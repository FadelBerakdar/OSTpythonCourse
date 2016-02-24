#!/usr/bin/env python
# By: Fadel Berakdar
# date: 22 Nov 2015


import unittest
from furnishings import *


class TestMapHome(unittest.TestCase):

    def setUp(self):
        self.home = list()
        self.home.append(Bed("Bedroom"))
        self.home.append(Sofa("Living Room"))
        self.home.append(Table("Kitchen"))
        self.home.append(BookShelf("Living Room"))
        self.home.append(Sofa("Bedroom"))

    def test_map_home(self):
        expected = {
            "Living Room": [self.home[1], self.home[3]],
            "Kitchen": [self.home[2]],
            "Bedroom": [self.home[0], self.home[4]]
                    }
        observed = map_home(self.home)
        self.assertEqual(expected, observed)

    def test_map_mentor(self):

        observed = map_home(self.home)
        print(observed)
        self.assertTrue(isinstance(observed['Living Room'][0], Sofa))
        self.assertTrue(isinstance(observed['Living Room'][1], BookShelf))
        self.assertTrue(isinstance(observed['Kitchen'][0], Table))
        self.assertTrue(isinstance(observed['Bedroom'][0], Bed))
        self.assertTrue(isinstance(observed['Bedroom'][1], Sofa))

    def test_empty(self):
        self.assertIsNotNone(map_home(self.home))

if __name__ == "__main__":
    unittest.main()
