import pygame
import time
import random
import os

pygame.init()

display_width = 400
display_height = 600

button_start_x = 75
new_game_y = 400
quit_y = 460
button_width = 242
button_height = 50

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
redLight = (255, 21, 21)
gray = (112,128,144)
green = (0,255,0)
greenLight = (51, 255, 51)
blue = (0,0,255)

gameDisplay= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('F1 RaceRoad')
clock=pygame.time.Clock()

carImg = pygame.image.load(os.getcwd()+'\\car.png')
carLeft = pygame.image.load(os.getcwd()+'\\car_left.png')
carRight = pygame.image.load(os.getcwd()+'\\car_right.png')
obstacle_Img = pygame.image.load(os.getcwd()+'\\obstacle.png')
textur = pygame.image.load(os.getcwd()+'\\texture.png')
(car_width,car_height) = carImg.get_rect().size
(carL_width,carL_height) = carLeft.get_rect().size
(carR_width,carR_height) = carRight.get_rect().size
(thing_width,thing_height) = obstacle_Img.get_rect().size
(texture_width, texture_height) = textur.get_rect().size

logo = pygame.image.load(os.getcwd()+'\\logo.png')
pygame.display.set_icon(logo)

background = pygame.image.load(os.getcwd()+'\\background.png')
background_still = pygame.image.load(os.getcwd()+'\\background_inv.png')
backgroundRect = background.get_rect()

intro_1 = pygame.mixer.Sound(os.getcwd()+'\\intro1.wav')
intro_2 = pygame.mixer.Sound(os.getcwd()+'\\intro2.wav')
crash_sound = pygame.mixer.Sound(os.getcwd()+'\\car_crash.wav')
ignition = pygame.mixer.Sound(os.getcwd()+'\\ignition.wav')
pygame.mixer.music.load(os.getcwd()+'\\running.wav')

def things_dodged(count, high_score, thing_speed):
	font = pygame.font.SysFont(None, 25)
	score = font.render("Dodged: "+str(count), True, green)
	highscore = font.render("High Score: "+str(high_score), True, green)
	speed = font.render("Speed: "+str(thing_speed)+"Km/h", True, green)
	gameDisplay.blit(score, (10,0))
	gameDisplay.blit(highscore, (10,27))
	gameDisplay.blit(speed, (display_width - 125,0))

def high_score_update(dodged):
	hs = open(os.getcwd()+'\\high_score.txt', 'w')
	temp = str(dodged)
	hs.write(temp)

def things(thingx, thingy):
	gameDisplay.blit(obstacle_Img,(thingx,thingy))

def car(x,y,dir):
	if dir==0:
		gameDisplay.blit(carImg,(x,y))
	if dir==-1:
		gameDisplay.blit(carLeft,(x,y))
	if dir==1:
		gameDisplay.blit(carRight,(x,y))

def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

def message_display(text, shift_x, shift_y, color, sleep_time):
	largeText = pygame.font.Font('freesansbold.ttf',50)
	TextSurf, TextRect = text_objects(text, largeText, color)
	TextRect.center = ((display_width/2 - shift_x),(display_height/2 - shift_y))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()
	time.sleep(sleep_time)

def title_msg(shift_x, shift_y, color):
	largeText = pygame.font.Font('freesansbold.ttf',60)
	TextSurf, TextRect = text_objects("F1 RaceRoad", largeText, color)
	TextRect.center = ((display_width/2 - shift_x),(display_height/3 - shift_y))
	gameDisplay.blit(TextSurf,TextRect)
	time.sleep(0.15)
	pygame.display.update()

def title():
	height_anim=display_height
	pygame.mixer.Sound.play(intro_1)
	while height_anim > -600:
		gameDisplay.fill(white)
		things(display_width/2 - thing_width/2, height_anim)
		height_anim-=1.5
		pygame.display.update()
	title_msg(0,0,black)
	time.sleep(0.1)
	pygame.mixer.Sound.play(intro_2)

