"""
Sample program to list subjects by date.
"""
from database import login_info
import mysql.connector
from email import message_from_string

conn = mysql.connector.Connect(**login_info)
curs = conn.cursor()

curs.execute("SELECT msgText FROM message ORDER BY msgDate")
for text, in curs.fetchall():
    msg = message_from_string(text)
    print(msg['date'], msg['subject'])
