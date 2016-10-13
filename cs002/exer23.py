"""Exercise 2.3:  Madlibs"""

adjective_1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective_2 = input("Enter another adjective: ")
number = input("Enter a number: ")

print("The {} knight ventured on a {} quest.\nHe found {} masssive {}(s).".format(
    adjective_1, adjective_2, number, noun))
