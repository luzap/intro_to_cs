"""Exercise 2.1 Pyramid."""
stars = int(input("How many stars?"))

for i in range(1, stars + 1):
    print(" " * (stars - i) + (" *" * i))
