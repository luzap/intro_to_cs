"""main.py:
A subclass of the pyglet Window class that forwards all
input-related method calls to the appropriate scenes (there might
be a better way to do this, but this works just fine for a single
player game).

It is also more closely integrated with the *esper* module, which
is a Python entity component system (ECS), allowing for
more modularized design.

TODO
- Create my own assets, drawing inspiration from the examples given
- Improve scaling of user interface
"""

import pyglet
from pyglet.window import key
from pyglet.gl import *
import esper

import scenes
from constants import *


class Window(pyglet.window.Window):
    """Does this need a draw method, or will the processors handle it?"""

    def __init__(self, *args, **kwargs):
        # Relegation of arguments to proxy object
        super().__init__(*args, **kwargs)

        # Not sure if necessary, but seems to improve framerate
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
        self.scenes = [
            scenes.Menu,
            scenes.HighScores,
            scenes.Game,
            scenes.EnterHighscore
        ]

        self.scene = scenes.Menu(self)
        self.score = 0

    def on_key_press(self, sym, mod):
        self.scene.on_key_pressed(sym, mod)

    def on_key_release(self, sym, mod):
        self.scene.on_key_released(sym, mod)

    def change_scene(self, scene_id):
        if self.scene.pl.playing:
            self.scene.pl.pause()
        self.scene = self.scenes[scene_id](self)

    def process(self, dt):
        self.scene.world.process(dt)

    def on_activate(self):
        self.scene.unpaused()

    def on_deactivate(self):
        self.scene.paused()


if __name__ == '__main__':
    window = Window(
        width=WIDTH, height=HEIGHT,
        caption="Can you escape the maze?")

    # Resizing is a pain
    window.set_fullscreen(False)

    # Sets intended framerate
    pyglet.clock.schedule_interval(window.process,
                                   interval=1.0 / FPS)
    pyglet.app.run()
