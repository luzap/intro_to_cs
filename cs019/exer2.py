"""Exercise 2: Invaders."""

import sys
from random import randint

import pygame
from pygame.math import Vector2 as vec2


display = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Invaders")


class Particle:

    def __init__(self):
        self.pos = vec2(randint(0, display.get_width()), 10)
        self.vel = vec2(0, 5)
        self.dims = vec2(10, 10)

        self.color = (255, 255, 255)

        self.rect = pygame.Rect(self.pos, self.dims)

    def move(self):
        self.rect.move_ip(self.vel)

    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)


class Ship:

    def __init__(self):
        self.image = pygame.image.load("space-ship.png").convert()
        self.vel = vec2(vel_x, vel_y)

        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

        self.rect = pygame.Rect(vec2(x, y), (self.image.width, self.image.height))

    def move_left(self):
        if not (self.rect.left < 0):
            self.rect.move_ip(-self.vel)

    def move_right(self):
        if not (self.rect.right > display.get_width()):
            self.rect.move_ip(self.vel)

    def draw(self):
        pygame.blit(self.image, (self.rect.x, self.rect.y))

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.font(None, 28)


def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            ship.move_right()
        elif keys[pygame.K_LEFT]:
            ship.move_left()

        if keys[pygame.K_SPACE]:
            ship.shoot()

def victory_screen():
    pass

while True:
    mainloop()
    victory_screen()
