import settings
from database import login_info
import mysql.connector as msc
import datetime
import time
import matplotlib.pyplot as plt
import numpy as np


def save_email(recipients, starttime, daysout):
    conn = msc.Connect(**login_info)
    curs = conn.cursor()
    curs.execute("""CREATE DATABASE IF NOT EXISTS MailDB""")
    curs.execute("""USE MailDB""")
    curs.execute("DROP TABLE IF EXISTS messages")
    conn.commit()
    curs.execute(settings.TABLEDEF)
    conn.commit()
    
    for day in range(daysout):
        date_time = starttime + datetime.timedelta(days=day)
        for recipient_name, recipient_address in recipients:
            data = ("Test", date_time, "Eddie", "eddie.valv@gmail.com", 
                    recipient_name, recipient_address, "JOTD") 
            curs.execute("""
            INSERT INTO messages (msgMessageID, msgDate, msgSenderName,
            msgSenderAddress, msgRecipientName, msgRecipientAddress, msgText)
            VALUES (%s, %s, %s, %s, %s, %s, %s)""", data)
    conn.close()


RECIPIENTS = (('Frank', 'frank@gmail.com'), ('Michael', 'michael@gmail.com'),
              ('Annie', 'annie@gmail.com'))
STARTTIME = datetime.datetime(2014, 12, 12)
day_counts = [1, 10, 50, 100, 500, 1000, 5000, 10000]
results = []
'''
for day_count in day_counts:
    print(day_count)
    start = time.time()
    save_email(recipients=RECIPIENTS,
               starttime=datetime.datetime(2014, 12, 12), daysout=day_count)
    end = time.time()
    interval = end - start
    results.append(interval)
print(results)
'''
plt.plot(day_counts, [0.036006927490234375, 0.04800915718078613, 0.16103291511535645, 0.32006406784057617, 1.5713138580322266, 3.049610137939453, 15.12502384185791, 30.343067169189453])
plt.show()

