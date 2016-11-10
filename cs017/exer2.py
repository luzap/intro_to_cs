"""Exercise 1.2: Playing cards."""
from random import choice


suit = {
    "spades": 0,
    "hearts": 1
    "diamonds": 2
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


class Hand:

    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0

    def receive(self, card: Card):
        self.card = card

    def __gt__(self, other):
        return self.card > other.card
