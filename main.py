import pygame
from pygame.locals import *
import sys
import time


pygame.init()
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


def wayly_animation():
    global wayly1Rect, rob
    if index % 15 == 0:
        if rob == 0:
            rob = 3
        rob -= 1
    
def scoring():
    global score, index
    if index % 60 == 0:
        score += 1
        print(score)

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

### WILFRID
wilfrid_walk2 = pygame.image.load(
    r"P\pygame\hackathon1\Pixel_Art\character\sandbox_walk.png"
)
wilfrid_walk1 = pygame.image.load(
    r"P\pygame\hackathon1\Pixel_Art\character\sandbox_result_i.png"
)
wilfrid_walks = [wilfrid_walk1, wilfrid_walk2]
wilfridRect = wilfrid_walk1.get_rect(bottomleft=(0, 375))
bob = 0
horizontal_speed = 0
vertical_speed = 0
bobby = wilfridRect.y
red = 0

### WAYLY
wayly_still = pygame.image.load(
    r"P\pygame\hackathon1\Pixel_Art\enemies\enemyuno\gorlrun.png"
).convert_alpha()
wayly_run1 = pygame.image.load(
    r"P\pygame\hackathon1\Pixel_Art\enemies\enemyuno\gorlrun2.png"
).convert_alpha()
wayly_run2 = pygame.image.load(
    r"P\pygame\hackathon1\Pixel_Art\enemies\enemyuno\gorlrun3.png"
).convert_alpha()
wayly = [wayly_still, wayly_run1, wayly_run2, wayly_still]
wayly1Rect = wayly_still.get_rect(bottomleft=(1300, 375))
rob = 0
wayly_horspeed = -4
wayly_vertspeed = 0

# LANDSCAPE
background1 = pygame.image.load(
    r"P\pygame\hackathon1\Pixel_Art\scene4\bobsandvegen.jpg"
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

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # PLAYER CONTROLS
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

    # SCORE
    scoring()

    # STATIC BLITS

    # BACKGROUND BLITS
    windowSurface.blit(background1, background1rect)

    # NON STATIC BLITS (CHARACTERS +)
    if red == 0:
        windowSurface.blit(wilfrid_walks[0], wilfridRect)
    else:
        windowSurface.blit(wilfrid_walks[bob], wilfridRect)
    windowSurface.blit(wayly[rob], wayly1Rect)

    ### WAYLY MOVEMENT

    wayly1Rect.x += wayly_horspeed
    wayly1Rect.y += wayly_vertspeed
    if wayly1Rect.left < -20:
        wayly1Rect.bottomleft = (1300, 375)

    ### WILFRID MOVEMENT
    wilfridRect.x += horizontal_speed
    wilfridRect.y += vertical_speed
    if horizontal_speed == 0 and vertical_speed == 0:
        red = 0
    else:
        red = 1

    # COLLISIONS & LOGIC
    if background1rect.right < 900:
        background1rect.topleft = (0, 0)
    
    ### CEILING
    if wilfridRect.top <= 0:
        wilfridRect.top = 0

    ### SCREEN WRAPPING
    if wilfridRect.right <= 0:
        wilfridRect.left = SCREEN_LENGTH

    elif wilfridRect.left >= SCREEN_LENGTH:
        wilfridRect.right = 0
    
    ### GRAVITY
    if vertical_speed == 0:
        if wilfridRect.bottomleft[1] < 375:
            wilfridRect.y += 10
        else:
            wilfridRect.y = bobby

    ### main char movement code
    index_indexer()
    wilfird_movement()
    wayly_animation()


    # NECESSITIES
    clock.tick(60)
    pygame.display.update()
