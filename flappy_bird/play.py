import pygame
from pygame.locals import *
import sys
import random

screen = pygame.display.set_mode((400, 700))
bird = pygame.Rect(65, 50, 50, 50)
background = pygame.image.load("pics/background.png").convert()
pics = [pygame.image.load("pics/1.png").convert_alpha(), pygame.image.load("pics/2.png").convert_alpha(), pygame.image.load("pics/dead.png")]
top_pipe = pygame.image.load("pics/top.png").convert_alpha()
bottom_pipe = pygame.image.load("pics/bottom.png").convert_alpha()
gap = random.randint(150, 170)
wall_1_x = 400
wall_2_x = 650
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
space1 = random.randint(-110, 110)
space2 = random.randint(-110, 110)
wall_speed = 2
beginning = False
press_jump = False

with open("data/game_idx.txt", "r") as f:
    current = int(f.read())

with open("data/game_idx.txt", "w") as f:
    f.write(str(current+1))
game_file = f"data/game_{str(current)}.txt"
with open(game_file, "w") as f:
    f.write("bird_y, bottom_pipe_y, top_pipe_y, dist\n")
with open("high_score.txt", "r") as f:
    high_score = int(f.read())
    orig_high_score = high_score

def updateWalls():
    global wall_1_x, wall_2_x, score, space1, space2, gap, high_score, alive, wall_speed
    wall_1_x-=wall_speed
    wall_2_x-=wall_speed
    if wall_1_x < -80:
        wall_1_x = 400
        if alive:
            score += 1
        if(score > high_score):
            high_score = score
        
        space1 = random.randint(-110, 110)
    if wall_2_x < -80:
        wall_2_x = 400
        if alive:
            score += 1
        if(score > high_score):
            high_score = score
        
        space2 = random.randint(-110, 110)
            

def birdUpdate():
    global press_jump, jump, jumpSpeed, birdY, birdX, gravity, wall_1_x, wall_2_x, space1, space2, alive, score, orig_high_score, wall_speed, gap, beginning
    if jump:
        jumpSpeed -= 1
        birdY -= jumpSpeed
        jump -= 1
    else:
        birdY += gravity
        gravity += 0.2
    bird[1] = birdY
    if wall_1_x < -20:
        beginning = True
    if beginning == True and (wall_1_x < -80 or wall_1_x > 150):
        # print("2")
        wall = 2
        space = space2   
        upRect = pygame.Rect(wall_2_x, 0 - gap - space2, top_pipe.get_width() - 10, top_pipe.get_height())
        downRect = pygame.Rect(wall_2_x, 360 + gap - space2, bottom_pipe.get_width() - 10, bottom_pipe.get_height())
    else:
        # print("1")
        wall = 1
        space = space1
        upRect = pygame.Rect(wall_1_x, 0 - gap - space1, top_pipe.get_width() - 10, top_pipe.get_height())
        downRect = pygame.Rect(wall_1_x, 360 + gap - space1, bottom_pipe.get_width() - 10, bottom_pipe.get_height())
    if wall == 1:
        if wall_1_x < birdX:
            dist = 0
        else:
            dist = wall_1_x-birdX
    else:
        if wall_2_x < birdX:
            dist = 0
        else:
            dist = wall_2_x-birdX
    if upRect.colliderect(bird):
        # if alive:
            # print(0 - gap - space + 500, 360 + gap - space, space)
        alive = False
        
    if downRect.colliderect(bird):
        # if alive:
            # print(0 - gap - space + 500, 360 + gap - space, space)

        alive = False
    if alive:
        with open(game_file, "a") as f:
            f.write(f"{int(birdY)},{360 + gap - space},{0 - gap - space + 500},{dist},{int(press_jump)}\n")
            press_jump = False
    if not 0 < bird[1] < 720:
        if orig_high_score < high_score:
            with open("high_score.txt", "w") as f:
                f.write(str(high_score))
        wall_speed = 2
        bird[1] = 50
        birdY = 50
        gap = 170
        # alive = True
        score = 0
        wall_1_x = 400
        wall_2_x = 650
        space1 = random.randint(-110, 110)
        space2 = random.randint(-110, 110)
        gravity = 5
        beginning = False

def runner():
    global jump, sprite, gravity, jumpSpeed, gap, high_score, orig_high_score, alive, birdX, wall_1_x, wall_2_x, space1, space2, press_jump
    clock = pygame.time.Clock()
    pygame.font.init()
    score_font = pygame.font.SysFont("Arial", 50)
    high_score_font = pygame.font.SysFont("Arial", 20)
    while alive == True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and alive == True:
                jump = 17
                press_jump = True
                gravity = 5
                jumpSpeed = 10

            # if(count == 10):
            #     state = False
            # else:
            #     with open("data.txt", "a") as f:
            #         f.write(",0\n")     
        # if state:
        #     print(wall_1_x-birdX)
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(top_pipe, (wall_1_x, 0 - gap - space1))
        screen.blit(bottom_pipe, (wall_1_x, 360 + gap - space1))

        screen.blit(top_pipe, (wall_2_x, 0 - gap - space2))
        screen.blit(bottom_pipe, (wall_2_x, 360 + gap - space2))

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