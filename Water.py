from Entity import *
from random import randint

class Water(Entity):    
            
    def __init__(self,image):
        Entity.__init__(self,image)
        
    def move(self,a):      
        if a==0:
            self.rect.centerx+=1
        if a==5:
            self.rect.centerx-=1        