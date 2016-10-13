# Exercise 2.4: Interactive addition

num_1 = input("Enter the first number: ").rstrip().lstrip()
num_2 = input("Enter the second number: ").rstrip().lstrip()
num_3 = input("Enter the third number: ").rstrip().lstrip()
num_4 = input("Enter the fourth number: ").rstrip().lstrip()

# First concatenates the string, then adds
concat_num_1 = int(num_1 + num_2)
concat_num_2 = int(num_3 + num_4)

print(concat_num_1 + concat_num_2)
