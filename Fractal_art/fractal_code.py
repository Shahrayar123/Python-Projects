import pygame
import math

# Constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
MAX_DEPTH = 6  # Maximum iterations for the L-system
MIN_DEPTH = 1   # Minimum iterations for the L-system
TREE_SPACING = 100  # Spacing between trees
TREE_COUNT = 1  # Number of trees
ANGLE = math.pi / 2  # 90 degrees

# Function to calculate the fractal dimension D2
def calculate_fractal_dimension(gamma):
    return 2.0 - gamma

# Function to generate the L-system string
def generate_l_system(axiom, rules, iterations):
    current_string = axiom
    for _ in range(iterations):
        next_string = ""
        for char in current_string:
            next_string += rules.get(char, char)
        current_string = next_string
    return current_string

# Function to draw the fractal based on the L-system string
def draw_fractal_l_system(surface, l_system_string, start_x, start_y, length, angle):
    stack = []
    x, y = start_x, start_y
    for command in l_system_string:
        if command == 'F':
            # Calculate new branch endpoint
            x_new = x + length * math.cos(angle)
            y_new = y + length * math.sin(angle)

            # Draw the branch
            pygame.draw.line(surface, (255, 255, 255), (x, y), (x_new, y_new), 1)
            x, y = x_new, y_new
        elif command == '+':
            angle += ANGLE  # Turn right
        elif command == '-':
            angle -= ANGLE  # Turn left
        elif command == '[':
            stack.append((x, y, angle))  # Save current position and angle
        elif command == ']':
            x, y, angle = stack.pop()  # Restore last position and angle

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fractal Trees with Pygame (L-System)")

    clock = pygame.time.Clock()
    axiom = "F+F+F+F"
    rules = {'F': "F+F-F+F+F"}  # Production rule
    iterations = 4  # Initial number of iterations for L-system
    length = 7.0  # Length of each branch

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Adjust depth with key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k and iterations < MAX_DEPTH:
                    iterations += 1  # Increase iterations
                if event.key == pygame.K_j and iterations > MIN_DEPTH:
                    iterations -= 1  # Decrease iterations

        # Generate the L-system string based on the current number of iterations
        l_system_string = generate_l_system(axiom, rules, iterations)  # Generate L-system string

        screen.fill((0, 0, 0))  # Set background color to black

        # Draw the L-system fractal tree
        start_x = SCREEN_WIDTH / 2
        start_y = SCREEN_HEIGHT - 50  # Y position for tree base
        draw_fractal_l_system(screen, l_system_string, start_x, start_y, length, -math.pi / 2)

        # Display the current depth on screen
        font = pygame.font.Font(None, 36)
        text = font.render(f"Iterations (Press K/J to change): {iterations}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(120)

    pygame.quit()

if __name__ == "__main__":
    main()
