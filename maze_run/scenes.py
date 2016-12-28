"""scenes.py:

Scenes are going to be the primary mechanism through which various
instances of the game will be launched.

Each Scene has to implement a constructor, and three methods:
- on_key_pressed
- paused
- unpaused

These methods are necessary for the Window instance to
be able to pass on keyboard and mouse events to the separate
scenes.

The Highscore and Menu scenes are implemented using the
pyglet-gui library. As such, their construction is somewhat
different from that of the central game scene.

Image assets are loaded and processed in batches, as blitting
them to the screen one by one quickly becomes problematic.
Note that having 100+ image assets loaded into one batch also
drops the framerate quite dramatically. The current workaround
is to have mazes that have fewer than 900 entries (the plan
was to max out at a smaller number, but for testing purposes,
big mazes were generated). This could be theoretically
circumvented by stitching logical blocks together, but
that would come at the cost of the current collision system,
which is more vital to the game than large mazes.


TODO
- Generation of new levels (not sure what's the best
way of doing this)
"""
# Abstract Base Class - part of the standard library
import os
import random
import collections
from abc import ABC, abstractmethod

import esper
import pyglet
import numpy as np
from pyglet.window import key

# These imports have to be done this way, otherwise they don't work
# for some reason
from pyglet_gui.theme import Theme
from pyglet_gui.manager import Manager
from pyglet_gui.document import Document
from pyglet_gui.containers import VerticalContainer
from ui_elements import SceneButton, QuitButton

import prim
import processors
import components
from constants import *
from database import ScoresDB


class Scene(ABC):

    @abstractmethod
    def __init__(self, background_sound):
        """Abstract __init__ method that needs to be overridden by subclasses.
        """
        # Each scene will have its own world instance, and will load
        # systems depending on which ones are necessary, and will
        # create different entities based on purpose
        self.world = esper.World()

        # Asset management
        self.batch = pyglet.graphics.Batch()
        self.assets = collections.OrderedDict()
        # Logical rendering groups with associated priorities
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)

        # Sound loading. Since each of the Scenes has the same one
        # track in the background, passing it to the superclass and
        # using the inherited Player object reduces code reuse.
        # Given more time to look into it, might be better off in the
        # Window instance, with each Scene then controlling the sound queue
        tune = pyglet.media.load(os.path.join(SOUNDASSETS, background_sound))
        self.pl = pyglet.media.Player()
        self.looper = pyglet.media.SourceGroup(tune.audio_format, None)
        self.looper.loop = True

        self.looper.queue(tune)
        self.pl.queue(self.looper)

        self.pl.volume = 1.0

    @abstractmethod
    def on_key_pressed(self, sym, mod):
        """Determines the events happening in the Scene when a button is
        pressed down."""
        pass

    @abstractmethod
    def paused(self):
        """Determines what to do when focus is lost."""
        pass

    @abstractmethod
    def unpaused(self):
        """Determines what to do when focus is restored."""
        pass


# TODO Make component presets in constants.py
class Menu(Scene):

    def __init__(self, window):
        super().__init__("menu.mp3")
        self.window = window
        self.window.set_mouse_visible(True)

        # Load menu background music
        tune = pyglet.media.load(os.path.join(SOUNDASSETS, "menu.mp3"))
        self.looper = pyglet.media.SourceGroup(tune.audio_format, None)
        self.looper.loop = True

        self.looper.queue(tune)
        self.pl.queue(self.looper)
        self.pl.play()

        pyglet.text.Label(text="Can you escape the maze?", font_size=32,
                          x=WIDTH / 2, y=HEIGHT * 0.75, anchor_x="center",
                          anchor_y="center", batch=self.batch)

        # Simple syntax for dictionary joining
        theme = Theme({**GUIPRESET, **BUTTON}, resources_path=THEMERES)
        Manager(VerticalContainer([SceneButton(self.window, 2, label="Play"),
                                   SceneButton(self.window, 1,
                                               label="High Scores"),
                                   QuitButton("Quit")]),
                window=self.window,
                batch=self.batch,
                theme=theme)

        rend_proc = processors.RenderProcessor(self)

        self.world.add_processor(rend_proc)

    def on_key_pressed(self, sym, mod):
        pass

    def on_key_released(self, sym, mod):
        pass

    def paused(self):
        self.pl.pause()

    def unpaused(self):
        self.pl.play()


