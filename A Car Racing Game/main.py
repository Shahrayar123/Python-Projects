import pygame
import random

# Initialize
pygame.init()

# Set up display for the game
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Racing Game")

# Adding Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Car settings
car_width, car_height = 50, 100
car_speed = 5
car_x, car_y = screen_width // 2 - car_width // 2, screen_height - car_height - 20

# Adding Obstacles
obstacle_width, obstacle_height = 50, 100
obstacle_speed = 7
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height

def display_car(x, y):
    pygame.draw.rect(screen, RED, [x, y, car_width, car_height])

def display_obstacle(x, y):
    pygame.draw.rect(screen, BLACK, [x, y, obstacle_width, obstacle_height])

def is_collision(car_x, car_y, obstacle_x, obstacle_y):
    if (car_y < obstacle_y + obstacle_height and car_y + car_height > obstacle_y and 
        car_x + car_width > obstacle_x and car_x < obstacle_x + obstacle_width):
        return True
    return False

# Main game loop
def game_loop():
    global car_x, car_y, obstacle_x, obstacle_y
    game_over = False
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < screen_width - car_width:
            car_x += car_speed

        # Move obstacle
        obstacle_y += obstacle_speed
        if obstacle_y > screen_height:
            obstacle_y = -obstacle_height
            obstacle_x = random.randint(0, screen_width - obstacle_width)
            score += 1

        # Check for collision
        if is_collision(car_x, car_y, obstacle_x, obstacle_y):
            print(f"Game Over! Final Score: {score}")
            game_over = True

        # Fill screen and draw objects
        screen.fill(WHITE)
        display_car(car_x, car_y)
        display_obstacle(obstacle_x, obstacle_y)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# Start the game
game_loop()
