"""Exercise 1.2: Timed Q/A."""
import time
import random


class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask(self):
        return int(input(self.question + "? "))


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
        print("\nResults")
        for watch in self.watches:
            print(self.watches.index(watch) + 1, round(watch, 3), sep="\t")
        print("Average time:", round(sum(self.watches)/len(self.watches), 3))

timer = Timer()

rounds = int(input("How many rounds of practice would you like? "))

for i in range(0, rounds):
    operation = random.randint(0, 4)
    a = random.randint(1, 5)
    b = random.randint(1, 5)

    if operation == 0:
        result = a + b
        operator = " + "
    elif operation == 1:
        result = a - b
        operator = " - "
    elif operation == 2:
        result = a * b
        operator = " * "
    else:
        result = a // b
        operator = " // "

    question = Question(str(a) + operator + str(b), result)
    timer.start()
    answer = question.ask()
    while answer != question.answer:
        answer = question.ask()
    timer.stop()

timer.results()
