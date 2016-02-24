#!/usr/bin/env python

# By: Fadel Berakdar
# Date: 10 Nov 2015

import unittest

from coconut import Inventory, American, SouthAsian, MiddleEastern


class TestCoconut(unittest.TestCase):

    def setUp(self):
        """
        Initializing the Inventory and Coconuts objects.
        """
        self.inventory = Inventory()

        self.singaporean = SouthAsian()
        self.malaysian = SouthAsian()
        self.syrian = MiddleEastern()
        self.canadian = American()
        self.florida = American()
        self.brazilian = American()

        self.inventory.add_coconut(self.syrian)
        self.inventory.add_coconut(self.singaporean)
        self.inventory.add_coconut(self.malaysian)
        self.inventory.add_coconut(self.canadian)
        self.inventory.add_coconut(self.florida)
        self.inventory.add_coconut(self.brazilian)

    def test_different_weights(self):
        """
        Test the weights associated with each coconut class
        """
        self.assertNotEqual(self.singaporean.weight, self.syrian.weight)
        self.assertNotEquals(self.singaporean.weight, self.canadian.weight)
        self.assertNotEquals(self.syrian.weight, self.canadian.weight)

    def test_integrity(self):
        self.assertRaises(AttributeError, self.inventory.add_coconut, "Fake")


    def test_total_weights(self):
        """
        Test the functionality of the total_weight method
        """
        self.assertEquals(self.inventory.total_weight(), 19, "the total is 19!")


if __name__ == "__main__":
    unittest.main()
