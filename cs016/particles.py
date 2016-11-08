"""Particles: main event + additional practice."""
import os
import time
from random import randint


class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Pair(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "{},{}".format(self.x, self.y)


class Particle:

    def __init__(self, position: Pair, velocity: Pair, identifier: str) -> None:
        self.position = position
        self.velocity = velocity
        self.identifier = identifier

    def move(self):
        self.position += self.velocity

    def __str__(self):
        return "{} at {}, {}".format(self.identifier, self.position.x,
                                     self.position.y)


class Board:

    def __init__(self, x: int, y: int, filler=" "):
        # The next two rows ensure the extensibility of the gameboard
        self.columns = y
        self.rows = x
        self.filler = filler

        self.board = self.__create_board()

    def __create_board(self) -> list:
        """Create a empty board."""
        board = []
        for i in range(self.rows):
            board.append([])
            for j in range(self.columns):
                board[i].append(self.filler)
        return board

    def __str__(self) -> None:
        board = ""
        board += "+ - " * len(self.board[0]) + "+\n"
        for row in self.board:
            board += "| " + " | ".join(row) + " |\n" + "+ - " * len(row) + "+\n"
        return board

    def update(self, particle: Particle) -> None:
        self.board[particle.position.x % self.rows][
            particle.position.y % self.columns] = particle.identifier


columns = rows = 20

particles = []

for i in range(10):
    x = randint(0, rows)
    y = randint(0, columns)
    v_x = randint(-1, 1)
    v_y = randint(-1, 1)
    particles.append(Particle(Pair(x, y), Pair(
        v_x, v_y), chr(randint(97, 122))))


while(True):
    board = Board(rows, columns)
    for part in particles:
        board.update(part)
    os.system('cls')
    print(board)
    for part in particles:
        part.move()
    for index in range(len(particles)):
        particles[index].velocity = Pair(randint(-1, 1), randint(-1, 1))
    time.sleep(2 ** -3)
