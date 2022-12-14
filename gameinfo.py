import pygame

class GameInfo():
    # there should only be 1 instance of this class since there is only 1 game
    def __init__(self, screen):
        # general game variables that otherwise need to be passed along in different functions which i hate
        self.font = pygame.font.SysFont("Vera", 40)
        self.frameselapsed = 0
        self.screen = screen
        # this gets updated a the beginning of every iteration of the main loop
        self.deltatime = None
        # for the physics system
        self.gravity = 9.8 # pixels per second
        self.friction = 10
        self.maxaccelaration = 100 # pixels per second 
        # entity shiz
        self.entitylist = []
        self.playerlist = []
        self.enemylist = []
        self.walllist = []
        
    def rendertext(self, text, color):
        renderedtext = self.font.render(text, True, color)
        return renderedtext        
    
    def update(self):
        # updates every entity in the list, duh
        for entity in self.entitylist:
            entity.update()