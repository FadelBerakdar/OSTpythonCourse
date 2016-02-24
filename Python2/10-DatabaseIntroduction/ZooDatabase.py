#!usr/bin/env python3
#       Populates a table with data from a python tuple
# By : Fadel Berakdar
# Date: 4 / 7 / 2015


import mysql.connector
from database import login_info

# etpass.getpass("Password:")

# os.system("sudo /usr/local/mysql/support-files/mysql.server start")
# mysql -h sql -u mberakda -p mberakda


if __name__ == "__main__":
    db = mysql.connector.Connect(**login_info)
    # convert the dictionary to a set of keyword arguments
    cursor = db.cursor()
    # cursor.execute("DROP DATABASE IF EXISTS Zoo")
    cursor.execute("CREATE DATABASE IF NOT EXISTS Zoo")
    cursor.execute("USE Zoo")
    cursor.execute("DROP TABLE IF EXISTS Animal")
    cursor.execute("""
              CREATE TABLE IF NOT EXISTS Animal (
                    id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(50),
                    family VARCHAR(50),
                    weight INTEGER) ENGINE=MYISAM""")

    data_animal = (("Ellie", "Elephant", 2350),
                   ("Gerald", "Gnu", 1400),
                   ("Gerald", "Giraffe", 940),
                   ("Leonard", "Leopard", 280),
                   ("Sam", "Snake", 24),
                   ("Steve", "Snake", 35),
                   ("Zorro", "Zebra", 340),
                   ("littleTiger", "Cat", 7),
                   ("Aarnie", "Aardvark", 40)
                   )
    # nukes the contents of the animal table :D
    cursor.execute("DELETE FROM Animal")
    for entry in data_animal:
        cursor.execute("""
        INSERT INTO animal (name, family, weight)
        VALUES (%s, %s, %s) """, entry)

    db.commit()

    cursor.execute("DROP TABLE IF EXISTS Food")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Food (
                    id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    anid INTEGER,
                    feed VARCHAR(50),
                    FOREIGN KEY (anid) REFERENCES Animal(id)) ENGINE=MYISAM""")

    data_food = (("Ellie", "Elephant", ['hay', 'peanuts']),
                 ("Gerald", "Gnu", ['leaves', 'shoots']),
                 ("Gerald", "Giraffe", ['hay', 'grass']),
                 ("Leonard", "Leopard", ['meat']),
                 ("Sam", "Snake", ['mice', 'meat']),
                 ("Steve", "Snake", ['mice', 'meat']),
                 ("Zorro", "Zebra", ['grass', 'leaves'])
                 )

    cursor.execute("DELETE FROM Food ")
    for name, family, foods in data_food:
        cursor.execute(" SELECT id FROM animal WHERE name=%s and family=%s",
                       (name, family))
        _id = cursor.fetchone()[0]
        for food in foods:
            cursor.execute(" INSERT INTO food (anid,feed) VALUES (%s,%s)",
                           (_id, food))
        db.commit()
        print("Processed", name, family, id)

    cursor.execute("""SELECT id, name FROM Animal """)
    animals = cursor.fetchall()

# Verifying the animals which are in animal table but not in Food table
    cursor.execute(""" SELECT id, name, family FROM animal
                       WHERE id NOT IN (SELECT anid FROM food)""")

    hungryAnimals = cursor.fetchall()
    if len(hungryAnimals) > 0:
        fmt = "{0:^5} {1:^12} {2:^15}"
        print("\nThe following animals are not listed in the food table: ")
        print(format(fmt.format("ID", "Name", "Family")))
        for animal in hungryAnimals:
            print(fmt.format(animal[0], animal[1], animal[2]))
    else:
        print("Each animal eats at least one food")
