import pygame
from constants import *
from sounds import Sounds
from auxiliar import Auxiliar

class Item:
    def __init__ (self,path,x,y,w,h,sounds,p_scale=1,type=0,used=False):
        self.p_scale = p_scale * GLOBAL_SCALE
        
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + path + "_{:03d}.png",1,step=0,flip=False,scale=self.p_scale,w=w,h=h)
        self.image = self.image_list[type]
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.rect_collition = pygame.Rect(self.rect)
        
        self.used = used
        
        self.sounds = sounds
                    
    def update (self,lista_personajes):
        pass
    
    def draw (self,screen):        
        if(DEBUG):
            pygame.draw.rect(screen,ORANGE,self.rect_collition)
            
        screen.blit(self.image,self.rect)
        
class Health_Potion (Item):
    def __init__ (self,asset,name,x,y,sounds,p_scale=1.5,used=False):
        self.asset = asset["Healing Item"][name]
        self.path= self.asset["asset_folder"]
        item_dimensions = Auxiliar.splitIntoInt(self.asset["asset_dimensions"],",")
        self.w = item_dimensions[0]
        self.h = item_dimensions[1]
        super().__init__ (path=self.path,x=x,y=y,w=self.w,h=self.h,sounds=sounds,p_scale=p_scale,used=used)
        self.healing_power = self.asset["healing_power"]
        self.healing_sound = self.asset["sound_effect"]
    
    def healing (self,lista_personajes):        
        for personaje in lista_personajes:
            if(self.rect_collition.colliderect(personaje.rect_collition)):
                        if ((personaje.hitpoints + self.healing_power) <= personaje.hitpoints_max):
                            personaje.hitpoints += self.healing_power
                        else:
                            personaje.hitpoints = personaje.hitpoints_max
                        self.sounds.sound_effect(self.healing_sound)
                        self.used = True
            break
      
    def update (self,lista_personajes):
        self.healing(lista_personajes)
    
    def draw (self,screen):
            super().draw(screen)
            
class Gem (Item):
    def __init__ (self,asset,name,x,y,sounds,p_scale=0.8,enemy_drop=False,used=False):
        self.asset = asset["Currency"][name]
        if (enemy_drop):
            self.path= self.asset["asset_folder"][0]
            self.currency_value = self.asset["currency_value"][0]
        else:
            self.path= self.asset["asset_folder"][1]
            self.currency_value = self.asset["currency_value"][1]
        item_dimensions = Auxiliar.splitIntoInt(self.asset["asset_dimensions"],",")
        self.w = item_dimensions[0]
        self.h = item_dimensions[1]
        super().__init__ (path=self.path,x=x,y=y,w=self.w,h=self.h,sounds=sounds,p_scale=p_scale,used=used)
        self.currency_sound = self.asset["sound_effect"]
    
    def earning (self,lista_personajes):        
        for personaje in lista_personajes:
            if(self.rect_collition.colliderect(personaje.rect_collition)):
                        personaje.currency += self.currency_value
                        self.sounds.sound_effect(self.currency_sound)
                        self.used = True
            break
      
    def update (self,lista_personajes):
        self.earning (lista_personajes)
    
    def draw (self,screen):
            super().draw(screen)