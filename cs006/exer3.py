"""Exercise 1.3: List counting."""

x = [[1, 2], [3], [4, 5, 6, 7], [8, 9]]

evens = 0
odds = 0

for lst in x:
    for item in lst:
        if item % 2 == 0:
            evens += 1
        else:
            odds += 1

print("Number of evens:", evens)
print("Number of odds:", odds)
