# Program : Horus Video Game
# Author : Samuel Austin
# Date 04/07/2024
# Version 1.0

# TODO: # create a game interface / Menu to start the game

# this makes pygame referred to as p
import pygame as p, sys
import random
import os
import time

# -------------SET UP-----------------#
#This tells pygame to set up a window for the game and gives the needed dimensions of the window
WIDTH = 800
HEIGHT = 600
# this sets the frames per second the game runs at
FPS = 30

# Useful colours as variables for ease of use
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# sets a caption for the window
p.display.set_caption("Menu")

# Initializes pygame
p.init()

# Initializes the sound mixer
p.mixer.init()

# This tells pygame to create the window and use the given dimensions and specifications. 
screen =  p.display.set_mode((WIDTH, HEIGHT))

# Sychronizes pygame with computer clock
clock = p.time.Clock()

class Player(p.sprite.Sprite):  
    #sprite for the player
    def __init__(self):
        p.sprite.Sprite.__init__(self)
        # self.image is the image that the sprite uses 
        self.image = p.Surface((50, 50))
        self.image.fill(GREEN) 
        # self.rect is the rectangle / hitbox of the sprite
        self.rect = self.image.get_rect() 
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    # This updates the sprite and moves it to the right
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = p.key.get_pressed()
        if keystate[p.K_LEFT]:
            self.speedx = -5
        if keystate[p.K_RIGHT]:
            self.speedx = 5
        if keystate[p.K_UP]:
            self.speedy = -5
        if keystate[p.K_DOWN]:
            self.speedy = 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <0:
            self.rect.left = 0
        if self.rect.top <0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top) # 
        all_sprites.add(bullet)
        bullets.add(bullet)
        
# creating a bullet sprite / class
class Bullet(p.sprite.Sprite):
    def __init__(self, x, y):
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface ((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        

    def update(self):
        self.rect.y += self.speedy
        # Kill if it moves off of the screen
        if self.rect.bottom < 0:
            self.kill()





# Creating a sprite for the enemy mobs / sprites
class Mob(p.sprite.Sprite):
    def __init__(self):
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1,8)
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,8)

# This puts all of the sprites into one group to reduce the length of the update and the draw section

all_sprites = p.sprite.Group()
mobs = p.sprite.Group() 
bullets = p.sprite.Group()
player = Player()
all_sprites.add(player)
all_sprites.add(mobs)
for i in range(10):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


#---------------------END OF SET UP------------------------#

#--------------------MAIN GAME LOOP------------------------#

#While true means while the game is running this code will run
global lives
lives = 3

#Setting a variable for when the game is running and using it in the main game loop
running = True
while running:
    lives = 3
    #Keep the loop running at the correct speed 
    clock.tick(FPS)
    #Process events
    for event in p.event.get():
        # Check for closing of the window and if true closes the program
        if event.type == p.QUIT:    
            running = False 
        elif event.type ==p.KEYDOWN:
            if event.key ==p.K_SPACE:
                player.shoot()
        
        if event.type == p.KEYDOWN:
            if event.key == p.K_ESCAPE:
                running = False


    #Update
    all_sprites.update()

    # check if a mob hit the player (Collisions)
    hits = p.sprite.spritecollide(player, mobs, False)
    if hits:
        print("Player hit")
        
        #running = False 


    #mob_hits = p.sprite.spritecollide(bullets, mobs, False)
    #if mob_hits:
    #    print("mob hit")
        
        
       

    #Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # This makes what's drawn in the code is flipped onto the display instead of having to redraw every frame.
    p.display.flip()
    
