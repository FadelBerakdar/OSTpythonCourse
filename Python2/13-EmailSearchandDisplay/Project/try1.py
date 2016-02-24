import mysql.connector
from database import login_info


db = mysql.connector.Connect(**login_info)
cursor = db.cursor()
cursor.execute(""" SHOW DATABASES""")
print(cursor.fetchall())
