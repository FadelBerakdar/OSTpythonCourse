#!/usr/bin/env python
# By: Fadel Berakdar
# date: 29 Jan 2016


import unittest
from mathQuiz import Quiz
import datetime

class TestMathQuiz(unittest.TestCase):

    def setUp(self):
        self.quiz = Quiz()
        self.quiz.stats = [{'after': datetime.datetime(2016, 1, 29, 17, 30, 57, 502771),
                            'before': datetime.datetime(2016, 1, 29, 17, 30, 51, 371351),
                            'result': 'wrong', 'number': 1, 'time': 6},
                           {'after': datetime.datetime(2016, 1, 29, 17, 31, 2, 54852),
                            'before': datetime.datetime(2016, 1, 29, 17, 30, 57, 502859),
                            'result': 'right', 'number': 2, 'time': 4},
                           {'after': datetime.datetime(2016, 1, 29, 17, 31, 10, 103209),
                            'before': datetime.datetime(2016, 1, 29, 17, 31, 2, 54905),
                            'result': 'wrong', 'number': 3, 'time': 8},
                           {'after': datetime.datetime(2016, 1, 29, 17, 31, 12, 79005),
                            'before': datetime.datetime(2016, 1, 29, 17, 31, 10, 103263),
                            'result': 'right', 'number': 4, 'time': 1},
                           {'after': datetime.datetime(2016, 1, 29, 17, 31, 14, 319681),
                            'before': datetime.datetime(2016, 1, 29, 17, 31, 12, 79075),
                            'result': 'right', 'number': 5, 'time': 2}]

    def test_average(self):
        self.assertEqual(self.quiz.average(), 4.2)
        self.assertEqual(self.quiz.total_time(), 22)

if __name__ == '__main__':
    unittest.main()
