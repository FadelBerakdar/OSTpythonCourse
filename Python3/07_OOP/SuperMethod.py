import unittest


"""
super.py: demonstrate how to extend a superclass method.
"""


class Car(object):
    def __init__(self, color, cc):
        self.color = color
        self.cc = cc


class Toyota(Car):
    def __init__(self, color, cc, model):
        Car.__init__(self, color, cc)
        self.model = model


class Ford(Car):
    def __init__(self, color, cc, model):
        super().__init__(color, cc)
        self.model = model


class Test(unittest.TestCase):
    def test_Toyota(self):
        car1 = Car("red", 2000)
        car2 = Toyota("red", 2000, "Corolla")
        self.assertEqual(car1.color, car2.color)
        self.assertEqual(car1.cc, car2.cc)
        self.assertEqual(car2.model, "Corolla")

    def test_ford(self):
        car1 = Car("red", 2000)
        car2 = Ford("red", 2000, "Taurus")
        self.assertEqual(car1.color, car2.color)
        self.assertEqual(car1.cc, car2.cc)
        self.assertEqual(car2.model, "Taurus")


if __name__ == "__main__":
    unittest.main()
