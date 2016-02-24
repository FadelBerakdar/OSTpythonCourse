from datetime import datetime, timedelta


"""
calculating the time in the future :D



now = datetime.now()
seconds = timedelta(seconds=1000)
minutes = timedelta(minutes=100)
hours = timedelta(hours=3)
weeks = timedelta(weeks=2)

composite = timedelta(hours=1, minutes=30)

print(now)
print(now + seconds)
print(now + minutes)
print(now + hours)
print(now + weeks)

print(now + composite)


"""
from datetime import datetime

formatter_string = "%m-%d-%Y %I:%M %p"
date_string = "07-24-1985 2:00 AM"

time = datetime.strptime(date_string, formatter_string)
print(time)
time_string = time.strftime(formatter_string)
print(time_string)

from datetime import datetime

now = datetime.now()
print(now.hour)