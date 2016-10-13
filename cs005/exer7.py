"""1.7 Even or odd."""

num = int(input("What number would you like to check?").strip())

if num % 2 == 0:
    print("{} is even".format(num))
else:
    print("{} is odd".format(num))
