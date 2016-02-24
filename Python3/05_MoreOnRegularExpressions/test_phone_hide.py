import re
import unittest

text = """While I was at the store I tried to call 555-123-4567 on my mobile
but accidentally called 555-754-4321. The person on the line redirected me to
999-999-9999 which I don't think is a real number. Neither is 000-000-0000 or
555-555-0000. Well, I will try (555) 123-4567 again now."""


def phone_hide(string):
    pattern = r"\d{3}-\d{4}"
    return re.subn(pattern, "XXX-XXXX", string)

print(phone_hide(text))

class TestHidePhone(unittest.TestCase):

    def test_phone(self):
        response, count = phone_hide(text)
        self.assertFalse("555-123-4567" in response)
        self.assertTrue("555-XXX-XXXX" in response)
        self.assertTrue("(555) XXX-XXXX" in response)
        self.assertEqual(6, count)
        
if __name__ == "__maine__":
    unittest.main()
