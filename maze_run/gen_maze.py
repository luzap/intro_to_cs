import numpy as np
import random
from random import shuffle, randrange


class Maze:

    @staticmethod
    def make_maze(width, height):
        # Creating the maze
        maze = np.zeros((width + 2, height + 2), dtype=np.int8)
        maze.fill(1)  # Fill the maze with walls
        return maze

    @staticmethod
    # TODO Make randomized depth-first search => consider making tree
    # TODO Please not recursive
    def _make_path(self, x, y):
        pass


if __name__ == '__main__':
    maze = Maze.make_maze(10, 10)
    print(maze)
