import pygame
from components import *

class Player(pygame.sprite.Sprite):
    def __init__(self, gameinfo, x, y):

        super().__init__()

        # an instance of a class that stores information across classes, must be present on every entity
        self.gameinfo = gameinfo
        # x and y coord on the screen, 0 is topleft
        self.x = x
        self.y = y
        # width and height variables for scaling the entity
        self.height = 50
        self.width = 50
        # sprite rendering system
        self.sprite = pygame.Rect((self.x, self.y), (self.width, self.height)) #pygame.image.load("PygameGame\sprites\CatSprite.jpg").convert()
        self.renderingsystem = renderingsystem(self, self.sprite, (255,255,255))
        # movement system
        self.movementspeed = 300
        self.movementsystem = movementsystem(self, self.movementspeed)
        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])
        # color of the sprite
        self.color = (255, 255, 255)
        # player health component
        self.healthsystem = healthsystem(self, 100, 1, 120)

    def update(self):
        
        self.renderingsystem.render()
        self.healthsystem.update()
        self.movementsystem.handlemovement()
        # uncomment for cool animation
        # self.healthsystem.update()
        

