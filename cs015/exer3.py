"""Exercise 1.3: Rock-paper-scissors."""


class Rock:

    def __gt__(self, other):
        if other.name != "paper":
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
