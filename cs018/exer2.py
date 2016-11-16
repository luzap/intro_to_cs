"""Exercise 2: Main event."""

# TODO Increase speed of particles following cursor
# TODO Make random particles follow cursor
# TODO Velocity a property of radius (inversely prop.)

import pygame
import sys
from random import randint
from math import sqrt
pygame.init()

screen = (height, width) = (1280, 768)
display = pygame.display.set_mode((1280, 768))


class Particle:

    def __init__(self, x: int, y: int, follower: bool):
        self.radius = randint(10, 50)
        self.x = x
        self.y = y
        self.follower = follower

        # Small particles will have a greater max velocity
        self.max_vel = (round((1 / self.radius) * 50))
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def move(self):
        """Move the particle."""
        dir_x, dir_y = (1, 1) if not self.follower else (
            self.follow_cursor()[0], self.follow_cursor()[1])

        self.v_x = randint(0, self.max_vel) * dir_x
        self.v_y = randint(0, self.max_vel) * dir_y

        self.x += self.v_x
        self.x = (self.x % display.get_width())

        self.y += self.v_y
        self.y = (self.y % display.get_height())

    def follow_cursor(self):
        """Returns the directional vector leading towards the mouse cursor.
This is done by finding the Pythagorean distance between the particle and the
cursor, and then using that to normalize the original directional vector.
If the partucle were to coincide with the cursor, it would stop.

        """
        mouse = pygame.mouse.get_pos()
        distance_to_cursor = (mouse[0] - self.x, mouse[1] - self.y)
        abs_distance = sqrt(sum([value ** 2 for value in distance_to_cursor]))
        if abs_distance != 0:
            normalized = [round(distance /
                                abs_distance) for distance in distance_to_cursor]
        else:
            normalized = (0, 0)

        return normalized

    def draw(self):
        """Draw particle using global display variable."""
        pygame.draw.circle(display, self.color,
                           (self.x, self.y), self.radius)


particles = []

for index in range(100):
    particles.append(Particle(randint(0, height), randint(
        0, height), True if randint(1, 100) > 90 else False))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.K_q:
            sys.exit(0)
    display.fill((0, 0, 0))
    for particle in particles:
        particle.move()
        particle.draw()

    pygame.display.update()
