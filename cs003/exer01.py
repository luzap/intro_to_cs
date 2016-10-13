# Exercise 1: Pony Stash Toek
x = "pony stash token"

print("First letter:", x[0])
print("Last letter:", x[-1])
print("Without first or last letters:", x[1:len(x)-1])
print("Every other letter:", x[::2])

addition = 'tony'
new_x = x[:5] + addition + x[len(addition) + 6:]
print("After replacement:", new_x)
