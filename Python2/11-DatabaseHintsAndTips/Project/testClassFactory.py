#!/usr/bin/env python3
#                     Class Factory Test Module
#                        testClassFactory.py
# By: Fadel Berakdar
# Date: 28/7/2015

"""
General Purpose Approach
Creating class with columns names already incorporated
By constructing the class inside a function, which takes the columns and the
table names as arguments.
The function then returns the class after inserting the table name as class
attributes. the function effectively becomes a "Class Factory" returning
slightly different class each time its called
"""

import unittest
from classFactory import build_row

import mysql.connector
from database import login_info


class DBTest(unittest.TestCase):
    def setUp(self):
        C = build_row("user", "id name email")
        self.c = C([1, "steve", "steve@"])

    def test_attributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "steve")
        self.assertEqual(self.c.email, "steve@")

    def test_retrieve_data_row_objects(self):
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()

        table = 'animal'
        cols = 'id name family weight'
        D = build_row(table, cols)
        cursor.execute("USE Zoo")
        sql = 'SELECT * FROM animal;'
        cursor.execute(sql)
        expected_rows = set()

        for row in cursor.fetchall():
            expected_rows.add(repr(D(row)))

        d = D([100, "Joe", "Python", 10])  # making up data
        observed_rows = set()
        for row in d.retrieve(cursor):
            observed_rows.add(repr(row))

if __name__ == "__main__":
    unittest.main()
