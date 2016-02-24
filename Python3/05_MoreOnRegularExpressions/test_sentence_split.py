import re
import unittest


text = "Hello! My name is Steve. What is yours? I hope you enjoyed this class!"


def sentence_split(string):
    pattern = r"[?.!]\s+"
    return re.split(pattern, string)

class TestSentenceSplit(unittest.TestCase):

    def test_split_sentence(self):
        self.assertEqual(len(sentence_split(text)), 4)

if __name__ == "__main__":
    unittest.main()
