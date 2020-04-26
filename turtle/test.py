import pygame
from pygame.locals import *
import sys
import random



screen = pygame.display.set_mode((400, 700))

def runner():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # if(count == 10):
            #     state = False
                
        # if state:
        #     print(wall_1_x-birdX)
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (0, -100, 10, 200))

        pygame.display.update()

runner()