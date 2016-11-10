"""Exercise 1.2: Playing cards."""
from random import choice


suit = {
    "spades": 0,
    "hearts": 1,
    "diamonds": 2,
    "clubs": 3
}


class Card:

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __gt__(self, other):
        if self.number != other.number:
            return self.number > other.number
        else:
            return self.suit > other.suit


class Deck(list):

    def __init__(self):
        for i in range(1, 53):
            self.append(Card(i % 16, i // 16))

    def deal(self) -> Card:
        card = choice(self)
        self.remove(card)
        return card

    def empty(self):
        return (len(self) == 0)


class Hand:

    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0

    def receive(self, card: Card):
        self.card = card

    def __gt__(self, other):
        return self.card > other.card

h1 = Hand("Player 1")
h2 = Hand("Player 2")
deck = Deck()

while not deck.empty():
    h1.receive(deck.deal())
    h2.receive(deck.deal())

    if h1 > h2:
        h1.wins += 1
    else:
        h2.wins += 1

print(h1.wins)
print(h2.wins)
