"""Exercise 1.1: Paddle ball."""

import sys
import pygame
from pygame.math import Vector2 as vec2
from pygame.math import Vector3 as vec3
from random import randint

display = pygame.display.set_mode((500, 600))
pygame.display.set_caption("What's the name of that game?")


class BaseRect:

    def __init__(self, x: int, y: int, x_dim: int, y_dim: int, vel_x=0, vel_y=0):
        self.pos = vec2(x, y)
        self.vel = vec2(vel_x, vel_y)
        self.dims = vec2(x_dim, y_dim)

        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

        self.rect = pygame.Rect(self.pos, self.dims)

    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)


class Particle(BaseRect):

    def move(self):
        """Move the particle."""

        if self.rect.left + self.vel.x < 0:
            self.vel.x *= -1

        if self.rect.right + self.vel.x > display.get_width():
            self.vel.x *= -1

        if self.rect.top + self.vel.y < 0:
            self.vel.y *= -1

        if self.rect.bottom + self.vel.y > display.get_height():
            self.vel.y *= -1

        self.rect.move_ip(self.vel)


class Slider(BaseRect):

    apply_physics = False

    def move_left(self):
        if not (self.rect.left < 0):
            self.rect.move_ip(-self.vel)

    def move_right(self):
        if not (self.rect.right > display.get_width()):
            self.rect.move_ip(self.vel)

    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)

particle = Particle(10, 10, 10, 10, 2, 2)
slider = Slider(display.get_width() * 0.5 - 25,
                display.get_height() * 0.85, 50, 10, vel_x=10)

pygame.init()
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        slider.move_right()
    elif keys[pygame.K_LEFT]:
        slider.move_left()

    slider.draw()
    particle.move()
    particle.draw()
    pygame.display.update()
