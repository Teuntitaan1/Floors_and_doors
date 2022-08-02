from cmath import inf
from random import random
from entities import entity
from components import *
from random import randint
def playertemplate(gameinfo, x, y, width, height, color = (255,255,255)):
    
    player = entity(gameinfo, x, y, width, height)
    player.addcomponent(renderingsystem(player, pygame.Rect((player.x, player.y), (player.width, player.height)), color), "renderingsystem")
    player.addcomponent(movementsystem(player, 300), "movementsystem")
    player.addcomponent(physicssystem(player, 1), "physicssystem")
    player.addcomponent(collider(player), "collider")
    player.addcomponent(collidersystem(player), "collidersystem")

    return player

def walltemplate(gameinfo, x = randint(0, 800), y = randint(0, 800), width = randint(10, 60), height = randint(10, 60), color = (255,255,255)):
    
    wall = entity(gameinfo, x, y, width, height)
    wall.addcomponent(renderingsystem(wall, pygame.Rect((wall.x, wall.y), (wall.width, wall.height)), color), "renderingsystem")
    wall.addcomponent(collider(wall), "collider")
    wall.addcomponent(collidersystem(wall), "collidersystem")

    return wall