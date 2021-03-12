import os
import pygame,sys, random,time
from pygame.locals import *

#initialising and creating the screen for the pygame program
pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((1280, 768)) #screen resolution

screenwidth = 1280
screenlength = 768

ypos = 100

#loading images
clock = pygame.time.Clock()
playerSprite = pygame.image.load(os.path.join('images', 'PlayerSpaceShip.png')).convert_alpha()
playerBullet = pygame.image.load(os.path.join('images', 'EnemyBullet.png')).convert_alpha()
alienEnemy01 = pygame.image.load(os.path.join('images', 'EnemyShip.png')).convert_alpha()
alienEnemy01HitBox = alienEnemy01.get_rect() #this will draw a collider/hit box around the enemy's shape
background = pygame.image.load(os.path.join('images', 'backgrounds_stars.jpg')).convert_alpha()



class Player:
    def __init__(self):
        self.xpos = 50
        self.ypos = 886-192
        self.hitBox = playerSprite.get_rect(topleft=(self.xpos, self.ypos)) #draws a hitbox around the player's shape

    def drawplayer(self):
        screen.blit(playerSprite, (self.xpos,self.ypos))
        self.hitbox = playerSprite.get_rect(topleft=(self.xpos, self.ypos))

    def moveplayer(self): #checks for the input of either the left or right key
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.xpos -= 5
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.xpos += 5

    def fire(self): #for making the bullets, need to make alist outside of the class for this
        bulletInstance = Bullets(self.xpos + self.hitbox.width / 2, self.ypos)
        bullets.append(bulletInstance)

class Enemy:
    def __init__(self, x, y, colour):
        self.xpos = x
        self.ypos = y
        self.size = random.randint(1,5)
        self.startspeed = random.uniform(0.05, 0.1)
        self.velocity = random.uniform(0.05, 0.2)
        self.speed = self.startspeed
        self.colour = colour
        self.hitBox = alienEnemy01.get_rect(topleft=(self.xpos, self.ypos))


    def draw(self): #drawing the enemy on the screen and its hitbox
        screen.blit(alienEnemy01, (self.xpos, self.ypos))
        self.hitbox = alienEnemy01.get_rect(topleft=(self.xpos, self.ypos))


    def move(self): #moves the circles down
        self.ypos += self.speed + self.velocity
        self.velocity += 0.05

class Bullets:

    def __init__(self,x,y):
        self.xpos = x
        self.ypos = y
        self.startSpeed = -20 #so that the bullet moves upwards not downwards
        self.hitBox = playerBullet.get_rect(topleft=(self.xpos,self.ypos))

    def draw(self): #drawing the bullets on the screen and their hitboxes
        screen.blit(playerBullet, (self.xpos,self.ypos))
        self.hitbox = playerBullet.get_rect(topleft=(self.xpos,self.ypos))

    def move(self):
       bullet.ypos +=self.startSpeed





playerInstance = Player() #refers to the player class above
playerLives = 3

timeSinceLastBullet = 0
timeSinceLastEnemy = 0

Score = 0
bullets = []
enemies = []

while True:
    clock.tick(60) #fps 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key ==pygame.K_SPACE:
            playerInstance.fire()
    #checking for input
    pressed_key = pygame.key.get_pressed()

    #rendering/#colour
    screen.fill((150, 150, 150))
    screen.blit(background, (0, 0))

    if playerInstance.xpos >=(screenwidth - 119):
        playerInstance.xpos = (screenwidth -119) #when the player's posistion is close to the edge it will be stopped
    elif playerInstance.xpos <= -30:
        playerInstance.xpos = -30
    playerInstance.moveplayer()
    playerInstance.drawplayer()

    if time.time() - timeSinceLastEnemy > 3:
        enemy = Enemy(random.randint(0,screenwidth),0,(100, 100, 100))
        enemies.append(enemy)
        timeSinceLastEnemy = time.time()



    for bullet in bullets[:]:
        for enemyInstance in enemies[:]:
            if bullet.hitBox.colliderect(enemyInstance.hitBox): #checks for a collision between the bullet and enemy hitboxes
                bullets.remove(bullet) #remove the bullet after colliding
                enemies.remove(enemyInstance) #removes/kills the enemy after colliding

            else: #if it hits nothing it will still be on the screen
                bullet.move()
                bullet.draw()

    for enemyInstance in enemies[:]:
        if playerInstance.hitBox.colliderect(enemyInstance.hitBox):
            playerLives -= 1
            enemies.remove(enemyInstance) #removes the enemy after colliding with the player

        if enemyInstance.ypos >= screenlength:
            enemies.remove(enemyInstance) #removes the enemy after reaching the end of the screen vertically
        else: #while they are not at the end, they will still be on the screen and moving
            enemyInstance.draw()
            enemyInstance.move()


    pygame.display.flip() #updates everytime



