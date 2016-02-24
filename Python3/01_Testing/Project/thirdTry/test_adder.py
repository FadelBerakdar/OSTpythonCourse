#!/usr/bin/env python

#       Testing the functionality of the adder.py
#             test_adder.py

# By: Fadel Berakdar
# Date: 6 Oct 2015


import unittest
from adder import supper_adder


class TestSupperAdder(unittest.TestCase):
    """
    Testing the supper_adder function.
    """
    def test_failure(self):
        """
        testing type errors.
        """
        self.assertRaises(TypeError, supper_adder, 1, 2.0)
        self.assertRaises(TypeError, supper_adder, 1, "a")
        self.assertRaises(TypeError, supper_adder, 1.0, 2.0)
        self.assertRaises(TypeError, supper_adder, "a", "b")
        self.assertRaises(TypeError, supper_adder, True, False)

    def test_success(self):
        """
        Testing valid data.
        """
        self.assertEqual(supper_adder(1, 1), 2, "1 + 1 = 2 !!!")


if __name__ == "__main__":
    unittest.main()
