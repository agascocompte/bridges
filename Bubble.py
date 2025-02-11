from Entity import *
from random import randint

class Bubble(Entity):    
            
    def __init__(self,image):
        Entity.__init__(self,image)
        self.speed=0.1
        self.time_passed=0
        
    def move(self,time,HEIGHT,WEIDGH):
        self.time_passed+=time
        if self.time_passed>=50:        
            self.rect.centery-=self.speed*time
            self.time_passed=0
        
        if self.rect.centery<=HEIGHT-46:
            self.set_pos(randint(0,WEIDGH),randint(HEIGHT,HEIGHT+100))