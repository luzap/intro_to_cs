import pygame

class Renderable:
    """Renderable component. Determines where to render an objects."""

    def __init__(self, image, xpos, ypos):
        """Define the position and dimensions of the sprite."""
        self.image = image
        self.x = xpos
        self.y = ypos
        self.width = self.image.get_width()
        self.height = self.image.get_height()
