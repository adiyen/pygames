import pygame
from pygame.locals import *
import sys
import random



screen = pygame.display.set_mode((400, 700))
bird = pygame.Rect(65, 50, 50, 50)
background = pygame.image.load("pics/background.png").convert()
pics = [pygame.image.load("pics/1.png").convert_alpha(), pygame.image.load("pics/2.png").convert_alpha(), pygame.image.load("pics/dead.png")]
top_pipe = pygame.image.load("pics/bottom.png").convert_alpha()
bottom_pipe = pygame.image.load("pics/top.png").convert_alpha()
gap = 170
wallx = 400
birdY = 350
birdX = 65
jump = 0
jumpSpeed = 10
gravity = 5 
alive = True
sprite = 0
score = 0
high_score = 0
orig_high_score = 0
space = random.randint(-110, 110)
wall_speed = 2


with open("high_score.txt", "r") as f:
    high_score = int(f.read())
    orig_high_score = high_score

def updateWalls():
    global wallx, score, space, gap, high_score, alive, wall_speed
    wallx-=wall_speed
    if wallx < -80:
        wallx = 400
        if alive:
            score += 1
        if(score > high_score):
            high_score = score
        
        space = random.randint(-110, 110)
        if score % 5 == 0:
            gap-=20
        if score % 3 == 0:
            wall_speed+=1
            

def birdUpdate():
    global jump, jumpSpeed, birdY, gravity, wallx, space, alive, score, orig_high_score, wall_speed, gap
    if jump:
        jumpSpeed -= 1
        birdY -= jumpSpeed
        jump -= 1
    else:
        birdY += gravity
        gravity += 0.2
    bird[1] = birdY
    upRect = pygame.Rect(wallx, 360 + gap - space + 10, top_pipe.get_width() - 10, top_pipe.get_height())
    downRect = pygame.Rect(wallx, 0 - gap - space - 10, bottom_pipe.get_width() - 10, bottom_pipe.get_height())
    if upRect.colliderect(bird):
        alive = False
    if downRect.colliderect(bird):
        alive = False
    if not 0 < bird[1] < 720:
        if orig_high_score < high_score:
            with open("high_score.txt", "w") as f:
                f.write(str(high_score))
        wall_speed = 2
        bird[1] = 50
        birdY = 50
        gap = 170
        alive = True
        score = 0
        wallx = 400
        space = random.randint(-110, 110)
        gravity = 5

def runner():
    global jump, sprite, gravity, jumpSpeed, gap, high_score, orig_high_score, alive, birdX, wallx
    clock = pygame.time.Clock()
    pygame.font.init()
    score_font = pygame.font.SysFont("Arial", 50)
    high_score_font = pygame.font.SysFont("Arial", 20)
    running = True
    state = True
    count = 0
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and alive == True:
                jump = 17
                gravity = 5
                jumpSpeed = 10

            # if(count == 10):
            #     state = False
                
        if state:
            print(wallx-birdX)
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(top_pipe, (wallx, 360 + gap - space))
        screen.blit(bottom_pipe, (wallx, 0 - gap - space))
        if state:
            print()
        screen.blit(score_font.render(str(score), -1, (255, 255, 255)), (200, 50))
        screen.blit(high_score_font.render("High Score: " + str(high_score), -1, (255, 255, 255)), (100, 10))
        if alive == False:
            sprite = 2
        elif jump:
            sprite = 1
        screen.blit(pics[sprite], (70, birdY))
        if alive == True:
            sprite = 0
        updateWalls()
        birdUpdate()
        pygame.display.update()

runner()