import pygame
import random
from item import *
from constants import *
from auxiliar import Auxiliar

class Chest:
    def __init__ (self,item_asset,x,y,w,h,sounds,p_scale=1):
        self.item_asset = item_asset
        
        self.p_scale = p_scale * GLOBAL_SCALE
                
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\tileset\\creepy_forest\\Objects\\chest_{:03d}.png",2,step=0,flip=False,scale=self.p_scale,w=w,h=h)
        self.chest_closed = self.image_list[0]
        self.chest_open = self.image_list[1]
        
        self.is_open = False
        self.open_sound = "\\sounds\\effects\\chest.wav"
        
        self.image = self.chest_closed           
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.sounds = sounds
        
        self.rect_collition = pygame.Rect(self.rect)

    def get_loot (self,lista_items):
        if not (self.is_open):
            self.sounds.sound_effect(self.open_sound)
            
            loot_number = random.randrange(10)
            
            if (loot_number % 2):
                loot_reward = Gem(asset=self.item_asset,name="Basic Gem",x=self.rect.x + (self.rect.w / 3),y=self.rect.y - (self.rect.h / 2),sounds=self.sounds,p_scale=1,enemy_drop=True)
            else:
                loot_reward = Health_Potion(asset=self.item_asset,name="Basic Health Potion",x=self.rect.x + (self.rect.w / 3),y=self.rect.y - (self.rect.h / 2),sounds=self.sounds,p_scale=1.5)

            lista_items.append(loot_reward)
        
    def is_opened (self,lista_personajes,lista_items):
        for personaje in lista_personajes:
            if (personaje.rect_body_collition.colliderect(self.rect_collition)):
                self.get_loot(lista_items)
                self.image = self.chest_open
                self.is_open = True

    def update (self,lista_personajes,lista_items):
        self.is_opened(lista_personajes,lista_items)
    
    def draw (self,screen):        
        if(DEBUG):
            pygame.draw.rect(screen,ORANGE,self.rect_collition)
            
        screen.blit(self.image,self.rect)