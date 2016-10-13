import esper

from components.movement import Velocity
from components.rendering import Renderable


class MovementProcessor(esper.Processor):
    """Takes Entities and iterates over them, adding speed."""

    def __init__(self, minx, maxx, miny, maxy):
        """Define bounds of screen."""
        super().__init__()
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def process(self):
        """Apply necessary modifications to dynamic objects."""
        for ent, (vel, rend) in self.world.get_components(Velocity,
                                                          Renderable):
            rend.x += vel.v_x
            rend.y += vel.v_y

            # The following block checks the bounds of the screen
            # and does not allow an object to move past
            rend.x = max(self.minx, rend.x)
            rend.y = max(self.miny, rend.y)
            rend.x = min(self.maxx - rend.height, rend.x)
            rend.y = min(self.maxy - rend.width, rend.y)
