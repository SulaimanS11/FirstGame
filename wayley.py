import pygame
import random

# Initialize variables for Wayley character
wayly_still = pygame.image.load(r"P\\hackathons\\1sthackathon\\Pixel_Art\\enemies\\enemyuno\\gorlrun.png").convert_alpha()
wayly_run1 = pygame.image.load(r"P\\hackathons\\1sthackathon\\Pixel_Art\\enemies\\enemyuno\\gorlrun2.png").convert_alpha()
wayly_run2 = pygame.image.load(r"P\\hackathons\\1sthackathon\\Pixel_Art\\enemies\\enemyuno\\gorlrun3.png").convert_alpha()

# Scale Wayley character
wayly_still = pygame.transform.scale(wayly_still, (int(wayly_still.get_width() * 0.7), int(wayly_still.get_height() * 0.7)))
wayly_run1 = pygame.transform.scale(wayly_run1, (int(wayly_run1.get_width() * 0.7), int(wayly_run1.get_height() * 0.7)))
wayly_run2 = pygame.transform.scale(wayly_run2, (int(wayly_run2.get_width() * 0.7), int(wayly_run2.get_height() * 0.7)))

# Character's walking images
wayly_walks = [wayly_still, wayly_run1, wayly_run2]
waylyRect = wayly_still.get_rect()

# Animation Variables
wayly_index = 0
wayly_animation_cooldown = 200  # Time in milliseconds to switch between images
wayly_last_updated = pygame.time.get_ticks()  # Record the time

# Wayley Movement Variables
wayly_speed = 10  # Initial speed of Wayley
target_position = (0, 0)  # Wilfrid's initial target position

def spawn_wayly(wilfrid_rect):
    """Spawn Wayley on the opposite half of Wilfrid's position."""
    global target_position

    # Determine which half of the screen Wilfrid is on and spawn Wayley on the opposite half
    if wilfrid_rect.centerx < 635:  # Wilfrid is on the left half
        waylyRect.x = random.randint(635, 1200)  # Spawn Wayley on the right half
    else:
        waylyRect.x = random.randint(50, 635)  # Spawn Wayley on the left half

    # Random vertical position within the screen height
    waylyRect.y = random.randint(50, 334)

    # Set Wayley's target position to Wilfrid's current position at the time of spawning
    target_position = (wilfrid_rect.centerx, wilfrid_rect.centery)

    # Print Wayley's spawn position for debugging
    print(f"Wayley spawned at: x={waylyRect.x}, y={waylyRect.y}, Target Position: {target_position}")

def animate_wayly():
    """Animate Wayley character."""
    global wayly_index, wayly_last_updated
    current_time = pygame.time.get_ticks()

    # Update animation based on cooldown
    if current_time - wayly_last_updated >= wayly_animation_cooldown:
        wayly_last_updated = current_time
        wayly_index = (wayly_index + 1) % len(wayly_walks)

def move_wayly(wilfrid_rect):
    """Move Wayley towards her target position and despawn when she reaches it."""
    global wayly_speed, target_position

    # Calculate the difference in positions
    diff_x = target_position[0] - waylyRect.centerx
    diff_y = target_position[1] - waylyRect.centery

    # Normalize the direction to get the unit vector
    distance = (diff_x**2 + diff_y**2) ** 0.5
    if distance != 0:
        direction_x = diff_x / distance
        direction_y = diff_y / distance

        # Move Wayley in the direction of the target position
        waylyRect.x += int(wayly_speed * direction_x)
        waylyRect.y += int(wayly_speed * direction_y)

    # Print Wayley's current position for debugging
    print(f"Wayley position: x={waylyRect.x}, y={waylyRect.y}")

    # Check if Wayley has reached the target position
    if distance <= wayly_speed:  # If distance is less than or equal to speed, she's at the target
        print("Wayley reached the target position. Respawning...")
        spawn_wayly(wilfrid_rect)  # Respawn Wayley using Wilfrid's current position

def increase_wayly_speed(score):
    """Increase Wayley's speed based on score."""
    global wayly_speed
    if score % 5 == 0 and score != 0:
        wayly_speed += 2
        print(f"Wayley speed increased to: {wayly_speed}")