import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

pattern = r'''
(?P<email>\b[A-Za-z+.]+@[A-Za-z+.]+),\s  # email
(?P<phone>\d{3}-\d{3}-\d{4}),\s          # phone
(?P<twitters>@[A-Za-z]+)$              # twitter
'''
regex = re.compile(pattern, re.X | re.M)


for match in regex.finditer(string) :
    print("<{email}> {phone:<20}{twitters}".format(**match.groupdict()))


string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

pattern = r"""
^(?P<last_name>[A-Za-z]+[\sA-Za-z]*),\s
(?P<first_name>[A-Za-z]+[\sA-Za-z]*):\s
(?P<score>\d{e()2})$
"""
regex = re.compile(pattern, re.M|re.X)


for match in regex.finditer(string):
    print("{last_name} {first_name} {score}".format(**match.groupdict()))

class Player(object):
    def __init__(self, last, first, score):
        self.last = last
        self.first = first
        self.score = score

"""
re.VERBOSE : flag lets us write our patterns out over multiple lines, ignoring whitespace and comments
re.MULTILINE : new lines are treated as new strings
re.IGNORECASE :
re.X :
"""

print("*" * 40)

string = "asdasd asdasd, sada. JohnSmith. asdasd"
pattern = r"John\Smith"
regex = re.search(pattern, string)
print(regex.group())