import pygame

# Function to handle player controls
def player_controls(horizontal_speed, vertical_speed):
    keys = pygame.key.get_pressed()

    # Horizontal Movement
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        horizontal_speed = 10
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        horizontal_speed = -10
    else:
        horizontal_speed = 0

    # Vertical Movement
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        vertical_speed = -10
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        vertical_speed = 10
    else:
        vertical_speed = 0

    return horizontal_speed, vertical_speed
