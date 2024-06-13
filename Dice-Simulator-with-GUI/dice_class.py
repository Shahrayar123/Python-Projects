import pygame 
from utils import generate_circle_points
pygame.init()

width, height = 500, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dice Simulator")

# colors 
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# misc
starting_point_value_x = 0

class Dice:
    def __init__(self, dice_number):
        self.dice_number = dice_number
        self.x = 150
        self.y = 100
        self.width = 200
        self.height = 160
        self.circle_x = 150
        self.circle_y = 150
        self.id = dice_number
        
        self.x_offset = 50
        self.y_offset = 50

    def draw_dice(self):
        pygame.draw.rect(win, GREEN, (self.x, self.y, self.width, self.height),border_radius=30)
        
        '''
        For the first three instances, the dots are displayed on the same line
        The rest will be moved to a separate line. Thus three dots per line
        This makes our 6 faced die (2 x 3)
        '''
        if self.dice_number == 1:
            self.width, self.height = 100, 100
            pygame.draw.circle(win, WHITE, (self.x + self.x_offset, self.y + self.y_offset), 15)

        if self.dice_number == 2:
            self.width, self.height = 150, 100
            points = generate_circle_points(starting_point_value_x, self.dice_number)
            for i in range(self.dice_number):
                pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y), 15)                               

        if self.dice_number == 3:
            self.height = 100
            points = generate_circle_points(starting_point_value_x, self.dice_number)
            for i in range(self.dice_number):
                pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y), 15)

        '''
        From four to six, the dots are moved to the next line
        This is done by a y-offset value on the circle/dot position
        '''
        if self.dice_number == 4:
            '''
            For the self.dice_number = 5, we repeat the "self.dice_number = 3" once 
            and the "self.dice_number == 2" once 
            '''
            self.width = 150
            points = generate_circle_points(starting_point_value_x, 3)
            for i in range(2):
                # This is the same as "self.dice_number = 3" but on the first horizontal line at y = 100
                pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y), 15)
                for _ in range(2):
                    # This is the same as self.dice_number = 3 but on the second horizontal line 
                    pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y + self.y_offset), 15)

        if self.dice_number == 5:
            '''
            For the self.dice_number = 5, we repeat the "self.dice_number = 3" once 
            and the "self.dice_number == 2" once 
            '''
            points = generate_circle_points(starting_point_value_x, 3)
            for i in range(3):
                # This is the same as "self.dice_number = 3" but on the first horizontal line at y = 100
                pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y), 15)
                for i in range(2):
                    # This is the same as self.dice_number = 3 but on the second horizontal line at y = 100 + self.y_offset
                    pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y + self.y_offset), 15)

        if self.dice_number == 6:
            '''
            For the self.dice_number = 5, we repeat the "self.dice_number = 3" twice
            but one on a different y value  
            '''
            points = generate_circle_points(starting_point_value_x, 3)
            for i in range(3):
                # This is the same as "self.dice_number = 3" but on the first horizontal line at y = 100
                pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y), 15)
                for i in range(3):
                    # This is the same as self.dice_number = 3 but on the second horizontal line at y = 100 + self.y_offset
                    pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y + self.y_offset), 15)



    
if __name__ == '__main__':
    print("***Challenge from Tik Tok")
    

        



        