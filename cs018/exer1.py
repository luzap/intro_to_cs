"""Exercise 1: Practice."""

import pygame
import sys
pygame.init()

display = pygame.display.set_mode((640, 480))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

mouth = pygame.Rect(display.get_width() // 2 - 30,
                    display.get_height() // 2 + 30, 60, 10)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    display.fill(WHITE)
    pygame.draw.circle(display, BLACK, (display.get_width() //
                                        2, display.get_height() // 2), 75)
    pygame.draw.circle(display, GREY, (display.get_width() //
                                       2 - 30, display.get_height() // 2), 20)
    pygame.draw.circle(display, GREY, (display.get_width() //
                                       2 + 30, display.get_height() // 2), 20)
    pygame.draw.circle(display, WHITE, (display.get_width() //
                                        2 - 35, display.get_height() // 2), 10)
    pygame.draw.circle(display, WHITE, (display.get_width() //
                                        2 + 35, display.get_height() // 2), 10)
    pygame.draw.rect(display, GREY, mouth)
    pygame.display.update()
