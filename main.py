from re import L
from turtle import left
import pygame
from pygame.locals import *
import sys
import time
import characters
import random

pygame.init()


# WINDOW & DISPLAY SETTINGS
SCREEN_HEIGHT = 384
SCREEN_LENGTH = 1270
windowSurface = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT), 0, 32)
windowSurface.fill((255, 255, 255))
windowRect = windowSurface.get_rect()
windowCenter = windowRect.center
pygame.display.set_caption("Travel to Monaco")


# INDEX
index = 0


# CHARACTERS
Wayly_c = characters.Wayly()

### WILFRID
charStarting_pos = (0, 375)
wilfrid_walk2 = pygame.image.load(
    r"C:\Users\mirsu\Desktop\Code\P\pygame\FirstGame\Pixel_Art\character\sandbox_walk.png"
)
wilfrid_walk1 = pygame.image.load(
    r"C:\Users\mirsu\Desktop\Code\P\pygame\FirstGame\Pixel_Art\character\sandbox_result_i.png"
)
wilfrid_walks = [wilfrid_walk1, wilfrid_walk2]
wilfridRect = wilfrid_walk1.get_rect(bottomleft=charStarting_pos)
bob = 0
horizontal_speed = 0
vertical_speed = 0
bobby = wilfridRect.y
red = 0

### WAYLY

wayly_still = pygame.image.load(
    r"C:\Users\mirsu\Desktop\Code\P\pygame\FirstGame\Pixel_Art\enemies\enemyuno\gorlrun.png"
).convert_alpha()
wayly_run1 = pygame.image.load(
    r"C:\Users\mirsu\Desktop\Code\P\pygame\FirstGame\Pixel_Art\enemies\enemyuno\gorlrun2.png"
).convert_alpha()
wayly_run2 = pygame.image.load(
    r"C:\Users\mirsu\Desktop\Code\P\pygame\FirstGame\Pixel_Art\enemies\enemyuno\gorlrun3.png"
).convert_alpha()
wayly = [wayly_still, wayly_run1, wayly_run2, wayly_still]
waylyHeight = wayly_still.get_size()[0]
waylyWidth = wayly_still.get_size()[1]
wayStart = Wayly_c.return_startingPos()[0]+waylyWidth, Wayly_c.return_startingPos()[1]


spawn_ranges = [(0,2*waylyHeight),(SCREEN_LENGTH,SCREEN_LENGTH+2*waylyWidth),(SCREEN_HEIGHT,SCREEN_HEIGHT+2*waylyHeight),(0,-2*waylyWidth)]
wayly1Rect = wayly_still.get_rect(bottomleft=wayStart)
rob = 0

wayly_horspeed = Wayly_c.wayly_hSpeed
wayly_vertspeed = Wayly_c.wayly_vSpeed
DIRECTIONS = {'left' : "left", 'right':'right','downleft':'downleft','downright':'downright','upleft':'upleft','upright':'upright'}
wayDir = "left"

# BOUNCING






# LANDSCAPE
background1 = pygame.image.load(
    r"C:\Users\mirsu\Desktop\Code\P\pygame\FirstGame\Pixel_Art\scene4\back1.jpg"
)
background1rect = background1.get_rect(topleft=(0, 0))

# EXTRA
clock = pygame.time.Clock()

# SCORE
score = 0

def waylyAttack():
    global wayly_speed, wayly_horspeed, wayly1Rect, score
    if score == -4:
        None


# FUNCTIONS
def index_indexer():
    global index
    index += 1
    if index > 5000:
        index = 1


def wilfird_movement():
    global bob
    if index % 10 == 0:
        if bob == 0:
            bob = 1
        elif bob == 1:
            bob = 0

    wilfridRect.x += horizontal_speed
    wilfridRect.y += vertical_speed
    if horizontal_speed == 0 and vertical_speed == 0:
        red = 0
    else:
        red = 1

def char_blit():
    if red == 0:
        windowSurface.blit(wilfrid_walks[0], wilfridRect)
    else:
        windowSurface.blit(wilfrid_walks[bob], wilfridRect)
    windowSurface.blit(wayly[rob], wayly1Rect)

def wayly_animation():
    global wayly1Rect, rob, wayly_horspeed, wayly_vertspeed
    if index % 15 == 0:
        if rob == 0:
            rob = 3
        rob -= 1

    wayly1Rect.x -= wayly_horspeed
    wayly1Rect.y += wayly_vertspeed
    
