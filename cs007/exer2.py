"""Exercise 1.2: Friend book."""

friends = []

while True:
    name = input("Enter your friend's name or `stop` to finish: ")
    if name == 'stop':
        break
    else:
        friends.append(name)

print("You have {} friends. They are:".format(len(friends)))
for friend in friends:
    if friends.index(friend) == len(friends) - 2:
        print(friend, end=", and\n")
    elif friends.index(friend) == len(friends) - 1:
        print(friend)
    else:
        print(friend, end=",\n")
