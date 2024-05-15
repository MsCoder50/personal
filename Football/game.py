import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 128, 0)  # Green

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Football Game")

# Load player image
player_image = pygame.image.load("player_1.png")
player_image = pygame.transform.scale(player_image, (30, 50))  # Resize the player image

# Load opponent image
opponent_image = pygame.image.load("player_2.png")
opponent_image = pygame.transform.scale(opponent_image, (30, 50))  # Resize the opponent image

# Load ball image
ball_image = pygame.image.load("ball.png")
ball_image = pygame.transform.scale(ball_image, (20, 20))  # Resize the ball image
ball_rect = ball_image.get_rect()

# Generate 11 players in a formation
formation_positions = [
    (WIDTH // 2, HEIGHT - 50),  # Current player (controlled by "Q" key)
    (WIDTH // 2, HEIGHT - 150),  # GK
    (WIDTH // 2, HEIGHT - 200),  # CB
    (WIDTH // 2 - 50, HEIGHT - 200),  # CB
    (WIDTH // 2 + 50, HEIGHT - 200),  # CB
    (WIDTH // 2 - 100, HEIGHT - 250),  # LB
    (WIDTH // 2 + 100, HEIGHT - 250),  # RB
    (WIDTH // 2 - 30, HEIGHT - 300),  # CM
    (WIDTH // 2 + 30, HEIGHT - 300),  # CM
    (WIDTH // 2 - 100, HEIGHT - 350),  # LW
    (WIDTH // 2 + 100, HEIGHT - 350)  # RW
]

player_rects = [pygame.Rect(x - 15, y - 25, 30, 50) for x, y in formation_positions]

# Generate 11 opponents in the same formation but not coinciding with players
opponent_positions = [
    (x, y - 300) for x, y in formation_positions
]

opponent_rects = [pygame.Rect(x - 15, y - 25, 30, 50) for x, y in opponent_positions]

# Set the initial ball position
ball_rect.center = (WIDTH // 2, HEIGHT // 2)
ball_speed = [0, 0]  # Initial momentum of the ball
ball_momentum = 3  # Initial momentum when the player hits the ball
friction = 0.1  # Friction to slow down the ball

# Boundary (the entire game window)
boundary_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)

# Player control variables
current_player_index = 0  # Index of the current player being controlled

# Function to find the index of the nearest player to the ball
def find_nearest_player_to_ball():
    ball_center = pygame.Vector2(ball_rect.center)
    distances = [ball_center.distance_to(player_rect.center) for player_rect in player_rects]
    return distances.index(min(distances))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            # Switch control to the nearest player to the ball when "Q" key is pressed
            current_player_index = find_nearest_player_to_ball()

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rects[current_player_index].x -= 5
    if keys[pygame.K_RIGHT]:
        player_rects[current_player_index].x += 5
    if keys[pygame.K_UP]:
        player_rects[current_player_index].y -= 5
    if keys[pygame.K_DOWN]:
        player_rects[current_player_index].y += 5

    # Calculate the direction vector from the ball to the goal
    goal_center = pygame.Vector2(WIDTH // 2, 0)
    direction_vector = goal_center - pygame.Vector2(ball_rect.center)

    # Check if the direction_vector is not a zero vector
    if direction_vector.length() > 0:
        direction_vector.normalize_ip()

        # Check for player collision with the ball
        if player_rects[current_player_index].colliderect(ball_rect):
            # Calculate the direction vector from the player to the ball
            direction_vector = pygame.Vector2(ball_rect.center) - pygame.Vector2(player_rects[current_player_index].center)
            if direction_vector.length() > 0:
                direction_vector.normalize_ip()
                ball_momentum = random.uniform(4, 6)
                ball_speed = [direction_vector.x * ball_momentum, direction_vector.y * ball_momentum]

    # Move the ball
    ball_rect.x += ball_speed[0]
    ball_rect.y += ball_speed[1]

    # Check for ball hitting the boundary
    if not boundary_rect.contains(ball_rect):
        # Reset the ball to the starting position
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed = [0, 0]

    # Apply friction to slow down the ball
    ball_speed[0] *= (1 - friction)
    ball_speed[1] *= (1 - friction)

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the boundary
    pygame.draw.rect(screen, (255, 255, 255), boundary_rect, 2)

    # Draw the opponents, players, and the ball
    for i, opponent_rect in enumerate(opponent_rects):
        screen.blit(opponent_image, opponent_rect)

    for i, player_rect in enumerate(player_rects):
        if i == current_player_index:
            # Highlight the current player
            pygame.draw.rect(screen, (255, 0, 0), player_rect, 2)
        screen.blit(player_image, player_rect)

    screen.blit(ball_image, ball_rect)

    # Update the display
    pygame.display.flip()

    # Control the game speed
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
sys.exit()
