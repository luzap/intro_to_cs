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
        self.image = pygame.image.load("space-ship.png")
        self.vel = vec2(5, 0)

        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

        self.rect = pygame.Rect(
            vec2(display.get_width() / 2, display.get_height() * 0.8),
            (self.image.get_width(), self.image.get_height()))

    def move_left(self):
        if not (self.rect.left < 0):
            self.rect.move_ip(-self.vel)

    def move_right(self):
        if not (self.rect.right > display.get_width()):
            self.rect.move_ip(self.vel)

    def draw(self):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self):
        pass

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)


ship = Ship()


def mainloop():
    particles = []
    while True:
        if randint(0, 100) > 90:
            particles.append(Particle())

        clock.tick(60)
        display.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            ship.move_right()
        elif keys[pygame.K_LEFT]:
            ship.move_left()

        if keys[pygame.K_SPACE]:
            ship.shoot()

        for particle in particles:
            if ship.rect.colliderect(particle.rect):
                return False
            particle.move()
            particle.draw()
        ship.draw()

        pygame.display.update()


playing = mainloop()

while not playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(60)
    display.fill((0, 0, 0))
    text = font.render("You lost!", True, (255, 255, 255))
    display.blit(text, (display.get_width() / 2 - text.get_width() /
                        2, display.get_height() / 2 - text.get_height() / 2))
    pygame.display.update()
