
import pygame
import sys
import characters
import controls  # Importing the controls module
import wilfrid  # Importing the Wilfrid module

# Initialize Pygame
pygame.init()

# Window Settings
SCREEN_HEIGHT = 384
SCREEN_LENGTH = 1270
windowSurface = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("Travel to Monaco")

# Import Wayley module after display initialization
import wayley

# Score Variables
score = 0
font = pygame.font.SysFont(None, 48)  # Create font object for displaying score

# Timer for incrementing score every second
pygame.time.set_timer(pygame.USEREVENT, 1000)  # Trigger USEREVENT every 1000 milliseconds (1 second)

# Initial Spawn of Wayley
wayley.spawn_wayly(wilfrid.wilfridRect)

# Clock
clock = pygame.time.Clock()

def display_score():
    # Render and display the score on the screen
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    windowSurface.blit(score_text, (10, 10))

def main():
    # Main game loop
    global score

    while True:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.USEREVENT:
                # Increment score every second
                score += 1

                # Increase Wayley's speed every 5 score increments
                wayley.increase_wayly_speed(score)

        # Use player controls from the module to update speed values
        wilfrid.horizontal_speed, wilfrid.vertical_speed = controls.player_controls(wilfrid.horizontal_speed, wilfrid.vertical_speed)

        # Move Wilfrid character based on controls
        wilfrid.wilfrid_movement()

        # Move Wayley character towards Wilfrid
        wayley.move_wayly(wilfrid.wilfridRect)
        wayley.animate_wayly()

        # Fill the screen
        windowSurface.fill((255, 255, 255))

        # Blit Wilfrid character on screen with animation
        windowSurface.blit(wilfrid.wilfrid_walks[wilfrid.walk_index], wilfrid.wilfridRect)

        # Blit Wayley character on screen with animation
        windowSurface.blit(wayley.wayly_walks[wayley.wayly_index], wayley.waylyRect)

        # Display the score on screen
        display_score()

        # Update display
        pygame.display.update()
        clock.tick(60)

main()