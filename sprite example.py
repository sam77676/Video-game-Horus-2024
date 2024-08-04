# Program : Horus Video Game
# Author : Samuel Austin
# Date 04/07/2024
# Version 1.0

# TODO: # create a game interface / Menu to start the game

# this makes pygame referred to as p
import pygame as p, sys

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

    
    # This updates the sprite and moves it to the right
    def update(self):
        self.speedx = 0
        keystate = p.key.get_pressed()
        if keystate[p.K_LEFT]:
            self.speedx = -5
        if keystate[p.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <0:
            self.rect.left = 0

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

# This puts all of the sprites into one group to reduce the length of the update and the draw section

all_sprites = p.sprite.Group()
player = Player()
all_sprites.add(player)
#---------------------END OF SET UP------------------------#

#--------------------MAIN GAME LOOP------------------------#

#While true means while the game is running this code will run

#Setting a variable for when the game is running and using it in the main game loop
running = True
while running:

    #Keep the loop running at the correct speed 
    clock.tick(FPS)
    #Process events
    for event in p.event.get():
        # Check for closing of the window and if true closes the program
        if event.type == p.QUIT:    
            running = False 

    #Update
    all_sprites.update()


    #Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # This makes what's drawn in the code is flipped onto the display instead of having to redraw every frame.
    p.display.flip()
