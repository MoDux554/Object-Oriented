import os
import pygame,sys, random
from pygame.locals import *

#initialising and creating the screen for the pygame program
pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((1280, 768)) #screen resolution

#loading images
cloud = pygame.image.load(os.path.join('images', 'cloud.png')).convert_alpha()
resize_cloud = pygame.transform.scale(cloud, (500, 325)) #changing the size of the cloud
human = pygame.image.load(os.path.join('images', 'hooman with umbrella.png')).convert_alpha()
clock = pygame.time.Clock


screenwidth = 1280
screenlength = 768

ypos = 100

class Rain:
    def __init__(self):
        self.xposition = random.randint(0, 1280) #helpful for when the raindrops/snow is being duplicated from the for loop
        self.yposition = 100
        self.size = random.randint(1, 5) # size of the drawn circle
        self.speed = random.randint(1,15)

    def draw(self): #creates the circle
        pygame.draw.circle(screen,(255,255,255), (self.xposition, self.yposition), self.size)

    def move(self): #moves the circles down
        self.yposition += self.speed #moves the rain in the y position downwards


raindroplist = [] #this is for adding in more than one snow object


canmoveright = True
canmoveleft = True
circle1xpos = 1200
circle1ypos = 700
circle2xpos = 10
circle2ypos = 700
humanxpos = 100
humanypos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #checking for input
    pressed_key = pygame.key.get_pressed()

    #rendering/#colour
    screen.fill((100, 100, 100))

    screen.blit(human, (humanxpos ,humanypos))

    screen.blit(resize_cloud, (100, 50) ) #copies the cloud's pixels onto the pygame screen surface

    first_circle = pygame.draw.circle(screen, (192, 192, 192), (circle1xpos,circle1ypos), 20)
    second_circle = pygame.draw.circle(screen, (192, 192, 192), (circle2xpos, circle2ypos), 20)

    raindrop = Rain()
    raindroplist.append(raindrop)
    for droplet in raindroplist:
        if droplet.yposition >= screenlength:
            raindroplist.remove(droplet)
        else:
            droplet.draw()
            droplet.move() #this allows the raindrops to fall to begin with as at the start they will not be at the bottom


    if pressed_key[K_RIGHT] and canmoveright:
        humanxpos+=1
        canmoveleft = True
        if humanxpos == circle1xpos:
            canmoveright = False
        elif humanxpos < circle1xpos:
            canmoveright = True

    elif pressed_key[K_LEFT] and canmoveleft:
        humanxpos-=1
        canmoveright = True
        if humanxpos == circle2xpos:
            canmoveleft = False
        elif humanxpos > circle2xpos:
            canmoveleft = True



    pygame.display.flip() #updates everytime



