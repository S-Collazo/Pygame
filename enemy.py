import pygame
import random
from constants import *
from entity import Entity
from item import *

class Enemy(Entity):
    """Base de los personajes que se enfrentan al jugador."""
    
    def __init__ (self,asset:dict,group:str,name:str,x:int,y:int,gravity:int,frame_rate_ms:int,move_rate_ms:int,sounds,p_scale:float=0.1) -> None:
        """
        Extrae información del diccionario para generar un personaje (base en clase Entity).
        
        También elige de forma aleatoria la dirección inicial del personaje.
        
        No retorna nada.
        
        ----------
        asset : dict
            diccionario con toda la información del personaje
        group : str
            grupo de enemigos al que pertenece el personaje
        name : str
            tipo de enemigo del personaje
        x : int
            coordenada X en la que aparece el personaje al inicio del nivel
        y : int
            coordenada Y en la que aparece el personaje al inicio del nivel
        gravity : int
            velocidad de caída
        frame_rate_ms : int
            velocidad de las animaciones     
        move_rate_ms : int
            velocidad de desplazamiento
        sounds
            objeto controlador de sonidos
        direction_inicial : int
            dirección del personaje al inicio del nivel. Por defecto, derecha
        p_scale : float
            escala del sprite. Por defecto, 0.1
        """
        
        self.asset_type = asset[group][name]
        
        self.direction_value = random.randrange(2)
        if (self.direction_value == 0):
            self.direction = DIRECTION_L
        else:
            self.direction = DIRECTION_R
        
        self.sounds = sounds
        
        super().__init__(self.asset_type,x,y,gravity,frame_rate_ms,move_rate_ms,self.sounds,self.direction,p_scale)             
        self.x = x
        
        self.can_block = False
        self.can_throw = False
                       
    def drop_loot (self,lista_items:list,item_asset:dict,boss_drop:bool=False) -> None:
        """
        Genera una objeto en el nivel con la posición del enemigo.
        
        No retorna nada.
        
        ----------
        lista_items : list
            lista de los objetos activos en el nivel
        item_asset : dict
            diccionario que contiene la información del objeto
        boss_drop : bool
            modificador del objeto exclusivo de enemigos tipo jefe
        """
        
        gem_reward = Gem(asset=item_asset,name="Basic Gem",x=self.rect.x + (self.rect.w / 2),y=self.rect.y + (self.rect.h / 2),sounds=self.sounds,p_scale=1,enemy_drop=True,boss_drop=boss_drop)
        gem_reward.currency_value = gem_reward.currency_value
        lista_items.append(gem_reward)
                     
    def update (self,delta_ms:int,lista_plataformas:list,lista_items:list,item_asset:dict) -> None:
        """
        Ejecuta el método update heredado, actualizando los atributos de tiempo pasado, plataformas e items activos 
        y objeto a generar cuando muera el personaje.
        
        No retorna nada.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_plataformas : list
            lista de las plataformas activas en el nivel
        lista_items : list
            lista de los objetos activos en el nivel
        item_asset : dict
            diccionario que contiene la información del objeto a generar en caso de muerte
        """
                  
        super().update(delta_ms,lista_plataformas)
        
    def draw (self,screen):
        """
        Ejecuta el método draw heredado.
        
        No retorna nada.
        
        ----------
        screen
            superficie en la que se renderizan los sprites       
        """
        
        super().draw(screen)