import pygame
# initialize pygame
pygame.init()

# define width of screen
width = 1000
# define height of screen
height = 600
screen_res = (width, height)

pygame.display.set_caption("Bouncing Ball game")
screen = pygame.display.set_mode(screen_res)

# define colors
red = (255, 116, 140)
black = (38, 67, 72)
pink = (255,218,224)

# define ball
ball_obj = pygame.draw.circle(
    surface=screen, color=red, center=[100, 100], radius=40)
# define speed of ball
# speed = [X direction speed, Y direction speed]
speed = [1, 1]

# define font
font = pygame.font.Font(None, 36)  # You can adjust the font size here

# game loop
while True:
    # event loop
    for event in pygame.event.get():
        # check if a user wants to exit the game or not
        if event.type == pygame.QUIT:
            exit()

    # fill black color on screen
    screen.fill(black)

    # move the ball
    ball_obj = ball_obj.move(speed)

    # if ball goes out of screen then change direction of movement
    if ball_obj.left <= 0 or ball_obj.right >= width:
        speed[0] = -speed[0]
    if ball_obj.top <= 0 or ball_obj.bottom >= height:
        speed[1] = -speed[1]

    # draw ball at new centers that are obtained after moving ball_obj
    pygame.draw.circle(surface=screen, color=red,
                       center=ball_obj.center, radius=40)

    # Render and display "WELCOME" text at the bottom
    welcome_text = font.render("WELCOME TO BOUNCING BALL, LET'S ROLL!", True, pink)
    text_rect = welcome_text.get_rect(center=(width // 2, height - 30))
    screen.blit(welcome_text, text_rect)

    # update screen
    pygame.display.flip()