"""Exercise 1.1: Slots."""
import random
import time

bet = 1

class SlotMachine:

    def __init__(self, credit):
        self.credit = credit
        self.wins = 0
        self.losses = 0

    def pull(self, bet):
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        c = random.randint(0, 10)

        if a == b and b == c:
            self.credit += (2 * bet)
            self.wins += 1
        else:
            self.credit -= bet
            self.losses += 1

slot = SlotMachine(100)

while slot.credit > 0:
    slot.pull(bet)


print("Won:", slot.wins)
print("Lost:", slot.losses)
