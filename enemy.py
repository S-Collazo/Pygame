import pygame
import random
from constants import *
from entity import Entity
from item import *

class Enemy(Entity):
    def __init__ (self,asset,group,name,x,y,gravity,frame_rate_ms,move_rate_ms,sounds,p_scale=0.1) -> None:
        self.asset_type = asset[group][name]
        
        self.direction_value = random.random()
        if (self.direction_value == 0):
            self.direction = DIRECTION_L
        else:
            self.direction = DIRECTION_R
        
        self.sounds = sounds
        
        super().__init__(self.asset_type,x,y,gravity,frame_rate_ms,move_rate_ms,self.sounds,self.direction,p_scale)             
        self.x = x
        
        self.can_block = False
        self.can_throw = False
                       
    def drop_loot (self,lista_items,item_asset,currency_multiplier=1):
        gem_reward = Gem(asset=item_asset,name="Basic Gem",x=self.rect.x + (self.rect.w / 2),y=self.rect.y + (self.rect.h / 2),sounds=self.sounds,p_scale=1,enemy_drop=True)
        gem_reward.currency_value = gem_reward.currency_value * currency_multiplier
        lista_items.append(gem_reward)
                     
    def update (self,delta_ms,lista_plataformas,lista_items,item_asset):          
        super().update(delta_ms,lista_plataformas)
        
    def draw (self,screen):
        super().draw(screen)