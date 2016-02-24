__author__ = 'Fadel'
#!/usr/local/bin/python3

#              code refactor
#             refactory.py.

# By:        Fadel Berakdar
# Date:      18 Feb 2015


small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')

def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into as'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """

    new_title = ""

    new_title = title.split()[0].capitalize() + " "

    for word in title.split()[1:] :
        if word.lower() in small_words:
            new_title += word.lower() + " "
        else :
            new_title += word.capitalize() + " "
    return new_title.strip()



def _test():
    import doctest

    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()


"""
Hi Fadel,

We worked long and hard to develop such crappy code. Believe me, it took a lot of beers to get it to this point ;-)

You've done an excellent job at getting rid of the "kruft" that made the original clunky and bloated.  The result is an elegant piece of very readable code.  Good work.

Here's the unofficial world record, in terms of the minimum number of lines of code:

    title = title.title().split()
    for i, word in enumerate(title[1:]):
        if word.lower() in small_words:
            title[i+1] = word.lower()
    return " ".join(title)

And here's another alternative solution, for your inspection:

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')

def book_title(title):
    """skipping tests"""

    if not title.strip():
        return ''

    lst_of_words = title.lower().split()

    new_title = lst_of_words.pop(0).title()

    for word in lst_of_words:
        new_title += ' ' + (word if word in small_words else word.capitalize( ))

    return new_title

-Pat

"""