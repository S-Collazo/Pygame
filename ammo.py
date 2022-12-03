import pygame
from constants import *
from bullet import Bullet

class Ammo:
    def __init__(self,asset,lista_balas,x,y,frame_rate_ms,move_rate_ms,direction,p_scale=1):
        self.lista_balas = lista_balas
        self.p_scale = p_scale * GLOBAL_SCALE
        
        if(direction == DIRECTION_R):
            self.pos_x = x + (100 * GLOBAL_SCALE)
        else:
            self.pos_x = x - (100 * GLOBAL_SCALE)
        self.pos_y = y + (50 * GLOBAL_SCALE)
        self.direction = direction
        
        self.lista_balas.append(Bullet(asset=asset,x=self.pos_x,y=self.pos_y,frame_rate_ms=frame_rate_ms,move_rate_ms=move_rate_ms,move=50,direction_inicial=self.direction,p_scale=self.p_scale,interval_bullet=FPS*2,distance=ANCHO_VENTANA))
        
    def is_shooting(lista_balas,asset):
        retorno = False
        for bala in lista_balas:
            if(bala.is_shoot and bala.bullet_asset_name == asset["bullet"]["name"]):
                retorno = True
                break   
        return retorno