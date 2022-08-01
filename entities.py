import pygame
from components import *
        
# template for everything in the game, can be customized via components added in components.py
class entity(pygame.sprite.Sprite):
    def __init__(self, gameinfo, x, y, width, height):

        # inherits all functionality from pygame.sprite.Sprite
        super().__init__()
        
        # needs to be present for every component, acts as a global class full of game information such as deltatime and gravity
        self.gameinfo = gameinfo
        # x and y coord on the screen, 0 is topleft
        self.x = x
        self.y = y
        # width and height variables for scaling the entity
        self.width = width
        self.height = height
        # a dictionary consisting of every component present in this entity, can be added and removed in runtime
        self.components = {}
    #
    #
    #  goes over every component in the dictionary and calls their respective update()  
    def update(self):
        
        components = self.components.keys()
        for component in components:
            self.components[component].update()
    #
    #
    #
    def addcomponent(self, componentclass, componentname):
        
        if componentname not in self.components.keys():
            self.components[componentname] = componentclass
            print(f"Added component: {componentname} to entity {self}")
        else:
            raise Exception("This component is already attached to this object")
    #
    #
    #
    def deletecomponent(self, componentname):
        
        if componentname in self.components.keys():
            self.components.pop(componentname)
            print(f"Removed component: {componentname} from entity {self}")
    #
    #
    #
    def getcomponent(self, componentname):
        
        if componentname in self.components.keys():
            return self.components[componentname]
        else:
            raise Exception("This component is not attached to this object")
    
        
    