def motion_texture(thing_starty):
	gameDisplay.blit(textur,(0,thing_starty -400))
	gameDisplay.blit(textur,(0,thing_starty))
	gameDisplay.blit(textur,(0,thing_starty +400))

def crash():
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(crash_sound)
	message_display("YOU CRASHED", 0, 0, red,0)
	while True:
		play = button("Play Again", button_start_x, new_game_y, button_width, button_height, greenLight, green)
		quit_game = button("Quit", button_start_x, quit_y, button_width, button_height, redLight, red)
		for event in pygame.event.get():
			if event.type == pygame.QUIT or quit_game == 1 or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				quit()
			if play== 1 or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
				game_loop()
		pygame.display.update()
		clock.tick(15)

def button(msg, x, y, w, h, inactive_color, active_color, action=None):

	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x + w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, active_color, (x, y, w, h))
		if click[0] == 1:
			return 1
	else:
		pygame.draw.rect(gameDisplay, inactive_color, (x, y, w, h))

	smallText = pygame.font.Font('freesansbold.ttf',20)
	TextSurf, TextRect = text_objects(msg, smallText, white)
	TextRect.center = ((x + w/2),(y + h/2))
	gameDisplay.blit(TextSurf,TextRect)
#brought to you by code-projects.org
def game_intro():
	intro = True
	gameDisplay.fill(white)
	title()
	quit_game=0
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or quit_game == 1 or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				quit()
		play = button("New game", button_start_x, new_game_y, button_width, button_height, greenLight, green)
		quit_game = button("Quit", button_start_x, quit_y, button_width, button_height, redLight, red)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quit_game = 1
		if play or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
			intro = False

		pygame.display.update()
		clock.tick(15)
######################### count down at start
def count_321():
	count = 3
	pygame.mixer.music.pause()
	pygame.mixer.Sound.play(ignition)
	while count >= 0:
		gameDisplay.blit(background, backgroundRect)
		car(display_width * 0.40,display_height * 0.6,0)
		if count == 0:
			message_display ("GO!", 0, 0 , green, 0.75)
			pygame.mixer.music.play(-1)
		else:
			message_display (str(count), 0, 0 , red, 0.75)
		count -= 1
	clock.tick(15)

def pause():
	pygame.mixer.music.pause()
	pause = True
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  ###############or quit_game == 1
				pygame.quit()
				quit()
			message_display("pause", 0, 0, blue,1.5)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pygame.mixer.music.unpause()
					return
		pygame.display.update()
		clock.tick(15)


def game_loop():

	pygame.mixer.music.play(-1)
	disp = 0
	x=(display_width * 0.4)
	y=(display_height * 0.6)
	x_change=0

	thing_startx = random.randrange(8, display_width-thing_width-8)
	thing_starty = -600
	thing_speed = 5

	track_y = 0
	track_speed = 25

	dodged=0
	dir = 0

	high_score_file = open(os.getcwd()+'/high_score.txt','r')
	high_score = high_score_file.read()

	gameExit = False

	count_321()

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					x_change = -10
					dir = -1
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					x_change = 10
					dir = 1
				if event.key == pygame.K_SPACE:
					pause()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
					x_change = 0
					dir = 0
		x+=x_change
		gameDisplay.blit(background, backgroundRect)

		motion_texture(thing_starty)

		things(thing_startx, thing_starty)
		thing_starty += thing_speed

		car(x,y,dir)

		things_dodged(dodged, high_score, thing_speed)
############# wall collision #############################
		if x > display_width - car_width or x < 0:
			crash()
##################### dodge ##############################
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)
			dodged += 1
			thing_speed += 1
		if dodged > int(high_score):
			high_score_update(dodged)
############# obstacle collision ##########################
		if y < thing_starty+thing_height-15 and x > thing_startx-car_width-5 and x < thing_startx+thing_width-5:
			crash()

		pygame.display.update() # pygame.display.flip() #alternative
		clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
