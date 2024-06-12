coloured = True if input("Do you want a colored ascii image? [Y/N] >>").lower() in ['y', "yes"] else False
import pygame
from os import system
def cls():
    system("cls")
cls()
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Image to ASCII")
running = True
clock = pygame.time.Clock()
image = pygame.transform.scale(pygame.image.load("<Enter the Image Path here>"), (200, 96))  
#x and y must be in a ratio of eaither 200:96, or 603:203 depending upon the maxnification because the length and breadth of a character is unequal
screen.blit(image, (0, 0))

chars = '█▓▒$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i! lI;:,"^`\'. ' 
#list of characters arranged according to the brightness
x = 0
y = 0
sentence = ""
#stores the sequence of characters according to colour and intensity of all pixel
while running == True:
    clock.tick(6000)  #increasing the framerate to increase the speed of printing the image
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if the user clicks on the cross button at top right corner then exit the program
            running = False
    if x < 200 and y < 200:
        pxlColor = screen.get_at((x, y))[:3] 
        #gives the colour of the pixel at position (x, y) in RGBA
        #slicing the list to obtain RGB value and neglecting the alpha value
        intensity = (sum(pxlColor))/len(pxlColor) #average of R, G, B components which gives us brightness of colour intensity at the pixel
        if coloured == True:
            try:
                Ratio = [round((pxlColor[0]/max(pxlColor))-0.2), round((pxlColor[1]/max(pxlColor))-0.2), round((pxlColor[2]/max(pxlColor))-0.2)]
                #The ratio in which all three colours are there
            except:
                Ratio = [0, 0, 0] #If there is 0 division error means that the colour is black
                sentence += "\33[90m"

            if Ratio == [0, 0, 1]: #if colour is blue
                sentence += "\33[34m"
            elif Ratio == [0, 1, 0]: #if colour is green
                sentence += "\33[32m"
            elif Ratio == [0, 1, 1]: #if colour is cyan
                sentence += "\33[36m"
            elif Ratio == [1, 0, 0]: #if colour is red
                sentence += "\33[31m"
            elif Ratio == [1, 0, 1]: #if colour is violet
                sentence += "\33[35m"
            elif Ratio == [1, 1, 0]: #if colour is yellow
                sentence += "\33[33m"
            elif Ratio == [1, 1, 1]: #if colour is white
                sentence += "\33[37m"

            sentence += "\33[1m" + chars[int(-(intensity/255)*(len(chars)-1))-1] 
            #arranging the intensity/brightness according to the length of list to get the character at the given intensity/brightness
        else:
            sentence += chars[int(-(intensity/255)*(len(chars)-1))-1]
            #arranging the intensity/brightness according to the length of list to get the character at the given intensity/brightness
        x += 1 #after every character is blitted we increase x value

    elif x >= 200:
        x=0
        y+=1 
        #if 200 characters are blitted means the entire line is  blitted so increase the y value by one. Means the next line has started
        if sentence != "":
            #if the sentence isn't empty means there are all black coloured pixels at that location
            print(sentence)
            #print the sentence
            sentence = ""
            #reset it to empty for the next line
    pygame.display.update()
