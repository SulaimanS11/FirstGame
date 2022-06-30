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
# CHARACTERS
wilfrid_walk2 = pygame.image.load(
    r"P\hackathons\1sthackathon\Pixel_Art\character\sandbox_walk.png"
)
wilfrid_walk1 = pygame.image.load(
    r"P\hackathons\1sthackathon\Pixel_Art\character\sandbox_result_i.png"
)
wilfrid_walks = [wilfrid_walk1, wilfrid_walk2]
wilfridRect = wilfrid_walk1.get_rect(bottomleft=(0, 384))
bob = 0
player_speed = 0


wayly_still = pygame.image.load(
    r"P\hackathons\1sthackathon\Pixel_Art\enemies\enemyuno\gorlrun.png"
).convert_alpha()
wayly_run1 = pygame.image.load(
    r"P\hackathons\1sthackathon\Pixel_Art\enemies\enemyuno\gorlrun2.png"
).convert_alpha()
wayly_run2 = pygame.image.load(
    r"P\hackathons\1sthackathon\Pixel_Art\enemies\enemyuno\gorlrun3.png"
).convert_alpha()
wayly = [wayly_still, wayly_run1, wayly_run2, wayly_still]
wayly1Rect = wayly_still.get_rect(bottomleft=(1300, 384))
rob = 0
wayly_horspeed = -4
wayly_vertspeed = 0
wayDir = ["left", "right", "up", "down", "downleft", "downright", "upleft", "upright"]


# BOUNCING

# if wayDir == 'downleft':
#     wayly1Rect.left -= wayly_vertspeed
#     wayly1Rect.top += wayly_vertspeed
# if wayDir == 'downright':
#     wayly1Rect.left += wayly_vertspeed
#     wayly1Rect.top += wayly_vertspeed
# if wayDir == 'upleft':
#     wayly1Rect.left -= wayly_vertspeed
#     wayly1Rect.top -= wayly_vertspeed
# if wayDir == 'upright':
#     wayly1Rect.left += wayly_vertspeed
#     wayly1Rect.top -= wayly_vertspeed


# if wayly1Rect.bottom == windowRect.bottom:
#     if wayDir == 'downleft':
#         wayDir = 'upleft'
#     if wayDir == 'downright':
#         wayDir = 'upright'

# if wayly1Rect.left == windowRect.left:
#     if wayDir == 'upleft':
#         wayDir = 'upright'
#     if wayDir == 'downleft':
#         wayDir = 'downright'

# if wayly1Rect.top == windowRect.top:
#     if wayDir == 'upleft':
#         wayDir = 'downleft'
#     if wayDir == 'upright':
#         wayDir = 'downright'

# if wayly1Rect.right == windowRect.right:
#     if wayDir == 'downright':
#         wayDir = 'downleft'
#     if wayDir == 'upright':
#         wayDir = 'upleft'


# LANDSCAPE
background1 = pygame.image.load(
    r"P\hackathons\1sthackathon\Pixel_Art\scene4\bobsandvegen.jpg"
)
background1rect = background1.get_rect(topleft=(0, 0))

# EXTRA
clock = pygame.time.Clock()


# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # PLAYER CONTROLS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player_speed += 5
            if event.key == pygame.K_a:
                player_speed -= 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player_speed -= 5
            if event.key == pygame.K_a:
                player_speed += 5

    # STATIC BLITS

    # BACKGROUND BLITS
    windowSurface.blit(background1, background1rect)

    # NON STATIC BLITS (CHARACTERS +)
    windowSurface.blit(wilfrid_walks[bob], wilfridRect)
    windowSurface.blit(wayly[rob], wayly1Rect)

    ### WAYLY MOVEMENT
    if score == 7:
        wayly1Rect.bottomleft = (1300, 375)
        wayly_horspeed = -5

    if score == 12:
        wayly1Rect.bottomleft = (0, 0)
        wayly_horspeed = 0
        wayly_vertspeed = 10

    wayly1Rect.x += wayly_horspeed
    wayly1Rect.y += wayly_vertspeed

    ### WILFRID MOVEMENT
    wilfridRect.x += player_speed

    # COLLISIONS & LOGIC
    if background1rect.right < 900:
        background1rect.topleft = (0, 0)

    ### main char movement code
    index_indexer()
    wilfird_movement()
    wayly_movement()
    # player_walk_animation()

    # NECESSITIES
    clock.tick(60)
    pygame.display.update()
