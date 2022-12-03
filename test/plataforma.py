import pygame
from constants import *
from auxiliar import Auxiliar

class Platform:
    def __init__ (self,x,y,w,h,type=0,p_scale=1,collition_enabled=True):
        
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\tileset\\creepy_forest\\Tiles\\Tile ({0}).png",16,flip=False,scale=p_scale,w=w,h=h)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.collition_enabled = collition_enabled

        if(self.collition_enabled):
            self.rect_collition = pygame.Rect(self.rect)
            self.rect_ground_collition = pygame.Rect(self.rect)
            self.rect_ground_collition.height = GROUND_COLLIDE_H
    
    def draw (self,screen):        
        if(DEBUG):
            if(self.collition_enabled):
                pygame.draw.rect(screen,RED,self.rect_collition)
                pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
            
        screen.blit(self.image,self.rect)