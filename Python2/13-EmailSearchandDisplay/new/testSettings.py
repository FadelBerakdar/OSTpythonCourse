import settings
import mysql.connector as msc
import unittest
from database import login_info
import datetime
import make_email

conn = msc.Connect(**login_info)
curs = conn.cursor()

class testSettings_functions(unittest.TestCase):
    def setUp(self):
        make_email.saveEmail(settings.RECIPIENTS, settings.STARTTIME, settings.DAYCOUNT)

    def testDataBaseRecords(self):
        curs.execute("SELECT COUNT(*) FROM Messages")
        result = curs.fetchone()[0]
        expected = len(settings.RECIPIENTS) * settings.DAYCOUNT
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

