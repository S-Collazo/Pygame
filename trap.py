import pygame
from constants import *
from auxiliar import Auxiliar

class Trap:
    def __init__ (self,x,y,w,h,type=0,p_scale=1):
        self.asset_name = "Trap"
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\traps\\creepy_forest\\spikes_{:02d}.png",1,step=0,flip=False,scale=p_scale,w=w,h=h)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.is_attack = True
        self.attack_power = 100
        self.attack_sound = "\\sounds\\effects\\trap.wav"
        
        self.rect_body_collition = pygame.Rect(self.rect)
    
    def draw (self,screen):        
        if(DEBUG):
            pygame.draw.rect(screen,ORANGE,self.rect_body_collition)
            
        screen.blit(self.image,self.rect)
        
