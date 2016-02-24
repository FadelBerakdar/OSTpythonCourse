#!/usr/bin/env python

import unittest


class Teacher:
    grades = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth"}

    def __init__(self, first_name, last_name, age, classes, grades):
        """
        Here the __init __ method creates a regular attribute called _attrs, a
        dict in which the attribute values are kept, by making a direct entry
        in the instance's __dict__. It uses this technique to avoid a direct
        assignment, which would invoke the instance's __setattr__() method.
        That method attempts to store the attribute value against its name self.
        _attrs, which would need to be looked up by __getattr__(). This in
        turn would try and find the name "_attrs" in the self ._attrs dict,
        which would again invoke __get attr__(), and so on.
        This infinite regression would only terminate when the interpreter ran
        out of stack, the area of memory where it stores partially-completed
        function namespaces.
        """
        self.__dict__['_attrs'] = {}   # == super().__setattr__("_attr",{})
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.classes = classes
        self.grades = grades

    def __setattr__(self, key, value):
        self._attrs[key] = value  # --> filling up the dictionary

    def __getattr__(self, name):
        if name not in self._attrs[name]:
            raise AttributeError("Teacher has no attribute {0!r}".format(name))

        value = self.__attrs[name]

        if name in ("first_name", "last_name"):
            return value.capitalize()

        elif name == "age":
            return int(value)

        elif name == "classes":
            return sorted(value)

        elif name == "grade":
            return self.grades[value]

        else:
            return value


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
