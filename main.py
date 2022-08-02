from components import *
from gameinfo import GameInfo
from entitytemplates import playertemplate, walltemplate
import pygame
import time



pygame.init()

# Pygame window setup
screen = pygame.display.set_mode((800, 800))
refreshrate = 60
clock = pygame.time.Clock()
pygame.display.set_caption("Starlit")

# gameinfo object
gameinfo = GameInfo(screen)
# game objects
player = playertemplate(gameinfo, 100, 100, 50, 50)

wall = walltemplate(gameinfo, 100, 200, 7000, 60)
wall2 = walltemplate(gameinfo, 300, 160, 120, 200)

gameinfo.entitylist.append(player)
gameinfo.entitylist.append(wall)
gameinfo.walllist.append(wall)
gameinfo.entitylist.append(wall2)
gameinfo.walllist.append(wall2)

# game variables
Running = True
Lastframe = time.time()
# main loop
while Running:

    # deltatime implementation
    Currentframe = time.time()
    deltatime = Currentframe - Lastframe
    Lastframe = Currentframe
    gameinfo.deltatime = deltatime
    
    
    # clears the screen
    screen.fill((0, 0, 0))

    # event listener
    for event in pygame.event.get():
        # exit checker
        if event.type == pygame.QUIT:
            Running = False
    
    # entity updates
    gameinfo.update()

    # screen updates
    clock.tick(refreshrate)
    pygame.display.update()
    gameinfo.frameselapsed += 1

# exit statement
print(f"Game shut down after {gameinfo.frameselapsed} frames")
    

