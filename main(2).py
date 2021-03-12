import pygame, sys, random

from pygame.locals import *

pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((1280, 768))
cloud = pygame.image.load("cloud.png").convert_alpha()
scaled_cl = pygame.transform.scale(cloud, (500,350))
hooman = pygame.image.load()
#clock = pygame.time.Clock()

class Raindrop:

    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.speed = random.randint(5,14)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.circle(screen, (150,150,150), (self.x, self.y), 2)


class Cloud:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        self.x += 1

    def draw(self):
        screen.blit(scaled_cl, (self.x, self.y))

    def create_rain(self):
        rain.append(Raindrop(random.randint(self.x + 80, self.x + 480), self.y + 250))


class Hooman:

    def __init__(self):
        self.x = 450
        self.y = 200

rain = []
cloud1 = Cloud(10,50)
cloud2 = Cloud(700,50)

while True:

    #clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_key = pygame.key.get_pressed()

    # Rendering part
    screen.fill((255,255,255))

    cloud1.create_rain()
    cloud2.create_rain()

    for i in rain:
        i.draw()
        i.move()

    cloud1.draw()
    cloud2.draw()
    cloud1.move()
    cloud2.move()


    pygame.display.flip()
    # pygame.display.update()



