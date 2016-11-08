"""Particles."""


class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Pair(self.x + other.x, self.y + other.y)


class Particle:

    def __init__(self, position: Pair, velocity: Pair, identifier: str) -> None:
        self.position = position
        self.velocity = velocity
        self.identifier = identifier

    def move(self):
        self.x += self.v_x
        self.y += self.v_y


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
                board[i].append(layout.marker.water)
        return board

    def print_board(self) -> None:
        print("+-" * len(row) + "+")
        for row in self.board:
            print("|" + "|".join(row), end="|\n")
            print("+-" * len(row) + "+")

    def update(self, particle: Particle) -> None:
        board[particle.position.x][particle.position.y] = particle.identifier



