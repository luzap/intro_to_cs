import os.path as path

import pygame.image as img

from components.movement import Velocity
from components.rendering import Renderable

from constants import IMAGE_ROOT


def make_dynamic_entity(world, image, posx, posy):
    """Add multiple components for static, renderable entities."""
    entity = world.create_entity()
    world.add_component(entity, Velocity())
    world.add_component(entity, Renderable(image=img.load(
        path.join(IMAGE_ROOT, image)), xpos=posx, ypos=posy))
    return entity


def make_static_entity(world, image, posx, posy):
    """Make a non-moving entity."""
    entity = world.create_entity()
    world.add_component(entity, Renderable(image=img.load(
        path.join(path.join(IMAGE_ROOT, image))), xpos=posx, ypos=posy))
    return entity
