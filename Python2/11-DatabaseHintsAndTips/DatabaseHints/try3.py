import mysql.connector
from database import login_info
'''
table = "Animal"
columns = "id name family"
conditions = ["id=7"]

query = "SELECT {0} FROM {1} WHERE {2}".format(", ".join(columns.split()),
                                                         table,
                                                         conditions[0]
                                               )

db = mysql.connector.connect(**login_info)
cursor = db.cursor()
cursor.execute("""SHOW DATABASES""")
'''

def funct(*args):
    for arg in args:
        print(arg)

funct(*{"hi":3, "sad":2})
