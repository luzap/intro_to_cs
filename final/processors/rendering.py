import esper
import pygame

from components.rendering import Renderable


class RenderingProcessor(esper.Processor):
    """."""

    def __init__(self, window, world):
        """."""
        self.window = window
        self.color = (0, 0, 0)

    def process(self):
        """."""
        self.window.fill(self.color)

        for ent, rend in self.world.get_component(Renderable):
            self.window.blit(rend.image, (rend.x, rend.y))

        pygame.display.flip()
