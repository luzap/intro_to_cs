"""Exercise 1.2: FizzBuzz."""

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    if i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
