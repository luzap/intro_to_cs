"""components.py:

The basic building blocks of entities in ECS.
"""

import constants


class Renderable:
    """Note that Renderable and Image are two different components.
    They were intended to be one, but it didn't work out for some
    reason to do with ctypes errors on Windows."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Velocity:
    """Component that separates which entity is the player."""

    def __init__(self, vx, vy):
        self.x = vx
        self.y = vy


class Image:

    def __init__(self, filename):
        self.filename = filename

        # Since the asset is a square with known dimensions
        # it's simpler to use the constant than get the
        # properties from a temporarily loaded image and then
        self.width = constants.BLOCKSIZE
        self.height = constants.BLOCKSIZE


class Color:
    """Used to color the one asset this game has."""

    def __init__(self, r, g, b):
        self.values = (r, g, b)


class End:

    def __init__(self, is_end=False):
        self.is_end = is_end