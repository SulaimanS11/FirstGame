import pygame

# Initialize variables for Wilfrid character
charStarting_pos = (0, 375)
wilfrid_walk1 = pygame.image.load(r"P\\hackathons\\1sthackathon\\Pixel_Art\\character\\sandbox_result_i.png")
wilfrid_walk2 = pygame.image.load(r"P\\hackathons\\1sthackathon\\Pixel_Art\\character\\sandbox_walk.png")

# Scale Wilfrid character down by 30%
wilfrid_walk1 = pygame.transform.scale(wilfrid_walk1, (int(wilfrid_walk1.get_width() * 0.7), int(wilfrid_walk1.get_height() * 0.7)))
wilfrid_walk2 = pygame.transform.scale(wilfrid_walk2, (int(wilfrid_walk2.get_width() * 0.7), int(wilfrid_walk2.get_height() * 0.7)))

# Character's walking images
wilfrid_walks = [wilfrid_walk1, wilfrid_walk2]
wilfridRect = wilfrid_walk1.get_rect(bottomleft=charStarting_pos)

# Animation Variables
walk_index = 0
animation_cooldown = 200  # Time in milliseconds to switch between images
last_updated = pygame.time.get_ticks()  # Record the time

# Movement Variables
horizontal_speed = 0
vertical_speed = 0

def animate_wilfrid():
    # Animate Wilfrid character when a movement key is pressed
    global walk_index, last_updated
    current_time = pygame.time.get_ticks()

    # Update animation based on cooldown
    if current_time - last_updated >= animation_cooldown:
        last_updated = current_time
        walk_index = (walk_index + 1) % len(wilfrid_walks)

def wilfrid_movement():
    # Update character position and animate if moving
    global horizontal_speed, vertical_speed, wilfridRect

    wilfridRect.x += horizontal_speed
    wilfridRect.y += vertical_speed

    # Animate only if there is movement
    if horizontal_speed != 0 or vertical_speed != 0:
        animate_wilfrid()

    # Ensure the character stays within window boundaries
    if wilfridRect.left < 0:
        wilfridRect.left = 0
    if wilfridRect.right > 1270:  # Assuming SCREEN_LENGTH = 1270
        wilfridRect.right = 1270
    if wilfridRect.top < 0:
        wilfridRect.top = 0
    if wilfridRect.bottom > 384:  # Assuming SCREEN_HEIGHT = 384
        wilfridRect.bottom = 384