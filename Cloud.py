from Entity import *

class Cloud(Entity):    
            
    def __init__(self,image):
        Entity.__init__(self,image)
        self.speed=0.1
        self.time_passed1=0
        self.time_passed2=0
        
    def move(self,time,WEIDGH,val=0):
        if val==0:
            self.time_passed1+=time
            
            if self.time_passed1>200:
                self.rect.centerx+=time*self.speed
                self.time_passed1=0
        else:
            self.time_passed2+=time
            
            if self.time_passed2>100:
                self.rect.centerx+=time*self.speed
                self.time_passed2=0
                
        if self.rect.centerx>=WEIDGH+100:
            self.rect.centerx=-100                   