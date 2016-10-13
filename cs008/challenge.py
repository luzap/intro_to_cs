phone_dir = {}

while True:
    name = input("Enter your friend's name: ")
    if name == " ":
        break
    phone_num = input("Enter {}'s phone number".format(name))
    phone_dir[name] = int(phone_num)

while True:
    name = input("What's your name? ")
    if name in phone_dir.keys():
        print(phone_dir[name])
    else:
        print("Sorry, you're not in the directory!")
        break
