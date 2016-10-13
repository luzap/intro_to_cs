"""Exercise 4: Dice game."""
import random

outcomes = ['one', 'two', 'three', 'four', 'five', 'six']
bool_outcomes = ['wrong', 'right']

guess = int(input("What is your guess? "))

value = random.randint(1, 6)

print("Your guess was", bool_outcomes[guess == value])
print("The value was", outcomes[value - 1])


side_of_die = "+------+"
middle_of_die = "{}".format(outcomes[value - 1]).center(len(side_of_die) - 2)

print(side_of_die)
print("+" + middle_of_die + "+")
print(side_of_die)
