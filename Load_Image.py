import pygame
from pygame.locals import *

def load_image(filename, transparent=False):  #Funcion de cargar imagenes
        image = pygame.image.load(filename)        
        image = image.convert()
        if transparent:
                color = image.get_at((869,166))
                image.set_colorkey(color, RLEACCEL)
        return image