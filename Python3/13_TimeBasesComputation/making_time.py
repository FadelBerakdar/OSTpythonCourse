from datetime import datetime

print(datetime(2012, 10, 31))
print(datetime(2012, 10, 31, 12))
print(datetime(2012, 10, 31, 12, 30))
print(datetime(2012, 10, 31, 12, 30, 59))
print(datetime(2012, 10, 31, 12, 30, 59, 300))


dt = datetime(2012, 10, 31, 12, 30, 59, 300)

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)