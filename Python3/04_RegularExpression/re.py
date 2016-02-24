"""
 ______________________________________________________________________
|                        Regular Expression                            |
|______________________________________________________________________|
| .     |  any character except new line \n                            |
| \w    |  any unicode word character Aa1_                             |
| \W    |  anything that isn't unicdoe character                       |
| \s    |  any white space, tabs, and newlines                         |
| \S    |  anything that isn't while space                             |
| \d    |  any number from 0 to 9                                      |
| \D    |  anything that isn't number                                  |
| \b    |  any word boundaries "edges of a word"                       |
| \B    |  anything that isn't word boundaries                         |
| \+    |  to escape a character +)({}#@!%^&*-                         |
|______________________________________________________________________|
| {3}   |  something that occurs exactly three times                   |
| {,3}  |  something that occurs 0 to three times                      |
| {2,3} |  something that occurs two to three times                    |
| ?     |  something that occurs 0 or one time                         |
| *     |  something that occurs at least one time                     |
| +     |  something that occurs at least once                         |
|_______|______________________________________________________________|
|[aple] |  apple                                                       |
| [a-z] |  any lowercase letters from a to z                           |
| [^2]  |  anythin that isn't 2                                        |
| [^\t] |  ignore tap character                                        |
|_______|______________________________________________________________|
|  ^    |  begining of new line                                        |
|  $    |  the end of the line                                         |
|  ()   |  group                                                       |
|  ?p< >|  group name                                                  |
| r""   | we have to use r"" to avoid using \\, so we use raw string r |
|_______|______________________________________________________________|

print(r"\tb")
print("\tb")

gro up() | Returns the entire matched string.
555-555-5555
start()
Returns the start index of the match.
0
end()
Returns the end index o f the m atch.
12
span()
Returns a tuple with the start and end indexes of the match.
(0,12)
"""

def ccn_safety(string):
    #pattern = r"\d{4}-\d{4}-\d{4}"
    pattern = r"(\d{4}-){3}(?P\d{4})"
    #return re.sub(pattern, "XXXX-XXXX-XXXX-" + "\g", string)
    return re.sub(r"(\d{4}-){3}(\d{4})", "XXXX-XXXX-XXXX-"+"\g", string)





a = "4444"
b = " 4444"
c = "asda 4444"
d = "AAC"
e = "AC"
f = "1AC"

import re

pattern = r"^\d{4}$"
pattern = r"^[A-Z]{2}$"

for ob in (a, b, c, d, e, f):
    print(bool(re.search(pattern,ob)))