"""Exercise 1.3: Rock-paper-scissors."""
import random


class Rock:

    def __init__(self):
        self.name = "rock"

    def __gt__(self, other):
        if other.name == "paper":
            return True
        else:
            return False

    def __lt__(self, other):
        if other.name == "paper":
            return True
        else:
            return False

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name


class Paper:

    def __init__(self):
        self.name = "paper"

    def __str__(self):
        return self.name

    def __gt__(self, other):
        if other.name == "rock":
            return True
        else:
            return False

    def __lt__(self, other):
        if other.name != "rock":
            return True
        else:
            return False

    def __eq__(self, other):
        return self.name == other.name


class Scissors:

    def __init__(self):
        self.name = "scissors"

    def __gt__(self, other):
        if other.name == "paper":
            return True
        else:
            return False

    def __lt__(self, other):
        if other.name != "paper":
            return True
        else:
            return False

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

hands = [Rock(), Paper(), Scissors()]

stats = {
    "wins": 0,
    "losses": 0,
    "ties": 0
}

for i in range(1, 10):
    player1 = random.choice(hands)
    player2 = random.choice(hands)

    print("Player 1", player1)
    print("Player 2", player2)
    print(player1 > player2)
    print(player1 < player2)
    print(player1 == player2)
    
    if player1 > player2:
        stats['wins'] += 1
    elif player1 < player2:
        stats['losses'] += 1
    else:
        stats['ties'] += 1

for key, value in stats.items():
    print(key.title(), value, sep="\t")