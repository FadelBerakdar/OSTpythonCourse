
# Complex Inheritance Program
import unittest

class Maurice(object):
    def hair(self):
        return "red"


class Vivian(object):
    def hair(self):
        return "brown"


class Isandore(object):
    def hair(self):
        return "bald"


class Tracy(object):
    def hair(self):
        return "gray"

class Mother(Maurice, Vivian):
    pass


class Father(Isandore, Tracy):
    pass

class Child(Father, Mother):
    pass


class TestHair(unittest.TestCase):
    def test_hair(self):
        child = Child()
        hair = child.hair()

        self.assertNotEqual(hair, "red")
        self.assertNotEqual(hair, "brown")
        self.assertNotEqual(hair, "gray")
        self.assertEqual(hair, "bald")
if __name__ == "__main__":
    unittest.main()