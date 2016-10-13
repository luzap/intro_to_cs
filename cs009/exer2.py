"""Exercise 1.2: Persistent phonebook."""

file = "phonebook.txt"

with open(file, "a") as fhandle:
    while True:
        name = input("Enter your friend's name: ")
        if name == "" or name == " ":
            break
        else:
            phone = input("Enter {}'s phone number: ".format(name))
            if len(phone) == 0:
                phone = "blank"
            fhandle.write(name + "," + phone + "\n")

phonebook = {}
with open(file, "r+") as fhandle:
    file = fhandle.read().split("\n")[:-1]
    for item in file:
        lst = item.split(",")
        if lst[0] not in phonebook.keys():
            phonebook[lst[0]] = lst[1]

while True:
    name = input("Who are you looking for? ")
    if name == "" or name == " ":
        break
    elif name in phonebook.keys():
        print(name, phonebook[name])
    else:
        print("Sorry, {} is not listed. Please try again.".format(name))
