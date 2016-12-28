"""processors.py:

The main body of the ECS. Processors act on entities that have
a specific subset of components, and change the values of those
components. These are responsible for game mechanics.

TODO:
- Score system
- Unloading + reloading system
"""

import pyglet
import esper
import database
import constants
from components import *


class MovementProcessor(esper.Processor):
    """Processor that allows the entity with Velocity to move
    (the player only) and checks for the victory condition."""

    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.end_coords = None

    def process(self, dt: "delta time"):
        """Move every entity with the Velocity component (just the player,
        though could be extended for multiple)."""
        for ent, (vel, rend, img) in self.scene.world.get_components(Velocity,
                                                                     Renderable,
                                                                     Image):
            # Since movement is done in discrete intervals, it is simple
            # to check whether or not the player is in one of those positions

            # Creates all the "forbidden" positions for the player
            coords = [(spr.x, spr.y)
                      for spr in self.scene.assets.values()]
            if self.end_coords is not None:
                if self.end_coords in coords:
                    coords.remove(self.end_coords)

            # Boolean on whether or not the player can be moved in the indended
            # direction
            movable = (rend.x + vel.x, rend.y + vel.y) not in coords
            rend.x += vel.x * movable
            rend.y += vel.y * movable

            # The sprite's position has to be updated as well, for rendering
            # purposes
            self.scene.assets[ent].x = rend.x
            self.scene.assets[ent].y = rend.y
            vel.x, vel.y = 0, 0

            if (rend.x, rend.y) == self.end_coords:
                self.scene.render_proc.clean()
                self.scene.next_maze()


class RenderProcessor(esper.Processor):
    """Processor that controls visual elements, their rendering and deletion."""

    def __init__(self, scene):
        self.scene = scene
        self.image = None  # Loaded once due to frequency of use
        # FPS for debugging
        if constants.DEBUG:
            self.fps_display = pyglet.clock.ClockDisplay()

    def gen_file_listing(self):
        """Handle all of the image assets, their conversions to textures,
        and their addition to the batch, from which they are rendered."""
        for ent, (img, rend, col) in self.scene.world.get_components(Image,
                                                                     Renderable,
                                                                     Color):
            if img is not None:
                img = pyglet.image.load(img.filename)
            if ent not in self.scene.assets.keys():

                # Determines whether to render to foreground or background
                which_group = self.scene.foreground if self.world.has_component(
                    ent, Velocity) else self.scene.background
                self.scene.assets[ent] = pyglet.sprite.Sprite(
                    img, rend.x, rend.y, batch=self.scene.batch,
                    group=which_group)  # Assets are associated with entities
                # Morphing color values through OpenGL allows
                # the use of only one image asset
                self.scene.assets[ent].color = col.values

    def clean(self):
        """Remove old assets from the current batch."""
        self.scene.world.clear_database()
        self.scene.assets = {}
        self.scene.batch = pyglet.graphics.Batch()

    def process(self, dt: "delta time"):
        """Blits everything to screen and generates the file listing if not available."""
        if not len(self.scene.assets):
            self.gen_file_listing()

        self.scene.window.clear()

        # Background texture via direct OpenGL call
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                     [0, 1, 2, 0, 2, 3],
                                     ('v2i', (0, 0, constants.WIDTH, 0, constants.WIDTH,
                                              constants.HEIGHT, 0, constants.WIDTH)),
                                     ('c3B', (255, 255, 0, 255,
                                              255, 0, 0, 255, 0, 0, 255, 0))
                                     )
        self.scene.batch.draw()
        if constants.DEBUG:
            self.fps_display.draw()


class TimeProcessor(esper.Processor):
    """Keeping track of the time taken for the level. Used as part of the score
    mechanic, and the loss mechanic. If more time is taken than necessary,
    show that the player lost, ask for player name and return to Menu."""

    def __init__(self, scene):
        self.scene = scene
        self.running = True
        self.label = pyglet.text.Label("",
                                       font_size=16,
                                       x=constants.WIDTH // 2,
                                       y=constants.HEIGHT * 0.90,
                                       batch=self.scene.batch,
                                       group=self.scene.background,
                                       color=(0, 0, 0, 255),
                                       anchor_x="center",
                                       anchor_y="center")

        # The divisor applied to the time given by each successive level
        # Otherwise, when the size of the maze is fully developed, it's
        # no longer as fun, as a lot of mistakes can be compensated for
        # using saved up time.
        self.time_reduction = iter(range(1, 500))
        self.max_time = 1
        self.time = 0

        self.new_level()

    def process(self, dt: "delta time"):
        if self.running:
            self.time += dt
            self.label.text = str(
                round(self.max_time - self.time, 2))
        if self.time > self.max_time:
            self.scene.end()

    def new_level(self, add_time=0):
        self.label = pyglet.text.Label("",
                                       font_size=16,
                                       x=constants.WIDTH // 2,
                                       y=constants.HEIGHT * 0.90,
                                       batch=self.scene.batch,
                                       group=self.scene.background,
                                       color=(0, 0, 0, 255),
                                       anchor_x="center",
                                       anchor_y="center")

        # Since the end of iteration brings about an error, still worth
        # having a try-except block, even if the chances of a player 
        # getting to that point are very low.
        try:
            divisor = 1 if add_time < 25 else next(self.time_reduction)
        except StopIteration:
            divisor = 1

        # Maximum time increases for a while, and then starts decreasing,
        # making the player rely on time they saved up
        self.max_time = ((self.max_time - self.time) // 5 +
                         add_time / divisor)
        self.time = 0

    def pause(self) -> None:
        """For pause screens."""
        self.running = False

    def unpause(self) -> None:
        self.running = True