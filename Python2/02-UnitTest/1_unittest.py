__author__ = 'Fadel'
#!/usr/bin/env python3

#              unittest test program for semi-title() function
#                        title.p
# By: Fadel Berakdar
# Date: 2 Mar 2015

'''
Make a UnitTesting_Homework project and assign it to the Python2_Homework
working set. In this project, write a unittest test program for the following
function. (The test program makes unittest.TestCase assertions about the results
 of
 calling the function with known arguments.)
def title(s):
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:]
Test your results for a given string s by comparing them with s.title().
Because this is purely an exercise, it's OK to put your test code in the same
file as the
function and just hand in a single file. Your file should be an importable
module.
You should be able to find an example that shows title(s) and s.title() diverge
(have different output).
Bonus marks for fixing the error in the function above (making it behave more
like the native method).



def title(s):
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:].lower()

string = input("Plz enter a string")
print(string.title(),title(string))
#FADe sad

'''
import unittest


def title(s):
    """.title's twin function."""
    string = ""
    for word in s.split():
        string += ''.join(word[0].upper() + word[1:].lower() + " ")
    return string.strip()


class TestTitle(unittest.TestCase):
    def test_convergent(self):
        words_list = ["hey there", "hEY tHERE"]
        for s in words_list:
            self.assertEqual(title(s), s.title(),
                             "\nTesting: {}\nThese should be the same: "
                             "\nThe built in:{}\ntitle(): {}".
                             format(s, s.title(), title(s)))

    def test_divergent(self):
        s = "barack o'bama"
        self.assertNotEqual(s.title(), title(s), "s.title should result in "
                                                 "\"{}\"".format(s.title()))

if __name__ == "__main__":
    unittest.main()
'''
a = ("                                                                       ")
print(len(a))
def test_a_single_word(self):
        """Tests  results of title(s) against s.title() """
        test = 'test'
        msg="title(s) returned '{0}' and s.title() returned '{1}'"
        self.assertEqual(title(test),
                         test.title(),
                         msg.format(title(test),test.title()))
'''