# TODO HTML label and table of some sort (can be made of button objects)
# TODO Switching back to Menu Scene
class HighScores(Scene):
    """Shows the glorious progress of the players that came before."""

    def __init__(self, window):
        super().__init__("menu.mp3")
        self.db = ScoresDB()
        self.window = window

        # Play the music loaded in the superclass
        self.pl.play()

        # The RenderProcessor has all of the rendering functionality,
        # including the background. It's the only system that HAS to
        # be included in every Scene.
        self.rend_proc = processors.RenderProcessor(self)
        self.world.add_processor(self.rend_proc)

        # GUI theme as part of the pyglet-gui module
        theme = Theme({**GUIPRESET, **SCROLL}, resources_path=THEMERES)

        # Obtain scores in correct order and style them using simple HTML
        scores = self.db.get_scores()
        doc = '''<center><h1>High Scores</h1>'''
        place = 1
        for score in scores:
            doc += str(place) + ". <b>" + score[0] + \
                "</b> with a score of " + str(score[1]) + "<br>"
            place += 1
        doc += "</center>"
        document = pyglet.text.decode_html(doc)

        # Set up a Manager
        Manager(Document(document, width=WIDTH, height=HEIGHT, is_fixed_size=True),
                window=self.window, batch=self.batch, theme=theme)

    def on_key_pressed(self, sym, mod):
        """Brings back to the menu screen."""
        self.rend_proc.clean()
        self.window.change_scene(0)

    def on_key_released(self, sym, mod):
        """Not necessary, but has to be overridden in order for the
        abstract class not to throw an error."""
        pass

    def paused(self):
        """Pauses music playback."""
        self.pl.pause()

    def unpaused(self):
        """Pauses music playback."""
        self.pl.play()


