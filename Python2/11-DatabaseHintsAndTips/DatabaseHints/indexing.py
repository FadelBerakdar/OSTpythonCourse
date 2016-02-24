#!usr/bin/env python3

# Demonstration of Index access to database
import mysql.connector

from database import login_info


class Animal(object):
    def __init__(self, id, name, family, weight):
        self.id = id
        self.name = name
        self.family = family
        self.weight = weight

    def __repr__(self):
        return "Animal {0} {1} {2} {3}".format(self.id, self.name,
                                               self.family, self.weight)

if __name__ == "__main__":
    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()
    cursor.execute("""USE Zoo""")

    # By numerical indexing:

    print("\n******* Numerical Indexing *******\n")
    fmt = "{0:10} {1:10} {2:6}"
    print(fmt.format("Animal", "Family", "Weight"))
    print(28*"-")
    cursor.execute("SELECT * FROM Animal")
    for animal in cursor.fetchall():
        print(fmt.format(animal[1], animal[2], animal[3]))

    # By alphabetical indexing:

    print("\n******* Alphabetical Indexing *******\n")
    fmt = "{0:10} {1:10} {2:6}"
    print(fmt.format("Animal", "Family", "Weight"))
    print(28*"-")
    cursor.execute("SELECT name, weight, family FROM Animal")
    for name, family, weight in cursor.fetchall():
        print(fmt.format(name, weight, family))

    # By using classes:
    # creating an object for each row that has attributes
    # with the same names as the columns

    print("\n******* CLass Indexing *******\n")
    cursor.execute("SELECT id, name, family, weight FROM Animal")
    animals = [Animal(*row) for row in cursor.fetchall()]
    from pprint import pprint
    pprint(animals)

