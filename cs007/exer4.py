"""Exercise 2.1: Horse racing."""
import time
import random
from sys import platform

if platform in ["linux", "linux2", "darwin"]:
    marker = u"\u26F7"
else:
    marker = "*"

race_schedule = [random.randint(1, 40) for i in range(10)]

race_map = []
for i in range(max(race_schedule)):
    race_map.append([" " for _ in range(len(race_schedule))])

for level in range(max(race_schedule)):
    for pos in range(len(race_schedule)):
        if race_schedule[pos] >= 1:
            race_map[level][pos] = marker
            race_schedule[pos] -= 1
print(flush=True)

print("+" + "-+" * len(race_schedule))
for row in race_map:
    print("|", end="")
    for horse in row:
        print(horse + "|", end="", flush=True)
    time.sleep(0.1)
    print("")