class Game(Scene):
    """Generates and stores the mazes, responsible for calculating score,
    and keeping track of time."""

    def __init__(self, window):
        super().__init__("game.mp3")
        self.window = window
        self.window.set_mouse_visible(False)

        self.max_maze_size = 25  # The max value for one of the sides
        self.maze_size = 10  # Starting value, to get the player used to it
        # The initial plan was to use an iterator, but considering there
        # is no method or function to check if the next value exists,
        # decided against it.

        # Used for scoring purposes
        self.step_counter = 0
        self.score = 0

        # Play scene sound
        self.pl.play()

        # Creation of processors in case manual interaction is needed
        self.render_proc = processors.RenderProcessor(self)
        self.movement_proc = processors.MovementProcessor(self)
        self.time_proc = processors.TimeProcessor(self)

        # Adding the processors to the World instance
        # The priority is an additional measure in making sure
        # they are loaded in the exact order speecified,
        # though arranging them in that order would have
        # probably worked fine.
        self.world.add_processor(self.render_proc, priority=2)
        self.world.add_processor(self.movement_proc, priority=1)
        self.world.add_processor(self.time_proc, priority=0)

        # EntityFactory for easy entity creation
        self.ent_factory = EntityFactory(self.world)

        self.next_maze()

    def on_key_pressed(self, sym, mod):
        """Basic movement model."""
        if sym in (key.UP, key.W):
            self.world.component_for_entity(
                self.player, components.Velocity).y = BLOCKSIZE
            self.step_counter += 1
        elif sym in (key.DOWN, key.S):
            self.world.component_for_entity(
                self.player, components.Velocity).y = -BLOCKSIZE
            self.step_counter += 1
        elif sym in (key.RIGHT, key.D):
            self.world.component_for_entity(
                self.player, components.Velocity).x = BLOCKSIZE
            self.step_counter += 1
        elif sym in (key.LEFT, key.A):
            self.world.component_for_entity(
                self.player, components.Velocity).x = -BLOCKSIZE
            self.step_counter += 1

    def on_key_released(self, sym, mod):
        """Does not produce any discernable effect, but implementation
        is needed for completeness of the Scene object."""
        if sym in (key.UP, key.DOWN, key.W, key.S):
            self.world.component_for_entity(
                self.player, components.Velocity).y = 0
        if sym in (key.LEFT, key.RIGHT, key.D, key.A):
            self.world.component_for_entity(
                self.player, components.Velocity).x = 0

    def paused(self):
        """Apply shader to increase dark color and render pause text."""
        self.time_proc.pause()
        self.pl.pause()

    def unpaused(self):
        """Remove shaders, text and restart timer."""
        self.time_proc.unpause()
        self.pl.play()

    def next_maze(self):
        """Generates the successive maze"""
        if self.step_counter != 0:
            self.score += self.calculate_score()

        self.maze_size += 1 if self.maze_size < self.max_maze_size else 0

        pad_x = (WIDTH - self.maze_size * BLOCKSIZE) // 2
        pad_y = (HEIGHT - self.maze_size * BLOCKSIZE) // 2
        self.wall_sm = prim.WallSmasher(
            self.maze_size, random.randint(0, 9))
        self.wall_sm.smash()

        # The output is unexpectedly flipped or rotated, and I can't
        # seem to figure out why
        self.grid = np.lib.pad(
            self.wall_sm.get_array(), 1, pad_with_walls)

        # Starting and ending positions as dictated by underlying array
        start_y, start_x = list(map(int, np.where(self.grid == 2)))
        end_y, end_x = list(map(int, np.where(self.grid == 3)))

        self.player = self.ent_factory.make_player(
            pad_x + ((start_x) %
                     self.maze_size) * BLOCKSIZE,
            pad_y + start_y * BLOCKSIZE)
        self.walls = [self.ent_factory.make_wall_block(pad_x + row * BLOCKSIZE,
                                                       pad_y + BLOCKSIZE * col)
                      for row in range(self.maze_size + 2)
                      for col in range(self.maze_size + 2)
                      if self.grid[col][row] == 1]

        self.walls.append(self.ent_factory.make_end(
            pad_x + end_x * BLOCKSIZE, pad_y + end_y * BLOCKSIZE))
        self.movement_proc.end_coords = (
            pad_x + end_x * BLOCKSIZE, pad_y + end_y * BLOCKSIZE)
        self.time_proc.unpause()
        self.time_proc.new_level(add_time=self.maze_size)

    def end(self):
        """There is no loss or victory, only an end."""
        self.score += self.calculate_score()
        self.window.score = self.score
        self.render_proc.clean()
        self.window.change_scene(3)

    def calculate_score(self):
        score = round(len(self.wall_sm.path_to_goal) /
                      self.step_counter * (self.maze_size) ** 2, 2)
        self.step_counter = 0
        return score


