import unittest
import re


p1 = """While I was at the store I tried to call 555-123-4567 on my mobile
but accidentally called 555-754-4321. The person on the line redirected me to
999-999-9999 which I don't think is a real number. Neither is 000-000-0000 or
55 5-555-0000. Well, I will try (555) 123-4567 again now."""
p2 = "I live in Washington, DC 20002. Where do you live?"
p3 = "I live in Falls Church, VA 20188. And you?"


def city_search(string):
    regex = r"[A-Z][a-z]+(\s[A-Z][a-z]+)*,\s[A-Z]{2}\s\d{5}"
    search = re.search(regex, string)
    if search:
        return search.group()


class TestCitySearch(unittest.TestCase):

    def test_city_search(self):
        self.assertEqual("Washington, DC 20002", city_search(p2))
        self.assertEqual("Falls Church, VA 20188", city_search(p3))

    def test_city_failure(self):
        self.assertIsNone(city_search(p1))

if __name__ == "__main__":
    unittest.main()
