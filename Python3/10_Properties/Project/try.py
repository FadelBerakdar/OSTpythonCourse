import re

pattern = r"^[A-Z]{2}$"
string = "ACC"

print(re.search(pattern, string, ))
