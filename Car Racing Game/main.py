import pygame
import random

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
CAR_WIDTH = 80
CAR_HEIGHT = 160
ROAD_WIDTH = 600
FPS = 60
WHITE = (255, 255, 255)

class Car:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
        self.y = SCREEN_HEIGHT - CAR_HEIGHT - 10
        self.speed_x = 0
        self.speed_y = 0
        self.image = pygame.transform.scale(pygame.image.load('car_nfs.png'), (CAR_WIDTH, CAR_HEIGHT))

    def move_left(self):
        if self.x > SCREEN_WIDTH // 4 - CAR_WIDTH:
            self.speed_x = -5

    def move_right(self):
        if self.x < SCREEN_WIDTH // 2:
            self.speed_x = 5

    def move_forward(self):
        self.speed_y = -5

    def move_backward(self):
        self.speed_y = 5

    def stop_x(self):
        self.speed_x = 0

    def stop_y(self):
        self.speed_y = 0

    def update_position(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Road:
    def __init__(self):
        self.y = 0
        self.speed = 5
        self.image = pygame.image.load('road_nfs.jpg')
        self.image = pygame.transform.scale(self.image, (ROAD_WIDTH, SCREEN_HEIGHT))

    def move(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = 0

    def draw(self):
        screen.blit(self.image, (SCREEN_WIDTH // 4, self.y))
        screen.blit(self.image, (SCREEN_WIDTH // 4, self.y - SCREEN_HEIGHT))

class HurdleManager:
    def __init__(self):
        self.hurdles = []
        self.speed = 5

    def create_hurdle(self):
        size = random.randint(20, 50)
        x = random.randint(SCREEN_WIDTH // 4, SCREEN_WIDTH // 2 - size)
        y = -size
        self.hurdles.append(pygame.Rect(x, y, size, size))

    def move_hurdles(self):
        for hurdle in self.hurdles:
            hurdle.y += self.speed
            if hurdle.y > SCREEN_HEIGHT:
                self.hurdles.remove(hurdle)

class Game:
    def __init__(self):
        self.car = Car()
        self.road = Road()
        self.hurdle_manager = HurdleManager()
        self.score = 0
        self.play_background_music()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.car.move_left()
        if keys[pygame.K_RIGHT]:
            self.car.move_right()
        if keys[pygame.K_UP]:
            self.car.move_forward()
        if keys[pygame.K_DOWN]:
            self.car.move_backward()

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.car.stop_x()
        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.car.stop_y()

    def update_score(self):
        self.score += 1

    def display_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(self.score), True, WHITE)
        screen.blit(score_text, (10, 10))

    def run(self):
        clock = pygame.time.Clock()

        while True:
            self.handle_events()

            self.road.move()

            screen.fill((0, 0, 0))
            self.road.draw()

            self.hurdle_manager.create_hurdle()
            self.hurdle_manager.move_hurdles()
            self.car.update_position()
            self.car.draw()
            self.display_score()

            self.car.speed_x = self.road.speed * 2
            self.car.speed_y = self.road.speed * 2
            self.hurdle_manager.speed = self.road.speed * 1.5

            self.update_score()

            pygame.display.update()
            clock.tick(FPS)

    def play_background_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load('background_music.wav')
        pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Need for Speed - Car Racing Game")

# Run the game
game = Game()
game.run()
