
from pygame import *
import random

#set canvas size variables
width = 700
height = 450

#draw canvas
screen = display.set_mode((width,height))
display.set_caption('Graphics')

#initial XY coordinates where game starts
x = random.randint(1, width)
y = random.randint(1, height)

#import logo
logo_img = image.load('dvd_logo_alpha.png')
R = 255
G = 255
B = 255

def logo(x, y, color):
    tintImage = logo_img.convert_alpha()
    tintImage.fill((R, G, B, 255), None, BLEND_RGBA_MULT)
    screen.blit(tintImage, (x, y))

#speed of the logo
dx = 3
dy = 3

endProgram = False
while not endProgram:
    for e in event.get():
        if e.type == QUIT:
            endProgram = True

    #speed changes position XY
    x += dx
    y += dy

    #detection of collision with border of screen
    if y<0 or y>height-47:
        dy *= -1
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
    if x<0 or x>width-107:
        dx *= -1
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)

    screen.fill((0))

    logo(x, y, (R, G, B))

    display.update()
