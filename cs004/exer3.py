# Exercise 3: Lists
import random

# Addition
original = range(1, 10)
sum_list = []
count = 0

for i in original:
    count += i
    sum_list.append(count)

print("Original:", list(original))
print("Cumulative:", sum_list)
print()

# Length
md_array = [[1, 2, 3], ['a', 'b', 'c', 'd'], [12.3, 2]]
count = 0

for i in md_array:
    count += len(i)
print("Original:", md_array)
print("Number of elements:", count)
print()

# Randomization
length = random.randint(1, 10)
lst = []

for i in range(length):
    lst.append(random.randint(0, 100))

print("List:", lst)
print("Sum of list:", sum(lst))
