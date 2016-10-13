import pygame
import esper

from components.movement import Velocity

from processors.movement import MovementProcessor
from processors.rendering import RenderingProcessor

from constants import RESOLUTION, FRAMERATE
from utils.entity import make_dynamic_entity


def main():
    """Initialization and running of window and addition of systems."""
    pygame.init()
    window = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("Runner v0.0.1")
    clock = pygame.time.Clock()

    world = esper.World()
    player = make_dynamic_entity(world, "player.png", 50, 50)

    render_processor = RenderingProcessor(world=world, window=window)
    movement_processor = MovementProcessor(minx=0, maxx=RESOLUTION[0], miny=0,
                                           maxy=RESOLUTION[1])
    world.add_processor(render_processor)
    world.add_processor(movement_processor)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    world.component_for_entity(player, Velocity).v_y -= 10
                elif event.key == pygame.K_DOWN:
                    world.component_for_entity(player, Velocity).v_y += 10
                elif event.key == pygame.K_LEFT:
                    world.component_for_entity(player, Velocity).v_x -= 10
                elif event.key == pygame.K_RIGHT:
                    world.component_for_entity(player, Velocity).v_x += 10
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    world.component_for_entity(player, Velocity).v_y = 0
                elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    world.component_for_entity(player, Velocity).v_x = 0

        world.process()
        clock.tick(FRAMERATE)


if __name__ == '__main__':
    main()
    pygame.quit()
