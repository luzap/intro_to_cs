"""Exercise 1.2: Fun with string output."""

listOfLists = [['a', 'b', 'c'],
               ['d', 'e', 'f'],
               ['g', 'h', 'i']]
element = 1
for list in listOfLists:
    for item in list:
        print("." * element + item)
        element += 2

print("")

for list in listOfLists:
    for item in list:
        print((2 * listOfLists.index(list) + 1) * "." + item)
