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
        self.hidden = False
        # animator
        self.animationsystem = animationsystem(self, "PygameGame\playeranimations")
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
        self.animationsystem.update()
        self.healthsystem.update()
        self.movementsystem.handlemovement()
        # debug statement to check if switch sprite was working
        key = pygame.key.get_pressed()
        if key[pygame.K_k]:
            self.animationsystem.playanimation("Number", 0.02, True)
        if key[pygame.K_l]:
            self.animationsystem.stopanimation()
        

# todo make all the components into a big list we can loop over in player.update(), also try to be able to dynamicly add and remove components on runtime