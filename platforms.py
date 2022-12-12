import pygame
from constants import *
from auxiliar import Auxiliar

class Platforms:
    """Superficies en las que se mueven los personajes del nivel."""
    
    def __init__ (self,path:str,x:int,y:int,w:int,h:int,type:int=0,p_scale:float=1,collition_enabled:bool=True):
        """
        Crea la plataforma en base a la carpeta de imagenes indicada.
        
        Si la variabla de colisiones es True, también genera un rectángulo con las mismas dimensiones que el sprite.
        
        No retorna nada.
              
        ----------
        path : str
            ubicación de la carpeta de imagenes de la plataforma
        x : int
            coordenada X en la que se genera la plataforma en el nivel
        y : int
            coordenada Y en la que se genera la plataforma en el nivel
        w : int
            ancho del sprite
        h : int
            alto del sprite
        type : int
            ubicación del sprite a usar en la carpeta de imagenes
        p_scale : float
            escala del sprite. Por defecto, 1
        colitions_enabled : bool
            indica si se deben comprobar las colisiones entre otros elementos y la plataforma
        """
        
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + path + "Tile ({0}).png",17,flip=False,scale=p_scale,w=w,h=h)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.collition_enabled = collition_enabled

        if(self.collition_enabled):
            self.rect_collition = pygame.Rect(self.rect)
            self.rect_ground_collition = pygame.Rect(self.rect)
            self.rect_ground_collition.height = GROUND_COLLIDE_H
    
    def draw (self,screen) -> None:
        """
        Renderiza el sprite de la plataforma.
        
        No retorna nada.
        
        ----------
        screen
            superficie en la que se renderizan los sprites
        
        ----------
        DEBUG: Renderiza el rectángulo de colisión.
        """
            
        if(DEBUG):
            if(self.collition_enabled):
                pygame.draw.rect(screen,ORANGE,self.rect_collition)
            
        screen.blit(self.image,self.rect)
        
    def create_plaforms(lista_plataformas:list,path:str,x:int,y:int,w:int,h:int,tile_total:int=2,p_scale:float=1,tile_type:int=0,collition_enabled:bool=True,add_bottom:bool=False) -> None:              
        """
        Crea una fila de plataformas con las características indicadas, iniciando en la posición indicada.
        
        No retorna nada.
        
        ----------
        lista_plataformas _ list
            lista de las plataformas activas en el nivel
        path : str
            ubicación de la carpeta de imagenes de las plataformas
        x : int
            coordenada X en la que se genera la fila de plataformas en el nivel
        y : int
            coordenada Y en la que se genera la fila de plataformas en el nivel
        w : int
            ancho de cada plataforma
        h : int
            alto de cada plataformas
        tile_total : int
            total de plataformas a crear. Por defecto, 2
        p_scale : float
            escala de los sprites. Por defecto, 1
        tile_type : int
            identificador de los sprites de plataforma a usar. Por defecto, 0
        colitions_enabled : bool
            indica si se deben comprobar las colisiones entre otros elementos y la plataforma
        add_botom : bool
            indica si se deben agregar plataformas carentes de colisiones desde la posición indicada 
            hasta el suelo del nivel.
        """
        
        scale = p_scale * GLOBAL_SCALE
        
        type_start = tile_type
        type_mid = type_start + 1
        type_end = type_mid + 1
        
        lista_plataformas.append(Platforms(path=path,x=x,y=y,w=w,h=h,type=type_start,p_scale=scale,collition_enabled=collition_enabled))
        for n in range(1,tile_total - 1):
            tile_separation = (w * scale) * n
            lista_plataformas.append(Platforms(path=path,x=x + tile_separation,y=y,w=w,h=h,type=type_mid,p_scale=scale,collition_enabled=collition_enabled))
        tile_separation = (w * scale) * (tile_total - 1)
        lista_plataformas.append(Platforms(path=path,x=x + tile_separation,y=y,w=w,h=h,type=type_end,p_scale=scale,collition_enabled=collition_enabled))

        if(add_bottom):
            tile_range = int((ALTO_VENTANA - y) / (h * p_scale))
            tile_bottom = type_end + 1

            for n in range(1,tile_range):
                y_position = y + ((h * n) * p_scale)
                Platforms.create_plaforms(lista_plataformas,path=path,x=x,y=y_position,w=w,h=h,tile_total=tile_total,p_scale=p_scale,tile_type=tile_bottom,collition_enabled=False)