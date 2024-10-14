# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)      # Color for the food
GREEN = (0, 255, 0)      # Color for the snake
BLUE = (50, 153, 213)    # Background color

# Fill screen with background color
screen.fill(BLUE)

# Draw the snake in GREEN
pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

# Draw the food in RED
pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])
