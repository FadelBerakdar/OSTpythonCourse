from datetime import datetime, timedelta


"""
An example shows how to skip over weekends.
"""


delivery = datetime.now()
delta = timedelta(5)
count = 0

while count < 31:
    delivery = delivery + delta
    if delivery.isoweekday() in (6, 7):
        continue
    count += 1

now = datetime.now()
print(now)
print(delivery)
print("Today: %s" % now.strftime("%d"))
print("Delivery: %s" % delivery.strftime("%d"))
