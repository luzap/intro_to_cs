import os

import pytmx

from constants import MAP_ROOT


def load_map(map_name):
    """Load a specific map and returns a TiledMap object."""
    map_loc = os.path.join(MAP_ROOT, map_name)
    map = pytmx.load_map(map_loc)
    return map
