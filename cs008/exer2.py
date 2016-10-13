"""Exercise 1.2: (More) Character counting"""

sentence = input("Enter a string: ")
breakdown = {}

for char in sentence:
    if char in breakdown.keys():
        breakdown[char] += 1
    else:
        breakdown[char] = 1

alphabetical = sorted(list(breakdown.keys()))


for i in alphabetical:
    print(i, '->', breakdown[i])
