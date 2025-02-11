from Entity import *

class Character(Entity):
    
    def __init__(self,image):
        Entity.__init__(self, image)
        self.speed=[0.1,0.5]
        self.direction=-1
        self.on_ground=False
        self.time_passed=0
        self.v=70                            #Velocidad del cambio de sprite                                                      
        
    def CollisionBox(self):
        rect=Entity.get_coor(self)
        col=(rect[0]+15,rect[1]+26,5,3)        
        return col
    
    def Gravity(self,time):
        rect=Entity.get_coor(self)
        rect.centery+=time*self.speed[1]
        
    def Collision(self,obj_col):
        char_col=self.CollisionBox()        
        
        if obj_col[0]<char_col[0]<obj_col[0]+obj_col[2] or obj_col[0]<char_col[0]+char_col[2]<obj_col[0]+obj_col[2]:            #Deteccion de plataformas en X
            if char_col[1]+char_col[3]>=obj_col[1] and char_col[1]-obj_col[1]<10:                                               #Deteccion de plataformas en Y                
                return True               
        return False
    
    def move(self,time,moves):
        rect=Entity.get_coor(self)        
        image=Entity.get_image(self)
        
        self.time_passed+=time
        
        if self.time_passed>=0 and self.time_passed<self.v*2:
            image=moves[0] 
        if self.time_passed>=self.v*2 and self.time_passed <self.v*3:
            image=moves[1]
        if self.time_passed>=self.v*3 and self.time_passed <self.v*4:
            image=moves[2]    
        if self.time_passed>=self.v*4 and self.time_passed <self.v*6:
            image=moves[3]
        if self.time_passed>=self.v*6:                 
            self.time_passed=0     
                
            
        if self.direction==0 or self.direction==1:
            rect.centerx+=time*self.speed[0]+1
        if self.direction==2 or self.direction==3:
            rect.centerx+=time*(-self.speed[0])
            image=pygame.transform.flip(image,1,0)
            
        return image
        
    def spawn(self,spawn_point):
        if spawn_point==0:
            self.set_pos(-28,122)
            self.direction=0
        elif spawn_point==1:
            self.set_pos(-28, 372)
            self.direction=1
        elif spawn_point==2:
            self.set_pos(795, 122)
            self.direction=2
        elif spawn_point==3:
            self.set_pos(795, 372)
            self.direction=3  