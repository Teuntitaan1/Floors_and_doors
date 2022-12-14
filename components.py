import pygame
from os import listdir

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
            healthtext = self.parent.gameinfo.rendertext(str(self.currenthealth), (255, 255, 255))
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

# simple rendering system
class renderingsystem():
    
    def __init__(self, parent, sprite, color = None,):
        self.parent = parent
        self.sprite = sprite
        # gets the sprite type to determine how to draw the given sprite
        self.spritetype = type(self.sprite)
        self.color = color
        # if it should even render
        self.hidden = False
        
    def update(self):

        # draws the given sprite to the current screen at the location of the parent object
        if self.hidden is False:
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
        self.jumpforce = 10
        self.canjump = True
    def update(self):

        key = pygame.key.get_pressed()

        # movement script
        if key[pygame.K_LEFT]:
            self.parent.x -= self.movementspeed * self.parent.gameinfo.deltatime

        elif key[pygame.K_RIGHT]:
            self.parent.x += self.movementspeed * self.parent.gameinfo.deltatime

        if key[pygame.K_UP] and self.canjump:
            self.parent.getcomponent("physicssystem").acceleration -= self.jumpforce
            self.canjump = False


# modular animation handler
class animationsystem():
    
    def __init__(self, parent, animationsources):
        
        self.parent = parent
        # empty dict that going to be containing every animation
        self.animations = {}
        self.isanimating = False
        
        # loops through every file in the animationsources directory, parses it to an image and adds it to a list corresponding to the animation name
        for frame in listdir(animationsources):
            try:
                print(frame)
                # appends the frame to the animationlist
                frameinimage = pygame.image.load(f"{animationsources}\\{frame}").convert()
                animationtype = frame.split("_")[0] # gets the animation name so it can class them tog
                self.animations[animationtype].append(frameinimage)
            
            except Exception as e:
                self.animations[animationtype] = []
        
        print(self.animations.keys())
        
        # updates on every animation change
        self.currentanimation = None
        self.currentanimationlength = None
        self.currentanimationframe = 0
        self.currentanimationspeed = None
        self.currentanimationislooping = False
    
    
    
    #still need to fix wierd bug causing the animation to always start on frame 2
    
    
    # preps an animation to be played   
    def playanimation(self, animationname, speed, looping = False):
        
        if animationname in self.animations.keys():
            # resets and switches the animation
            if not self.isanimating:
                self.isanimating = True
                self.currentanimation = animationname
                self.currentanimationlength = len(self.animations[animationname])
                
                self.currentanimationframe = 0
                # speed of the animation
                self.currentanimationspeed = speed
                # if the animation should loop indefinitly
                self.currentanimationislooping = looping
        else: 
            raise Exception("This is not a valid animation name")
    
    def stopanimation(self):
        self.isanimating = False
    
    # must be run on every frame for the animation to play    
    def update(self):
        if self.isanimating:
            
            # checks if the next frame is valid before rendering the actual frame, minus 1 because the root of currentanimationlength is a list which starts at index 0
            if self.currentanimationframe > self.currentanimationlength:
                if not self.currentanimationislooping:
                    self.isanimating = False
                else:
                    self.currentanimationframe = 0
            else:
                # a rendering system needs to be present on the parent entity, this function basically renders the current frame from the current animation
                self.parent.getcomponent("renderingsystem").changesprite(self.animations[self.currentanimation][int(self.currentanimationframe)])
                # increments to the next frame
                self.currentanimationframe += self.currentanimationspeed
        print(self.currentanimationframe)
        
        
class physicssystem():
    
    def __init__(self, parent, mass):
        self.parent = parent
        self.objectmass = mass
        self.acceleration = 0
        
    def update(self):
        
        self.acceleration += self.objectmass * self.parent.gameinfo.gravity * self.parent.gameinfo.deltatime # a=m*f or a=f*m and * deltatime to make it per second not per frame
        if self.acceleration > self.parent.gameinfo.maxaccelaration:
            self.acceleration = self.parent.gameinfo.maxaccelaration
        self.parent.y += self.acceleration
        
    def setacceleration(self, towhat):
        self.acceleration = towhat
        
class newphysicssystem():
    
    def __init__(self, parent, mass):
        self.parent = parent
        self.objectmass = mass
        self.friction = self.parent.gameinfo.friction
        self.xacceleration = 0
        self.yacceleration = 0
        
    def update(self):
        
        self.yacceleration += self.objectmass * self.parent.gameinfo.gravity * self.parent.gameinfo.deltatime # a=m*f or a=f*m and * deltatime to make it per second not per frame
        if self.acceleration > self.parent.gameinfo.maxaccelaration:
            self.acceleration = self.parent.gameinfo.maxaccelaration
        self.parent.y += self.acceleration
        
    def setacceleration(self, towhat):
        self.acceleration = towhat
  
# base collider class that holds some properties for a collider box      
class collider():
    
    def __init__(self, parent):
        self.parent = parent
        self.rect = pygame.Rect((self.parent.x, self.parent.y), (self.parent.width, self.parent.height))
        self.solid = True
        
    def update(self):
        
        self.rect = pygame.Rect((self.parent.x, self.parent.y), (self.parent.width, self.parent.height))
        
# player collider logic class that handles wall and enemy collision, for this to work a collider class(see above) also needs to be present
class collidersystem():
    
    def __init__(self, parent):
        self.parent = parent
        self.collisiontolerance = 10
    
    def update(self):
        # gets the rect of its parent
        parentrect = self.parent.getcomponent("collider").rect
        # gets the wall list out of gameinfo
        walllist = self.parent.gameinfo.walllist
        
        for wall in walllist:
            # gets the rect of the wall
            wallrect = wall.getcomponent("collider").rect
            
            if parentrect.colliderect(wallrect):
                
                # collision from the top
                if abs(parentrect.bottom - wallrect.top) < self.collisiontolerance:
                    
                    self.parent.getcomponent("physicssystem").acceleration = 0
                    self.parent.y = wallrect.top - self.parent.height
                    self.parent.getcomponent("movementsystem").canjump = True 
                    
                # collision from the bottom
                if abs(parentrect.top - wallrect.bottom) < self.collisiontolerance:
                    
                    self.parent.getcomponent("physicssystem").acceleration = 0
                    self.parent.y = wallrect.bottom + self.parent.height 
                    
                # collision from the left
                if abs(parentrect.right - wallrect.left) < self.collisiontolerance:
                    
                    # self.parent.getcomponent("physicssystem").acceleration = 0
                    self.parent.x = wallrect.left - self.parent.width
                  
                # WHAT THE HELL IS HAPPENING HERE?  
                # collision from the right
                if abs(parentrect.left - wallrect.right) < self.collisiontolerance:
                    
                    # self.parent.getcomponent("physicssystem").acceleration = 0
                    self.parent.x = wallrect.right + self.parent.width
