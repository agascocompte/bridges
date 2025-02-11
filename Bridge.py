from Entity import *

class Bridge(Entity):    
            
    def __init__(self,image):
        Entity.__init__(self,image)
        
    def CollisionBox(self):
        rect=Entity.get_coor(self)
        col=(rect[0]+20,rect[1]+32,rect[2]-20,10)     
        return col     