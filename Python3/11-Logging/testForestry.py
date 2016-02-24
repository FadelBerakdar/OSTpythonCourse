



import unittest
from forestry import Lumberjack, Tree, start_logging


sizes = (("S", 1), ("M", 2), ("L", 3), ("XL", 4), ("XXL", 5))


class TestTree(unittest.TestCase):
    def test_lumber(self):
        for code, boards in sizes:
            tree = Tree(code)
            self.assertEqual(boards, tree.get_boards())

    def test_string(self):
        tree = Tree("L")
        self.assertEqual(str(tree), "Tree: Size L")

    def test_exception(self):
        self.assertRaises(ValueError, Tree, "parrot")
        self.assertRaises(TypeError, Lumberjack().cut_down_tree)


class TestLumberjack(unittest.TestCase):
    def test_lumberjack(self):
        for code, boards in sizes:
            tree = Tree(code)
            graham = Lumberjack()
            self.assertIsNone(graham.tree)
            graham.tree = tree
            brds = graham.cut_down_tree()
            self.assertIsNone(graham.tree)
            self.assertEqual(boards, brds)

if __name__ == "__main__":
    start_logging(level="error")
