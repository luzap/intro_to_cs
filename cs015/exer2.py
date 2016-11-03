"""Exercise 1.2: Timed Q/A."""
import time


class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask(self):
        return input(self.question + "?")


class Timer:

    def __init__(self):
        self.watches = []
        self.begin = 0

    def start(self):
        self.begin = time.time()

    def stop(self):
        self.watches.append(time.time() - self.begin)
        self.begin = 0

    def results(self):
        for watch in watches:
            print(self.watches.index(watch), watch, sep="\t")
