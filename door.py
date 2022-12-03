import pygame
from constants import *
from auxiliar import Auxiliar

class Door:
    def __init__ (self,asset,x,y,w,h,p_scale=1):
        self.asset = asset
        self.asset_path = asset["asset_folder"]
        
        self.p_scale = p_scale * GLOBAL_SCALE
                
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + self.asset_path + "_{:03d}.png",2,step=0,flip=False,scale=self.p_scale,w=w,h=h)
        self.door_closed = self.image_list[1]
        self.door_open = self.image_list[0]
        
        self.is_open = False
        
        self.image = self.door_closed           
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.rect_collition = pygame.Rect(self.rect)
                
    def next_level (self,lista_personajes):
        self.state = None
        for personaje in lista_personajes:
            if (personaje.rect.colliderect(self.rect_collition)):
                self.state = GAME_VICTORY
        return self.state
                
    def update (self,level_clear):
        self.is_open = level_clear
        if (self.is_open):
            self.image = self.door_open 
    
    def draw (self,screen):        
        if(DEBUG):
            pygame.draw.rect(screen,ORANGE,self.rect_collition)
            
        screen.blit(self.image,self.rect)