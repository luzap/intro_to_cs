"""Battleships

Author: Lukas Zapolskas

In terms of formatting, the code should mostly follow the guidelines
set forth by the Python Enhancement Proposals (PEP).

"""
# A module that contains Python operators as functions, for usage with
# higher order functions
import operator

import layout


# Needed to call this multiple times, so moved it to a function
def add_lists(list1, list2):
    """Sum up lists by element."""
    return list(map(operator.add, list1, list2))


# Class definition of GBoard
class GBoard:
    """Class representing the main game board. This way, operations on ships
    can now be represented by class methods, allowing to separate the user
    interaction and the data processing. Also allows for "private" methods
    and variables (kind of but not really)."""

    def __init__(self):
        # The next two rows ensure the extensibility of the gameboard
        self.columns = layout.columns
        self.rows = layout.rows

        # Positions of ships will be recorded with Cartesian coordinates,
        # where the axes start at the top left corner of the board and
        # the positive y direction is inverted.
        self.ships = self.__gen_coords()
        self.misses = []
        self.hits = []

        self.__populate()

    def __gen_coords(self):  # Private method, only called by object
        """Based on the endpoints given, generate the coordinates
        for all of the boats."""
        ship_coords = []
        for endpoints in layout.ships:
            dx = endpoints[1][0] - endpoints[0][0]
            dy = endpoints[1][1] - endpoints[0][1]
            if dx != 0 and dy == 0:
                for i in range(dx + 1):
                    ship_coords.append(add_lists(endpoints[0], [i, 0]))
            elif dx == 0 and dy != 0:
                for i in range(dy + 1):
                    ship_coords.append(add_lists(endpoints[0], [0, i]))
        return ship_coords

    def __create_board(self):
        """Create a empty board."""
        board = []
        for i in range(self.rows):
            board.append([])
            for j in range(self.columns):
                board[i].append(layout.marker.water)
        return board

    def __populate(self, ships=layout.competition):
        """Draw characters on the board."""
        self.board = self.__create_board()
        for coords in self.hits:
            self.board[coords[0]][coords[1]] = layout.marker.hit
        for coords in self.misses:
            self.board[coords[0]][coords[1]] = layout.marker.miss

        if not ships:
            for coords in self.ships:
                self.board[coords[0]][coords[1]] = layout.marker.ship

    def __shift(self):
        """Shift every block in a specific direction based upon current."""
        current = layout.current()
        # .format is used to nicely insert the values for current into
        # the string
        print("Current last turn was: {}, {}".format(current[0], current[1]))
        for coords_set in [self.ships, self.hits, self.misses]:
            for item in range(len(coords_set)):
                # Adds current to coordinates
                coords_set[item] = add_lists(coords_set[item], current)
                # Takes care of the wrap around effect, since
                # 1 % 10 = 1, 10 % 10 = 0 and -1 % 10 = 9
                coords_set[item] = [coords_set[item][0] % layout.columns,
                                    coords_set[item][1] % layout.rows]

    # TODO Make guidelines
    def __pprint_board(self):
        """Pretty print of the board. Name inspired by the pprint module."""
        # The \ is used to break up one line into several for ease of reading
        separator = layout.board.corner + \
            (layout.board.top + layout.board.corner) * self.columns
        print(separator)
        for row in self.board:
            # layout.board.side.join joins the characters around the given
            # string, eliminating the need for a nested for-loop
            print(layout.board.side + layout.board.side.join(row),
                  end=(layout.board.side + "\n"))
            print(separator)

    # TODO Write comment on the annotation
    def guess(self, coords: "a coordinate pair (x,y)") -> bool:
        """Check user guesses against ship coordinates."""
        if coords in self.ships:
            self.board[coords[0]][coords[1]] = layout.marker.hit
            self.ships.remove(coords)
            self.hits.append(coords)
            return True
        else:
            self.board[coords[0]][coords[1]] = layout.marker.miss
            if coords not in self.misses:
                self.misses.append(coords)
            if coords in self.hits:
                print("Seriously? It's down already!")
            return False

    def loop(self):
        """Calling the functions separately ensures that the order of
        operations is correct. It is also simpler to switch them around
        for testing purposes."""
        self.__populate()
        self.__pprint_board()
        self.__shift()


class UserInterface:
    """Class that handles user interaction."""

    def __init__(self):
        self.gboard = GBoard()  # Instance of the gameboard class
        self.hits = 0
        self.misses = 0  # Note that values not on board are still counted

        self.__instructions()  # Runs once, upon initialization

        self.__mainloop()  # Runs the mainloop while the game is running

    def __instructions(self):
        """Introduce the game upon launch."""
        print("Welcome to Battleship: Rip current edition!\n"
              "This is a modification of the traditional Battleship.\n"
              "Keep in mind that the ships are not stationary!\n"
              "We're assuming you really know how to aim, so current \n"
              "is calculated after the shot.\n"
              "Also, the coordinates start from zero, not from one.\n"
              )  # print can take multiple strings without operators
        # in this manner

    def __user_input(self):
        """Ask for user input and process it."""
        try:
            str_coords = input("What's your guess (x,y)? ")
            coord = [int(x.strip()) for x in str_coords.split(",")][::-1]
            hit = self.gboard.guess(coord)  # Returns a True or False based
            return hit                      # on the coordinates given
        except (ValueError, IndexError):
            print("Not sure those were numbers. \n"
                  "Or you're just really bad at this. Try again!")
            return None

    def __scoreboard(self):
        """Display game statistics."""
        print("Hits:", self.hits)
        print("Misses:", self.misses)
        print("Total guesses:", self.hits + self.misses, end="\n\n")

    def __mainloop(self):
        """Run while all of the ships haven't been shot down."""
        while len(self.gboard.ships) != 0:
            success = self.__user_input()
            if success is True:
                print("Success! You hit a ship!")
                self.hits += 1
            else:
                print("Maybe next time!")
                self.misses += 1
            self.gboard.loop()
            self.__scoreboard()
        print("Victory!")
        guesses = self.hits + self.misses
        # The score is rounded up to 1 decimal place
        print("Score:", round((self.hits / guesses) * 100, 1))


if __name__ == '__main__':  # Runs if the script is launched by itself
    game = UserInterface()  # as opposed to being used as a module
