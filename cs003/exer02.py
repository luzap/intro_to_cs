"""Exercise 2: Computer Names."""

full_name = input("Please input your full name: ")
full_name = full_name.lower().split(" ")

computer_name = full_name[0][0] + full_name[-1][:5]
print("Your computer name is:", computer_name)
