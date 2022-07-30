import pygame

class healthsystem():
    # initializes the component
    def __init__(self, parent, starthealth, minhealth = 1, maxhealth = 999999):
        # gets the component user
        self.parent = parent
        # gets the starting healt
        self.currenthealth = starthealth
        # gets the minimum health
        self.minhealth = minhealth
        # gets the minimum health
        self.maxhealth = maxhealth
    # update function specific to the component
    def update(self):
        # this mess of a statement retrieves the screen class from the gameinfo class, it does so via a sort of pointer towards the gameinfo class present on the parent class
        if self.parent.hidden is False:
            healthtext = self.parent.gameinfo.font.render(str(self.currenthealth), True, (255, 255, 255))
            self.parent.gameinfo.screen.blit(healthtext, [self.parent.x, self.parent.y - (self.parent.height / 1.5)])
    
    # decreases the currenthealth variable of the current instance of the component
    def decreasehealth(self, howmuch):
        if self.currenthealth - howmuch > self.minhealth:
            self.currenthealth -= howmuch
        else:
            self.parent.kill()
    
    # increases the currenthealth variable of the current instance of the component
    def increasehealth(self, howmuch):
        if self.currenthealth + howmuch < self.maxhealth:
            self.currenthealth += howmuch

class renderingsystem():
    
    def __init__(self, parent, sprite, color = None,):
        self.parent = parent
        self.sprite = sprite
        # gets the sprite type to determine how to draw the given sprite
        self.spritetype = type(self.sprite)
        self.color = color
        
    def render(self):

        # draws the given sprite to the current screen at the location of the parent object
        if self.parent.hidden is False:
            if self.spritetype == pygame.Surface:
                # draws the surface to the screen
                self.parent.gameinfo.screen.blit(self.sprite, [self.parent.x, self.parent.y])

            elif self.spritetype == pygame.Rect:
                # updates the rect to be drawn
                self.sprite = pygame.Rect(((self.parent.x, self.parent.y), (self.parent.width, self.parent.height)) )
                # draws the rect to the screen
                if self.color is not None:
                    
                    pygame.draw.rect(self.parent.gameinfo.screen, self.color, self.sprite)
                
                else:
                    raise Exception("No color value given")
                
            else: 
                raise Exception("Current variable type not supported by the render engine")
    
    # changes the sprite and spritetype        
    def changesprite(self, towhat):
        self.sprite = towhat
        self.spritetype = type(towhat)        
                




# simple movment handler
class movementsystem():
    def __init__(self, parent, movementspeed):
        self.parent = parent
        self.movementspeed = movementspeed

    def handlemovement(self):

        key = pygame.key.get_pressed()

        # movement script
        if key[pygame.K_LEFT]:
            self.parent.x -= self.movementspeed * self.parent.gameinfo.deltatime

        elif key[pygame.K_RIGHT]:
            self.parent.x += self.movementspeed * self.parent.gameinfo.deltatime

        elif key[pygame.K_UP]:
            self.parent.y -= self.movementspeed * self.parent.gameinfo.deltatime

        elif key[pygame.K_DOWN]:
            self.parent.y += self.movementspeed * self.parent.gameinfo.deltatime

        