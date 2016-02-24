#!/usr/bin/env python

# testAddressBook.py: addressBookOLD.py's testing suit
# By: Fadel Berakdar
# Date: 26 Jan 2016


import unittest
import shelve
import addressBook


class TestEmailHandlers(unittest.TestCase):
    """
    A test suite to test the functionality of AddressBook.
    """
    def setUp(self):
        self.email = "test123@t.com"
        shelf_location = addressBook.shelf_location

        shelf = shelve.open(shelf_location)     # to delete self.email
        if 'emails' in shelf:
            if self.email in shelf['emails']:
                shelf['emails'] = []
        shelf.close()

    def test_email_delete(self):
        """
        testing suite to check the functionality of email_delete function
        :return:
        """
        addressBook.add_email(self.email)
        self.assertEqual(addressBook.delete_email(self.email)[0], True)
        self.assertEqual(addressBook.delete_email(self.email)[0], False)

    def test_add_email(self):
        """
        testing suite to check the functionality of add_email function
        :return:
        """
        self.assertEqual(addressBook.add_email(self.email)[0], True)
        self.assertEqual(addressBook.add_email(self.email)[0], False)

    def test_display_emails(self):
        """
        testing suite to check the functionality of display_emails function
        :return:
        """
        addressBook.add_email(self.email)
        val, display = addressBook.display_emails()
        self.assertTrue(self.email in display)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
