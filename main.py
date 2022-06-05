import pygame
from pygame.locals import *
import sys


pygame.init()
# WINDOW & DISPLAY SETTINGS
windowSurface = pygame.display.set_mode((1200,800),0,32)
windowSurface.fill((255,255,255))
windowRect = windowSurface.get_rect()
windowCenter = windowRect.center
pygame.display.set_caption("Travel to Monaco")


# INDEX
index = 0
# CHARACTERS
wilfrid_walk2 = pygame.image.load(r"P\pygame\hackathon1\Pixel_Art\character\sandbox_walk.png")
wilfrid_walk1 = pygame.image.load(r"P\pygame\hackathon1\Pixel_Art\character\sandbox_result_i.png")
wilfrid_walks = [wilfrid_walk1, wilfrid_walk2]
wilfridRect = wilfrid_walk1.get_rect(bottomleft = (0,700))
bob = 0


# LANDSCAPE
background1 = pygame.image.load(r"P\pygame\hackathon1\Pixel_Art\scene1\zxcr_s9nj_200605 - Copy.jpg")
background1rect = background1.get_rect(topleft = (0,0))

# EXTRA
clock = pygame.time.Clock()



# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # STATIC BLITS

    # BACKGROUND BLITS
    windowSurface.blit(background1, background1rect)
    background1rect.right -= 2
    # NON STATIC BLITS (CHARACTERS +)
    windowSurface.blit(wilfrid_walks[bob],wilfridRect)

    # COLLISIONS & LOGIC
    if background1rect.right < 1200:
        background1rect.topleft = (0,0)

    index += 1
    if index > 1000: index = 0
    if index % 5 == 0:
        if bob == 0:
            bob = 1
        elif bob == 1:
            bob = 0

    #NECESSITIES
    clock.tick(60)
    pygame.display.update()