"""Exercise 1: Paddle ball."""


import sys
import time
from random import randint

import pygame
from pygame.math import Vector2 as vec2


display = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Paddle ball")


class Constants:
    counter = 0


class BaseObject:

    def __init__(self, x: int, y: int, x_dim: int, y_dim: int, vel_x=0, vel_y=0):
        self.pos = vec2(x, y)
        self.vel = vec2(vel_x, vel_y)
        self.dims = vec2(x_dim, y_dim)

        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

        self.rect = pygame.Rect(self.pos, self.dims)

    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)

    def collide(self, other):
        """Detects a collision and returns the side from which it happens."""
        if self.rect.colliderect(other.rect):
            # Check if the other rectangle is below
            if other.rect.y <= self.rect.y - self.rect.height / 2:
                return vec2(0, -1)
            # Check if the other rectangle is above
            if other.rect.y >= self.rect.y + self.rect.height / 2:
                return vec2(0, 1)
            # Check if the other rectangle is to the right
            if other.rect.x <= self.rect.x:
                return vec2(1, 0)
            # Check if the other rectangle is to the left
            if other.rect.x >= self.rect.x:
                return vec2(-1, 0)


class Particle(BaseObject):

    def __init__(self, x: int, y: int, x_dim: int, y_dim: int, vel_x=0, vel_y=0):
        super().__init__(x, y, x_dim, y_dim, vel_x, vel_y)
        self.collisions = []

    def move(self, other):
        """Move the particle."""

        normal = self.collide(other)
        if not normal:
            if (self.rect.left + self.vel.x < 0) or \
                    (self.rect.right + self.vel.x > display.get_width()):

                self.vel.x *= -1

            if (self.rect.top + self.vel.y < 0):
                self.vel.y *= -1
        else:
            self.collisions.append(time.time())
            self.vel.reflect_ip(normal)
            if isinstance(other, Slider):
                Constants.counter += 1

        self.rect.move_ip(self.vel)

        # Making sure that the sticking effect does not occur
        # Probably not the best way to do it, but it works regardless
        if len(self.collisions) >= 2:
            if (self.collisions[-1] - self.collisions[-2]) < 0.5:
                self.rect.move_ip((0, -self.rect.height / 2))
                del self.collisions[-1]


class Slider(BaseObject):

    def move_left(self):
        if not (self.rect.left < 0):
            self.rect.move_ip(-self.vel)

    def move_right(self):
        if not (self.rect.right > display.get_width()):
            self.rect.move_ip(self.vel)

    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)

particles = []
particles.append(Particle(10, 10, 10, 10, 5, 5))
slider = Slider(display.get_width() * 0.5 - 25,
                display.get_height() * 0.85, 75, 9, vel_x=10)

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)


while True:
    clock.tick(60)
    display.fill((0, 0, 0))
    text = font.render("Score: " + str(Constants.counter),
                       True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            particles.append(
                Particle(pos[0], pos[1], 10, 10, randint(-5, 5), randint(-5, 5)))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        slider.move_right()
    elif keys[pygame.K_LEFT]:
        slider.move_left()

    slider.draw()
    if len(particles):
        for particle in particles:
            if particle.rect.bottom + particle.vel.y > display.get_height():
                particles.remove(particle)
            else:
                particle.move(slider)
                particle.draw()
    else:
        break

    display.blit(text, (350, 50))
    pygame.display.update()
