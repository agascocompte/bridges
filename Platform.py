from Entity import *

class Platform(Entity):    
            
    def __init__(self,image):
        Entity.__init__(self,image)
        
    def CollisionBox(self):
        rect=Entity.get_coor(self)
        col=(rect[0],rect[1],rect[2],10)     
        return col            