class EnterHighscore(Scene):

    def __init__(self, window):
        super().__init__("menu.mp3")
        # Scores
        self.db = ScoresDB()

        self.window = window
        self.window.set_mouse_visible(False)

        self.render_proc = processors.RenderProcessor(self)
        self.world.add_processor(self.render_proc)

        self.text = pyglet.text.Label("Enter your name:",
                                      x=WIDTH // 2, y=HEIGHT * 0.55,
                                      anchor_x="center",
                                      anchor_y="center",
                                      batch=self.batch,
                                      color=(0, 0, 0, 255))
        self.typing = pyglet.text.Label("_",
                                        x=WIDTH // 2, y=HEIGHT * 0.50,
                                        anchor_x="center",
                                        anchor_y="center",
                                        batch=self.batch,
                                        color=(0, 0, 0, 255))
        self.label = []

    def on_key_pressed(self, sym, mod):
        """Could not find any better way of doing this."""
        if sym == key.A:
            self.label.append("A")
        elif sym == key.B:
            self.label.append("B")
        elif sym == key.C:
            self.label.append("C")
        elif sym == key.D:
            self.label.append("D")
        elif sym == key.E:
            self.label.append("E")
        elif sym == key.F:
            self.label.append("F")
        elif sym == key.G:
            self.label.append("G")
        elif sym == key.H:
            self.label.append("H")
        elif sym == key.I:
            self.label.append("I")
        elif sym == key.J:
            self.label.append("J")
        elif sym == key.K:
            self.label.append("K")
        elif sym == key.L:
            self.label.append("L")
        elif sym == key.M:
            self.label.append("M")
        elif sym == key.N:
            self.label.append("N")
        elif sym == key.O:
            self.label.append("O")
        elif sym == key.P:
            self.label.append("P")
        elif sym == key.Q:
            self.label.append("Q")
        elif sym == key.R:
            self.label.append("R")
        elif sym == key.S:
            self.label.append("S")
        elif sym == key.T:
            self.label.append("T")
        elif sym == key.U:
            self.label.append("U")
        elif sym == key.V:
            self.label.append("V")
        elif sym == key.W:
            self.label.append("W")
        elif sym == key.X:
            self.label.append("X")
        elif sym == key.Y:
            self.label.append("Y")
        elif sym == key.Z:
            self.label.append("Z")
        elif sym == key.BACKSPACE:
            if len(self.label):
                self.label.pop()

        self.update()

        if sym == key.RETURN:
            self.db.add_score("".join(self.label), self.window.score)
            self.render_proc.clean()
            self.window.change_scene(0)

    def on_key_released(self, sym, mod):
        pass

    def paused(self):
        pass

    def unpaused(self):
        pass

    def update(self):
        """Update screen after every input."""
        self.name = "".join(self.label) + "_"

        self.render_proc.clean()

        self.text = pyglet.text.Label("Enter your name:",
                                      x=WIDTH // 2, y=HEIGHT * 0.55,
                                      anchor_x="center",
                                      anchor_y="center",
                                      batch=self.batch,
                                      color=(0, 0, 0, 255))

        self.typing = pyglet.text.Label(self.name,
                                        x=WIDTH // 2, y=HEIGHT * 0.50,
                                        anchor_x="center",
                                        anchor_y="center",
                                        batch=self.batch,
                                        color=(0, 0, 0, 255))


class EntityFactory:
    """Helper class for quick entity creation."""

    def __init__(self, world):
        self.world = world

    def make_player(self, x, y):
        """Create player entity at specified position."""
        player = self.world.create_entity()
        self.world.add_component(player, components.Velocity(0, 0))
        self.world.add_component(player, components.Image(
            os.path.join(IMGASSETS, "cube.png")))
        self.world.add_component(player, components.Renderable(x, y))
        self.world.add_component(player, components.Color(255, 0, 0))
        self.world.add_component(player, components.End())
        return player

    def make_wall_block(self, x, y):
        """Create wall entity at specified position."""
        wall = self.world.create_entity()
        self.world.add_component(wall, components.Color(0, 0, 255))
        self.world.add_component(wall, components.Renderable(x, y))
        self.world.add_component(wall, components.Image(
            os.path.join(IMGASSETS, "cube.png")))
        self.world.add_component(wall, components.End())
        return wall

    def make_end(self, x, y):
        end = self.world.create_entity()
        self.world.add_component(end, components.Color(255, 255, 255))
        self.world.add_component(end, components.Renderable(x, y))
        self.world.add_component(end, components.Image(
            os.path.join(IMGASSETS, "cube.png")))
        self.world.add_component(end, components.End(is_end=True))
        return end


def pad_with_walls(vector, pad_width, iaxis, kwargs):
    """Implementation of numpy padding function for
    an array. Builds walls around the outside."""
    vector[: pad_width[0]] = 1
    vector[-pad_width[1]:] = 1
    return vector
