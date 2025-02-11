import pygame

class Entity(pygame.sprite.Sprite):
    
    def __init__(self,image):
        
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        
    def set_pos(self,x,y):
        self.rect.left=x
        self.rect.top=y
     
    def get_coor(self):
        return self.rect
    
    def centery(self):
        return self.rect.centery
    
    def get_image(self):
        return self.image        