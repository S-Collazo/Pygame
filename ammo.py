import pygame
from constants import *
from bullet import Bullet

class Ammo:
    """Generador y controlador de la balas activas en el juego."""
    
    def __init__(self,asset:dict,lista_balas:list,x:int,y:int,frame_rate_ms:int,move_rate_ms:int,direction:int,p_scale:int=1) -> None:
        """
        Crea una bala nueva en base a los parámetros pasados y la genera en el nivel.
        
        No retorna nada.
        
        ----------
        asset : dict
            diccionario con toda la información del personaje que dispara la bala (contiene también la información de la bala)
        lista_balas : list
            lista de las balas activas en el nivel
        x : int
            coordenada X del personaje que dispara la bala
        y : int
            coordenada y del personaje que dispara la bala
        frame_rate_ms : int
            velocidad de las animaciones     
        move_rate_ms : int
            velocidad de desplazamiento
        direction : int
            dirección en la que se dispara la bala
        p_scale : int
            escala del sprite. Por defecto, 1
        """
        
        self.lista_balas = lista_balas
        self.p_scale = p_scale * GLOBAL_SCALE
        
        if(direction == DIRECTION_R):
            self.pos_x = x + (100 * GLOBAL_SCALE)
        else:
            self.pos_x = x - (100 * GLOBAL_SCALE)
        self.pos_y = y + (50 * GLOBAL_SCALE)
        self.direction = direction
        
        self.lista_balas.append(Bullet(asset=asset,x=self.pos_x,y=self.pos_y,frame_rate_ms=frame_rate_ms,move_rate_ms=move_rate_ms,move=50,direction_inicial=self.direction,p_scale=self.p_scale,interval_bullet=FPS*2,distance=ANCHO_VENTANA))
        
    def is_shooting(lista_balas:list,asset) -> bool:
        """
        Comprueba si la bala indicada se encuentra activa.
        
        Si es el caso, retorna True.
        
        Si no es el caso, retorna False.
        
        ----------
        lista_balas : list
            lista de las balas activas en el nivel
        asset : dict
            diccionario con toda la información del personaje que dispara la bala (contiene también la información de la bala)
        """
        
        retorno = False
        for bala in lista_balas:
            if(bala.is_shoot and bala.bullet_asset_name == asset["bullet"]["name"]):
                retorno = True
                break   
        return retorno
