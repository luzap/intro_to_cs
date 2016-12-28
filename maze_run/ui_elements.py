"""ui_elements.py:

Recreation of some of the UI elements for better compliance with the needs 
of the game.

"""
import sys

from pyglet_gui.buttons import OneTimeButton


class SceneButton(OneTimeButton):
    """Switches scenes."""

    def __init__(self, window, state, label=""):
        super().__init__(label, on_release=self.scene_change)
        self.window = window
        self.state = state

    def scene_change(self, is_pressed):
        self.window.change_scene(self.state)


class QuitButton(OneTimeButton):
    """Menu button that allows the game to quit."""
    def __init__(self, label=""):
        super().__init__(label, on_release=self.on_rel)

    def on_rel(self, ispressed):
        if not ispressed:
            sys.exit(0)


