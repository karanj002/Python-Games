import pygame
import sys
import math

from pygame.locals import *
pygame.init()

WINDOW = pygame.display.set_mode((900, 700))

COLOUR2 = (32,59,202)
COLOUR = (0,180,0)
COLOUR3 =(1,234,254)
WINDOW.fill(COLOUR)

keys=pygame.key.get_pressed()
y=100    
z=100    
x=100    
FPS=70
fpsClock=pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def _init_(self):
        super().  __init__()

    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.Surface([20,20])
    self.image.fill(COLOUR2)
    self.rect=self.image.get_rect()
    player.rect.x=20


#Defines what a pygame bullet is.
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().  __init__()

        self.image=pygame.Surface
        self.image.fill(COLOUR2)
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.y-=3

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().  __init__()

    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.Surface([20,20])
    self.image.fill(COLOUR2)
    self.rect=self.image.get_rect()
    player.rect.x=20

all_sprites_list=pygame.sprite.Group()#List of all the sprites
bullets_lis=pygame.sprite.Group()#List of all the bullets
player=Player()#Creates a player sprite and adds it to the small sprite list
all_sprites_list.add(player)#Adds the players to the list

while True:                 

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()

    #Makes Player character move right by pressing "d" 
    if keys[pygame.K_d]:
        x=x+3
        if x> 900:
            x=900
    #Makes player character move left by pressing "a"
    if keys[pygame.K_a]:
        x=x-3
        if x<0:
            x=0
    #Makes bullets shoot out of player character by pressing *space*
    if keys[pygame.K_SPACE]:
        bullet=Bullet()
        bullet.rect.x=player.rect.x
        bullet.rect.y=player.rect.y
        all_sprites_list.add(bullet)
        bullet_list.add(bullet)

    pygame.display.update()
#Updates all sprites (makes them move)
    all_sprites_list.update()
#Draws all the sprites
    all_sprites_list.draw(WINDOW)

    pygame.display.flip()


    fpsClock.tick(FPS)
