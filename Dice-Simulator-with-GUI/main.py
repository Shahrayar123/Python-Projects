from dice_class import Dice, BLACK, win
import pygame 
import random  

pygame.init()

clock = pygame.time.Clock()
FPS = 60

title = "Dice Simulator"
font = pygame.font.SysFont('Comicsans', 32)
WHITE = (255, 255, 255)

def show_text(text, x, y):
    message = font.render(text, False, WHITE)
    win.blit(message, (x, y))
    

def main():
    run = True

    d1, d2, d3, d4, d5, d6 = Dice(1), Dice(2), Dice(3), Dice(4), Dice(5), Dice(6)

    while run:
        show_text(title, 150, 10)
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

        # check for key presses 
        key_pressed = pygame.key.get_pressed()
        numbers = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_r]
        dr = Dice(random.randint(1, 6))
        dices = [d1, d2, d3, d4, d5, d6, dr]

        try:
            for i in range(len(numbers)):
                if key_pressed[numbers[i]]:
                    win.fill(BLACK)
                    dices[i].draw_dice()
                    show_text(str(dices[i].dice_number), 250, 300)
                    print(f"Dice {dices[i].dice_number}")
        except:
            pass 
                
        pygame.display.update()
    
if __name__ == '__main__':
    main()