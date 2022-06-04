import pygame
from pygame.locals import *
import sys


pygame.init()
windowSurface = pygame.display.set_mode((1200,800),0,32)
pygame.display.set_caption("Travel to Monaco")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

basicFont = pygame.font.SysFont(None, 48)

text = basicFont.render("Hello World!", True, WHITE,BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.fill(WHITE)

player_walk1 = pygame.image.load(r"P\pygame\hackathon1\Pixel_Art\character\sandbox_walk.jpg")
player_walk2 = pygame.image.load(r"P\pygame\hackathon1\Pixel_Art\character\sandbox_result_i.jpeg")




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.blit(text,textRect)

    pygame.display.update()