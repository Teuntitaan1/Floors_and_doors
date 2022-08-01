from components import *
from gameinfo import GameInfo
from entities import entity
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
player = entity(gameinfo, 100, 100, 50, 50)
player.addcomponent(renderingsystem(player, pygame.Rect((player.x, player.y), (player.width, player.height)), (255,255,255)), "renderingsystem")
player.addcomponent(movementsystem(player, 300), "movementsystem")
player.addcomponent(physicssystem(player, 1), "physicssytem")

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
    player.update()

    # screen updates
    clock.tick(refreshrate)
    pygame.display.update()
    gameinfo.frameselapsed += 1

# exit statement
print(f"Game shut down after {gameinfo.frameselapsed} frames")
    

