# Polymorphism

import unittest


class Animal(object):
    def __init__(self, name):
        self.name = name

    def sound(self):   # abstract method
        raise NotImplementedError("Animals need sound method")

    def has_wings(self):
        return False


class Lion(Animal):
    def sound(self):
        return "hreee"


class Dog(Animal):
    def sound(self):
        return "woof"


class Chicken(Animal):
    def sound(self):
        return "bok bok"

    def has_wings(self):  # overrides the Animal class's has_wings() method
        return True


class Test(unittest.TestCase):
    def test_base_animal_class(self):
        """Test the basics of Animal class"""
        animal = Animal("Orwell")
        self.assertRaises(NotImplementedError, animal.sound)
        self.assertFalse(animal.has_wings())

    def test_lion(self):
        """Test the inhabitants of the farm"""
        lion = Lion("Napoleon")
        self.assertEqual(lion.sound(), "hreee")
        self.assertFalse(lion.has_wings())

    def test_dog(self):
        dog = Dog("BlueBell")
        self.assertEqual(dog.sound(), "woof")
        self.assertFalse(dog.has_wings())

    def test_chicken(self):
        chicken = Chicken("Kulak")
        self.assertEqual(chicken.sound(), "bok bok")
        self.assertTrue(chicken.has_wings())

if __name__ == "__main__":
    unittest.main()
