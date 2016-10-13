"""Exercise 2.1: More list counting."""
import random

md_array = []

for i in range(random.randint(1, 5)):
    md_array.append([])
    for j in range(random.randint(1, 10)):
        md_array[i].append(random.randint(1, 20))

odds = 0
evens = 0

for lst in md_array:
    for item in lst:
        if item % 2 == 0:
            evens += 1
        else:
            odds += 1

print(md_array)
print("Evens:", evens)
print("Odds:", odds)
