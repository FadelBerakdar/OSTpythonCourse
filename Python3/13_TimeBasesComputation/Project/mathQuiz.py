#!/usr/bin/env python
# By: Fadel Berakdar
# date: 29 Jan 2016

    Explain the difference among the terms Polymorphism, virtual function and
    overriding. By using example getting the area of shape for rectangle and
    triangle, write two different snippet codes to show the implementation of
    polymorphism and implementation of polymorphism and virtual function.
    Give example of output from both snipper codes.

    Polymorphism refers to the ability to associate many meanings to one
    function name by means of the late-binding mechanism. Thus, polymorphism,
    late binding, and virtual functions are really all the same topic.


import random
import datetime
import argparse


class Quiz:
    def __init__(self, number=5):
        self.number = number        # number of questions
        self.stats = []             # list contains a dictionary for each answer
        # no quiz object without quiz generator function called first
        # but I had to ignore that feature to just to ba able to run the tests
        #self._quiz_generator()

    def _quiz_generator(self):
        counter = 1
        number_of_questions = self.number
        # new variable to isolate self.number from any process

        while number_of_questions:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)

            before = datetime.datetime.now()
            answer = input("what is the sum of {} and {}? ".format(num1, num2))
            after = datetime.datetime.now()
            time = (after - before).seconds

            try:
                answer = int(answer)
                if answer == num1 + num2:
                    result = "right"

                else:
                    result = "wrong"

            except ValueError:
                result = "wrong"

            print("{} is {}!".format(answer, result))
            self.stats.append({"number": counter, "result": result,
                               "before": before, "after": after, "time": time})

            counter += 1
            number_of_questions -= 1

        return self.stats

    def average(self):
        sum_of_times = 0

        for dic in self.stats:
            sum_of_times += dic["time"]

        return sum_of_times/self.number

    def total_time(self):
        for dic in self.stats:
            if dic["number"] == 1:
                start_time = dic["before"]

            if dic["number"] == self.number:
                end_time = dic["after"]

        return (end_time - start_time).seconds

    def print_details(self):
        print("")
        for dic in self.stats:
            print("Question #{} took about {} seconds to complete and it "
                  "was {}.".format(dic["number"], dic["time"], dic["result"]))

        print("\nYou took {} seconds to finish the quiz".format(self.total_time()))
        print("Your average time was {} seconds per question".format(self.average()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-n',
                        '--number',
                        action='store',
                        dest='number',
                        type=int,
                        default=5,
                        help='Number of the questions.')

    args = parser.parse_args()

    pop_up_quiz = Quiz(args.number)
    pop_up_quiz._quiz_generator()
    pop_up_quiz.print_details()
