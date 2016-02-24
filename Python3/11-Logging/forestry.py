import logging                     # import the logging module


LOG_FILENAME = "forestry.log"
LOG_FORMAT = "%(asctime)s %(name)s:%(levelname)s:%(filename)s " \
             "function:%(funcName)s lin e:%(lineno)d %(message)s"

DEFAULT_LOG_LEVEL = "error"        # Default log level
LEVELS = {'debug': logging.DEBUG, 'info': logging.INFO,
          'warning': logging.WARNING, 'error': logging.ERROR,
          'critical': logging.CRITICAL}


def start_logging(file_name=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):

    "Start logging with given filename and level."
    logging.basicConfig(filename=file_name,
                        level=LEVELS[level],
                        format=LOG_FORMAT)
    # log a message
    logging.info('Starting up the forestry program')

"""

The basic API for a Tree is pretty simple. You create it by calling Tree(s)
wheres is a size code—one of "S," "M," "L," "XL," or "XXL".

Instances have a get_boards() method that you call to learn the number of boards
the tree can produce (1 for a size "S" tree, 5 for a size "XXL").
Trees represent themselves as "Tree: Size S" or similar.

The Lumberjack is not that much more complicated in its initial implementation.
Created by calling the class Lumberjack(), each instance starts out with no tree
Once a tree is assigned it can be cut down and converted into boards by calling
the Lumberjack's cut_down_tree() method. If this method is called when the
Lumberjack has no tree, a TypeError exception is raised.
"""


class Tree:
    """
    Represent a tree in a forest that can be converted into boards.
    """
    sizes = dict(S=1, M=2, L=3, XL=4, XXL=5)

    def __init__(self, size):
        """
        Initialize: inist that size is a valid code.
        :param size: the size of tree
        :return: None
        """
        if size not in self.sizes:
            msg = "Tree size must be one of: %s" % ",".join(self.sizes.keys())
            #  msg = "Tree size must be one of: {}".
            #  format(",".join(self.sizes.keys()))
            logging.error(msg)
            raise ValueError(msg)
        self.size = size
        logging.info('Instantiated a tree')

    """
    another approach to set the self.size attribute
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in ("S", "M", "L", "XL", "XXL"):
            self._size = value
        else:
            raise ValueError

    """

    def get_boards(self):
        logging.info('tree.get_boards method called')
        return self.sizes[self.size]

    def __str__(self):
        """
        Render as a string.
        :return: readable string
        """
        return "Tree: Size {}".format(self.size)



class Lumberjack:
    """
    Represent a lumberjack who can cut down trees.
    """
    def __init__(self):
        """
        Initialize: starts with no tree.
        :return: None
        """
        self.tree = None
        logging.info('Instantiated a Lumberjack')

    def cut_down_tree(self):
        """
        Convert tree to boards and go back to not having a tree.
        :return:boards
        """
        if not self.tree:
            msg = "Cannot cut_down_tree(): Lumberjack has no tree!"
            logging.error(msg)
            raise TypeError
        boards = self.tree.get_boards()
        self.tree = None
        logging.info('Lumberjack.tree cut down')
        return boards

"""

if __name__ == "__main__":
    "Demonstrate basic usage."
    john = Lumberjack()
    john.tree = Tree("XXL")
    if john.cut_down_tree() != 5:
        print("Error: XXL tree should yield 5 boards")
"""



