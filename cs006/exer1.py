"""Exercise 1.1: if-reduction."""

# Original
x = 6
if x < 2:
    print('a')
else:
    if x < 4:
        print('b')
    else:
        if x < 6:
            print('c')
        else:
            print('d')
print(x)

# Using elif
if x < 2:
    print("a")
elif x < 4:
    print("b")
elif x < 6:
    print("c")
else:
    print("d")

print(x)
