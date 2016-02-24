#!/usr/bin/env python
import unittest


class Teacher:
    grades = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth"}

    def __init__(self, first_name, last_name, age, classes, grade):
        self._first_name = first_name  # internal data attributes are set
        self._last_name = last_name
        self.age = age
        self._classes = classes
        self._grade = grade


    # when to use properties ?
    # when we need to associate an attribute with some logic in a class
    # and then we want to subclass that class
    # to avoid recoding the __getattr__ method
    # we use the property to edit the logic associated with that attribute only
    @property
    def first_name(self):
        """
        The first_name() method accesses the_first_name data attribute,and
        processes it before returningit as the value of the attribute
        """
        return self._first_name.capitalize()

    @property
    def last_name(self):
        return self._last_name.capitalize()

    @property
    def classes(self):
        return sorted(self._classes)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = int(value)

    @property
    def grade(self):
        return self.grades[self._grade]

    @grade.setter
    def grade(self, value):
        self.grade[value] # throw error if value != a key
        self._grade = value

    @grade.deleter
    def grade(self):
        self.age +=1
        del self._grade

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
        self.assertEqual(self.teacher.classes, ["Python 3-1","Python 3-2","Python 3-3"])
        self.assertEqual(self.teacher.grade, "Fifth")
        self.teacher.description = "curmudgeon"
        self.assertEqual(self.teacher.description, "curmudgeon")


    def test_set(self):
        self.teacher.age = "21"
        self.assertEqual(self.teacher._age, 21)
        self.assertEqual(self.teacher.age, 21)
        self.assertRaises(ValueError, self.setAgeWrong)

    def setAgeWrong(self):
        self.teacher.age = "twentyone"

    def test_delete(self):
        del self.teacher.grade
        self.assertEqual(self.teacher.age, 64)
        self.assertRaises(AttributeError, self.accessGrade)

    def accessGrade(self):
        return self.teacher.grade

if __name__ == "__main__":
    unittest.main()