def wayly_bounce():
    if wayDir == 'downleft':
        wayly1Rect.x -= wayly_vertspeed
        wayly1Rect.y += wayly_vertspeed
    if wayDir == 'downright':
        wayly1Rect.x += wayly_vertspeed
        wayly1Rect.y += wayly_vertspeed
    if wayDir == 'upleft':
        wayly1Rect.x -= wayly_vertspeed
        wayly1Rect.y -= wayly_vertspeed
    if wayDir == 'upright':
        wayly1Rect.x += wayly_vertspeed
        wayly1Rect.y -= wayly_vertspeed
    if wayDir == "left":
        wayly1Rect.x -= wayly_horspeed
    if wayDir == "right":
        wayly1Rect.x += wayly_horspeed

    if wayly1Rect.bottom == windowRect.bottom:
        if wayDir == 'downleft':
            wayDir = 'upleft'
        if wayDir == 'downright':
            wayDir = 'upright'

    if wayly1Rect.left == windowRect.left:
        pass

    if wayly1Rect.top == windowRect.top:
        if wayDir == 'upleft':
            wayDir = 'downleft'
        if wayDir == 'upright':
            wayDir = 'downright'

    if wayly1Rect.right == windowRect.right:
        pass

def wayly_spawnLogic():
    global wayly1Rect, rob, wayly_horspeed, wayly_vertspeed, wayDir
    if wayly1Rect.x > 2*waylyWidth+SCREEN_LENGTH or wayly1Rect.x < -waylyWidth*2 or wayly1Rect.y > 2*waylyHeight+SCREEN_HEIGHT or wayly1Rect.y < 2*-waylyHeight:
        return
        
    # if score ==2:
    #     wayly1Rect.bottomleft = (wayStart)
    #     wayly_horspeed = 5

    # if score == 7:
    #     wayly1Rect.bottomleft = (wayStart)
    #     wayly_horspeed = 5
    #     wayDir = "left"

    # if score == 12:
    #     wayly1Rect.bottomleft = (-100, 0)
    #     wayly_horspeed = 5
    #     wayly_vertspeed = 10
    #     wayDir ="downright"

def scoring():
    global score, index
    if index % 60 == 0:
        score += 1
        print(score)

def gravity():
    if vertical_speed == 0:
        if wilfridRect.bottomleft[1] < 375:
            wilfridRect.y += 10
        else:
            wilfridRect.y = wilfridRect.y
def screen_wrapping():
    if wilfridRect.right <= 0:
        wilfridRect.left = SCREEN_LENGTH

    elif wilfridRect.left >= SCREEN_LENGTH:
        wilfridRect.right = 0
def borders():
    if wilfridRect.top <= 0:
        wilfridRect.top = 0
    

def collisions():
    if background1rect.right < 900:
        background1rect.topleft = (0, 0)

def player_controls():
    global vertical_speed, horizontal_speed, red
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            horizontal_speed += 5
            red = 1
        if event.key == pygame.K_a:
            horizontal_speed -= 5
            red = 1
        if event.key == pygame.K_w:
            vertical_speed -= 10
            red = 1

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            horizontal_speed -= 5
        if event.key == pygame.K_a:
            horizontal_speed += 5
        if event.key == pygame.K_w:
            vertical_speed += 10

    
    if event.type == pygame.MOUSEBUTTONDOWN:
        vertical_speed -= 20
    
    if event.type == pygame.MOUSEBUTTONUP:
        vertical_speed += 20

def back_blit():
    windowSurface.blit(background1, background1rect)

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # PLAYER CONTROLS
        player_controls()

    # SCORE
    scoring()

    # STATIC BLITS

    # BACKGROUND BLITS
    back_blit()

    # NON STATIC BLITS (CHARACTERS +)
    char_blit()

    ### WAYLY MOVEMENT
    wayly_spawnLogic()


    # COLLISIONS & LOGIC
    collisions()
    
    ### BORDERS
    borders()

    ### SCREEN WRAPPING
    screen_wrapping()
    
    ### GRAVITY
    gravity()

    ### main char movement code
    index_indexer()
    wilfird_movement()
    wayly_animation()


    # NECESSITIES
    clock.tick(60)
    pygame.display.update()
