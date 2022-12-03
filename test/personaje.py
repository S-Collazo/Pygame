import pygame
from constants import *
from auxiliar import Auxiliar
from entity import Entity

class Player(Entity):
    def __init__ (self,asset,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_R,p_scale=0.1) -> None:
        self.asset_folder = "\\players\\{0}".format(asset)
        
        super().__init__(self.asset_folder,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial,p_scale)
                
        self.lives = 5
        self.score = 0
        self.entity_type = PLAYER
                                                                             
    def update(self,delta_ms,lista_plataformas,lista_oponente):
        super().update(delta_ms,lista_plataformas,lista_oponente)
    
    def draw (self,screen):
        super().draw(screen)
                
    def events(self,delta_ms,keys):
        self.tiempo_transcurrido += delta_ms
        
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            super().walk(DIRECTION_L)
        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            super().walk(DIRECTION_R)
        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            super().stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            super().stay()   
        if(keys[pygame.K_SPACE] or keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > (self.interval_time_jump * FPS)):
                super().jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido
                   
        if(not keys[pygame.K_a]):
            self.shoot(False)  
        if(keys[pygame.K_s] and not keys[pygame.K_a]):
            self.shoot()
        if(not keys[pygame.K_a]):
            self.attack(False)
        if(keys[pygame.K_a] and not keys[pygame.K_s]):
            self.attack()  
