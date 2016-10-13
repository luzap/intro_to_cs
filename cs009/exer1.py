"""Exercise 1.1: Reading and writing skills."""
import random
from functools import reduce

file = "numbers.txt"

with open(file, mode="w+") as fhandle:
    for i in range(10):
        fhandle.write(str(random.randint(1, 10)) + "\n")

with open(file, mode="r+") as fhandle:
    file = fhandle.read().split("\n")[:-1]
    sum = reduce(lambda x, y: int(x) + int(y), file)
print(sum)
