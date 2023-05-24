# W - S for left player to go Up - Down respectively.
# I - K for right player to go Up - Down respectively.

import pygame, random

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("PingPong")
FPS = 30

player1_pos = [30, 200]
player2_pos = [960, 200]


class Button():
    def __init__(self, x, y, width, height, text='', color=(255, 255, 255), active_color=(200, 200, 200)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.active_color = active_color
        self.text = text
        self.font = pygame.font.Font(None, int(height * 0.6))

    def draw(self, surface, outline=None):
        if outline:
            pygame.draw.rect(surface, outline, self.rect, 0)
        pygame.draw.rect(surface, self.color, self.rect, 0)
        if self.text != '':
            text = self.font.render(self.text, 1, (0, 0, 0))
            text_pos = text.get_rect(center=self.rect.center)
            surface.blit(text, text_pos)

    def is_mouse_over(self, pos):
        return self.rect.collidepoint(pos)

    def set_active(self, active):
        self.color = self.active_color if active else (255, 255, 255)

class Saber:
    def __init__(self, color, pos) -> None:
        self.width, self.height = 10, 80
        self.color = color
        self.xpos, self.ypos = pos

    def draw(self):
        self.object = pygame.draw.rect(
            screen, self.color, (self.xpos, self.ypos, self.width, self.height)
        )
        self.rect = pygame.Rect(self.object)


class Ball:
    def __init__(self) -> None:
        self.radius = 10
        self.color = "BLUE"
        self.xpos, self.ypos = 500, 250
        self.dirs = [
            "left",
            "topleft",
            "bottomleft",
            "right",
            "topright",
            "bottomright",
        ]
        self.dir = random.choice(self.dirs)

    def draw(self):
        self.object = pygame.draw.circle(
            screen, self.color, (self.xpos, self.ypos), self.radius
        )
        self.rect = pygame.Rect(self.object)

    def move(self):
        # self.dirs = ['left','topleft','bottomleft','right','topright','bottomright']

        if self.dir == self.dirs[0]:
            # self.xpos -= 5
            self.dir = random.choice(self.dirs)

        if self.dir == self.dirs[1]:
            self.xpos -= 5
            self.ypos -= 5
        if self.dir == self.dirs[2]:
            self.xpos -= 5
            self.ypos += 5
        if self.dir == self.dirs[3]:
            # self.xpos += 5
            self.dir = random.choice(self.dirs)

        if self.dir == self.dirs[4]:
            self.xpos += 5
            self.ypos -= 5
        if self.dir == self.dirs[5]:
            self.xpos += 5
            self.ypos += 5


image = pygame.image.load("game_over.png")
image_position = (350, 150)

p1 = Saber("RED", player1_pos)
p2 = Saber("RED", player2_pos)
ball = Ball()
button = Button(500, 20 ,50, 50, 'Restart')


def dir():
    # self.dirs = ['left','topleft','bottomleft','right','topright','bottomright']
    if ball.rect.colliderect(p1.rect):
        ball.dir = random.choice(ball.dirs[3:])
    if ball.rect.colliderect(p2.rect):
        ball.dir = random.choice(ball.dirs[:3])
    if ball.rect.colliderect(up_rect):
        if ball.dir == ball.dirs[4]:
            ball.dir = ball.dirs[5]
        if ball.dir == ball.dirs[1]:
            ball.dir = ball.dirs[2]
    if ball.rect.colliderect(down_rect):
        if ball.dir == ball.dirs[2]:
            ball.dir = ball.dirs[1]
        if ball.dir == ball.dirs[5]:
            ball.dir = ball.dirs[4]


run = True
while run:
    screen.fill("White")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    up = pygame.draw.rect(screen, "black", (0, 0, 1000, 10))
    down = pygame.draw.rect(screen, "black", (0, 490, 1000, 10))
    up_rect = pygame.Rect(up)
    down_rect = pygame.Rect(down)

    if ball.xpos > 0 and ball.xpos < 1000:
        p1.draw()
        p2.draw()
        ball.draw()
    else:
        button.draw(screen, (10, 10, 10))
        screen.blit(image, image_position)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_mouse_over(pygame.mouse.get_pos()):
                ball.xpos = 500
                ball.ypos = 250
                p1.xpos,p1.ypos = player1_pos
                p2.xpos,p2.ypos = player2_pos

    ball.move()
    dir()
    if pygame.key.get_pressed()[pygame.K_w]:
        if p1.rect.top > 10:
            p1.ypos -= 10
    if pygame.key.get_pressed()[pygame.K_s]:
        if p1.rect.bottom < 490:
            p1.ypos += 10
    if pygame.key.get_pressed()[pygame.K_i]:
        if p2.rect.top > 10:
            p2.ypos -= 10
    if pygame.key.get_pressed()[pygame.K_k]:
        if p2.rect.bottom < 490:
            p2.ypos += 10

    pygame.display.update()
    pygame.time.Clock().tick(FPS)

pygame.quit()
