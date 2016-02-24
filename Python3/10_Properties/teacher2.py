#!/usr/bin/env python

import unittest


class Teacher:
    grades = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth"}

    def __init__(self, first_name, last_name, age, classes, grade):
        self._first_name = first_name  # internal data attributes are set
        self._last_name = last_name
        self._age = age
        self._classes = classes
        self._grade = grade

    @property
    # when to use properties ?
    # when we need to associate an attribute with some logic in a class
    # and then we want to subclass that class
    # to avoid recoding the __getattr__ method
    # we use the property to edit the logic associated with that attribute only
    def first_name(self):
        """
        The first_name() method accesses the_first_name data attribute,and
        processes it before returningit as the value of the attribute
        """
        return self._first_name.capitalize()

    def last_name(self):
        return self._last_name.capitalize()

    last_name = property(last_name)

    def age(self):
        return int(self._age)
    age = property(age)

    def classes(self):
        return sorted(self._classes)
    classes = property(classes)

    def grade(self):
        return self.grades[self._grade]
    grade = property(grade)


class TestTeacher(unittest.TestCase):

    def setUp(self):
        self.teacher = Teacher("steve",
                               "holden",
                               "63",
                               ["Python 3-1", "Python 3-2", "Python 3-3"], 5)

    def test_get(self):
        self.assertEqual(self.teacher.first_name, "Steve")
        self.assertEqual(self.teacher.last_name, "Holden")
        self.assertEqual(self.teacher.age, 63)
        self.assertEqual(self.teacher.classes, ["Python 3-1",
                                                "Python 3-2",
                                                "Python 3-3"])
        self.assertEqual(self.teacher.grade, "Fifth")
        self.teacher.description = "curmudgeon"
        self.assertEqual(self.teacher.description, "curmudgeon")


if __name__ == "__main__":
    unittest.main()
