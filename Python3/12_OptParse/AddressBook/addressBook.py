#!/usr/bin/env python

# addressBook.py: a very simple email address book program
# By: Fadel Berakdar
# Date: 26 Jan 2016

from optparse import OptionParser
import re
import shelve
import configparser


config = configparser.RawConfigParser()
config.read("/Users/Phoenix/Dropbox/Projects/Code/Python3/12_OptParse/AddressBook/addressBook.cfg")
shelf_location = config.get('database', 'file')


def add_email(email):
    """
    add a valid email to the database if its not existed.
    :param email: a valid email string
    :return: message as tuple(boolean, string)
    """
    validate_email(email)         # return error if the email is not valid email
    shelf = shelve.open(shelf_location)     # persistent, dictionary-like object

    if "emails" not in shelf:   # check if emails list in the database shelf
        shelf['emails'] = []

    emails = shelf['emails']  # assign the emails list in shelf to a variable

    if email in emails:        # check if the email already been added
        message = False, 'Email "%s" already in address book' % email
    else:
        emails.append(email)
        message = True, 'Email "%s" added to address book' % email

    shelf['emails'] = emails    # since writeback=False
    shelf.close()
    return message


def delete_email(email):
    """
    delete a valid emails if its existed,
    :param email: a valid email string
    :return: message as tuple(boolean, string)
    """
    validate_email(email)

    shelf = shelve.open(shelf_location)

    if "emails" not in shelf:
        shelf['emails'] = []
    emails = shelf['emails']

    try:
        emails.remove(email)
        message = True, 'Email "%s" removed from address book' % email
    except ValueError:
        message = False, 'Email "%s" was not in address book' % email
    shelf['emails'] = emails
    shelf.close()
    return message


def display_emails():
    """
    A function to display the content of the emails address book
    :return: a tuple (boolean, text)
    """
    shelf = shelve.open(shelf_location)
    emails = shelf['emails']
    shelf.close()

    text = "********* Emails List *********\n"

    if not emails:
        text += "Empty Database"
        return False, text
    else:
        for email in emails:
            text += email + '\n'
        return True, text


class InvalidEmail(Exception):
    pass


def validate_email(email):
    """
    A function raises an error when invalid email passed
    :param email: email string
    :return: tuple (boolean, text)
    """
    if not re.search(r"\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+", email):
        raise InvalidEmail("Invalid email: " + email)
    return True


def main():
    parser = OptionParser()

    # Options:
    parser.add_option("-a",            # short option string
                      "--action",      # long option string
                      action="store",  # what to do with the option's argument
                      dest="action",   # where to store the option's argument
                      type="string",   # the type of accepted option's argument
                      help="requires -e option. Actions: add/delete"  # help
                      )

    parser.add_option("-e",
                      "--email",
                      action="store",
                      dest="email",
                      help="email used in the -a option"
                      )

    parser.add_option('-d',
                      "--display",
                      action="store_true",  # the display attribute of options
                      dest="display",
                      help="show all emails"
                      )
    (options, args) = parser.parse_args()

    # validation
    if options.action and not options.email:
        parser.error("option -a requires option -e")
    elif options.email and not options.action:
        parser.error("option -e requires option -a")

    # routes requests"
    if options.action == 'add':
        try:                                # check before adding new email
            add_email(options.email)
        except InvalidEmail:                # dealing with expected exception
            parser.error("option -e requires a valid email address")
    elif options.action == 'delete':
        delete_email(options.email)

    if options.display:
        print(display_emails()[1])

if __name__ == '__main__':
    main()
