import pygame
class GameInfo():
    # there should only be 1 instance of this class since there is only 1
    def __init__(self, screen):
        # general game variables that otherwise need to be passed along in different functions which i
        self.font = pygame.font.SysFont("Vera", 40)
        self.frameselapsed = 0
        self.screen = screen
        # this gets updated a the beginning of every iteration of the main loop
        self.deltatime = None