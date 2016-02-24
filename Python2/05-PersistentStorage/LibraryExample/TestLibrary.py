__author__ = 'Fadel'
import unittest
import glob
import library
import os


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib_fn = "/Users/Fadel/Dropbox/python/Code/Python2/05-PersistentStorage/LibraryExample/lib.shelve"
        self.lib = library.Library(self.lib_fn)

        self.fixture_author1 = library.Author("Octavia", "Estelle", "Butler")
        self.fixture_book1 = library.Book("0807083100",
                                          "Kindred",
                                          [self.fixture_author1])
        self.fixture_author2 = library.Author("Robert‰a", "Anson", "Heinlein")
        self.fixture_book2 = library.Book("0441709348",
                                          "Stranger in a Strange Land",
                                          [self.fixture_author2])
        self.lib.add(self.fixture_book1)
        self.lib.add(self.fixture_book2)

    def testGetByISBN(self):
        observed = self.lib.get_by_isbn(self.fixture_book1.isbn)
        expected = self.fixture_book1
        self.assertEqual(observed, expected)

    def testGetByTitle(self):
        observed = self.lib.get_by_title(self.fixture_book2.title)
        expected = self.fixture_book2
        self.assertEqual(observed, expected)

    def testGetByAuthor(self):
        observed = self.lib.get_by_author(self.fixture_book1.authors[0])
        expected = self.fixture_book1
        self.assertEqual(observed, expected)

    def tearDown(self):
        self.lib.close()
        shelve_files = glob.glob(self.lib_fn + "*")
        for fn in shelve_files:
            os.remove(fn)

if __name__ == "__main__":
    unittest.main()
