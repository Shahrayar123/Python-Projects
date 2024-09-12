import pygame
from pygame.locals import *

#initalizes pygame
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 550

#creates game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 50

ACCELERATION = 0.1

class Ball():
    def __init__(self):
        #inital location of the ball
        self.y = 0
        self.x = ((SCREEN_WIDTH/2)-5)
        
        #inital direction of the ball when the games start
        self.yPlus = 5
        self.xPlus = 5

    def draw(self):
        pygame.draw.circle(screen, (255,255,255), (int(self.x),int(self.y)), 10)
    def move(self):
        #sets location of the ball by 5 in the x and y direction
        self.x += self.xPlus
        self.y += self.yPlus
        
        #sets the bounderies of the screen
        #if the ball hits a bounderies the direction of the x or y is changed
        
        #When the balls x location is greater then the screen width the x movement is reversed
        if self.x > SCREEN_WIDTH:
            self.xPlus = self.xPlus * -1
        #When the balls x location is less then 0 the x movment is reversed
        if self.x < 0:
            self.xPlus = self.xPlus * -1
        #When the balls y location is less than 0 the y movment is reversed
        if self.y < 0:
            self.yPlus = self.yPlus * -1
        #When the balls y location is greater than the screen height the x and y movement is changed to zero and stops (this is game over)
        if self.y > SCREEN_HEIGHT:
            self.xPlus = 0
            self.yPlus = 0
    
    #Reverses the y movement of the ball
    def hitPaddle(self):
        self.yPlus = self.yPlus * -1
    #Returns the y position of the ball
    def getPositionY(self):
        return self.y
    #Returns the x position of the ball
    def getPositionX(self):
        return self.x

class Paddle():
    def __init__(self):
        #Sets the inital x and y position of the paddle
        self.y = (SCREEN_HEIGHT - 80)
        self.x = ((SCREEN_WIDTH/2)-40)
    def draw(self):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x, self.y, 80, 10))
    def move(self):
        
        #Sets the bounderies of the screen to prevent the paddle from moving off of the screen
        if (self.x == SCREEN_WIDTH - 80):
            self.x = self.x - 5
            return
        elif (self.x == 0):
            self.x = self.x + 5
            return
        
        #Moves location of paddle when left and right arrow keys are pressed
        key = pygame.key.get_pressed()    
        if key[pygame.K_RIGHT] == True:
            self.x = self.x + 5
        elif key[pygame.K_LEFT] == True:
            self.x = self.x - 5
    # Returns the x position of the paddle obj
    def getPositionX(self):
        return self.x

         
def bounce(paddle, ball, count): 
    #Created vairables to hold the locations of the ball and paddle objs
    paddle_x = paddle.getPositionX()
    ball_x = ball.getPositionX()
    ball_Y = ball.getPositionY()
    
    #If the ball's y position is at the y position of the paddle
    #then the x position of the ball is check to see if it is with in the max and min x position of the paddle
    #If the ball is with the paddles x positions the function returns true
    if (SCREEN_HEIGHT - 90) < (ball.getPositionY()):
        if ((ball_x < (paddle_x + 80) and ball_x > (paddle_x - 80))):
            count += 1
            return True
        
def game():  
    #Creates a Ball obj
    ball = Ball()
    #Creates a Paddle obj
    paddle = Paddle()
    
    #Creates a variable called font that specifies the type and size of font for text
    #Creates a text and rectangle variable for the rest button
    font =pygame.font.SysFont("Arial", 14)
    text1= font.render(" RESET ", True, (255,255,255))
    rect1 = text1.get_rect(topleft=(10, (SCREEN_HEIGHT - 30)))
    
    #Count variable to keep score of every time the ball touches the paddle
    count = 0
    
    run = True
    #While run remains true the game continues to run
    while run:
        
        #Creates another text and rectangle variable to display the score
        text2 = font.render("Score: " + str(count), True, (255,255,255))
        rect2 = text2.get_rect(topleft = (60,(SCREEN_HEIGHT - 30)))
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
            
            #If mouse is click while over the reset button game() is called starting the game over
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect1.collidepoint(event.pos):
                        game()
        
        #fills the screen with black
        screen.fill((0,0,0))
        
        #combines text1 and rect1 obj to create the reset button
        screen.blit(text1, rect1)
        pygame.draw.rect(screen, (255,0,0),rect1,1)
        
        #combines text2 and rect2 obj that displays the score
        screen.blit(text2, rect2)
        pygame.draw.rect(screen,(255,255,255), rect2, 1)
        
        #displays ball
        ball.draw()
        #starts the balls motion
        ball.move()
        
        #displays the paddle
        paddle.draw()
        #Lets the user move the paddle location to the left or right
        paddle.move()
        
        #Determines if the ball has touched the paddle
        #If the ball is touching the paddle hitPaddle() is called which changes the balls direction
        #Count is increased (which is the score)
        if bounce(paddle, ball, count):
            ball.hitPaddle()
            count = count + 1

        clock.tick(FPS)
        pygame.display.flip()
      
game()
pygame.quit()
 