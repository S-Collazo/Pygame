import pygame
from constants import *
from auxiliar import Auxiliar

class Door:
    """Transportador a la pantalla de victoria. Finaliza el nivel."""
    
    def __init__ (self,asset:dict,x:int,y:int,w:int,h:int,p_scale:float=1) -> None:
        """
        Extrae información del diccionario para determinar sprite de la puerta (dos versiones: abierta y cerrada).
        Inicializa la puerta cerrada.
        
        También genera un rectángulo de colisión con las mismas dimensiones que el sprite.
        
        No retorna nada.
        
        ----------
        asset : dict
            diccionario con la información de la puerta
        x : int
            coordenada X inicial de la bala
        y : int
            coordenada Y inicial de la bala   
        w : int
            ancho del sprite
        h : int
            alto del sprite
        p_scale : float
            escala del sprite. Por defecto, 1
        """
        
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
                
    def next_level (self,lista_personajes:list) -> int:
        """
        Comprueba si ocurrió una colisión entre la puerta y un jugador.
        
        Si es el caso, retorna el estado de juego "GAME_VICTORY"
        
        Si no es el caso, retorna none.
        
        ----------
        lista_personajes : list
            lista de los jugadores activos en el nivel
        """
        
        self.state = None
        for personaje in lista_personajes:
            if (personaje.rect.colliderect(self.rect_collition)):
                self.state = GAME_VICTORY
        return self.state
                
    def update (self,level_clear:bool):
        """
        Si la variable de nivel completo es True, cambia el sprite de la puerta a su versión abierta.
        
        No retorna nada.
        
        ----------
        level_clear : bool
            indica si el nivel se completó o no
        """
        
        self.is_open = level_clear
        if (self.is_open):
            self.image = self.door_open 
    
    def draw (self,screen) -> None:
        """
        Renderiza y actualiza el sprite de la puerta en base a su versión activa.
        
        No retorna nada.
        
        ----------
        screen
            superficie en la que se renderizan los sprites
        
        ----------
        DEBUG: Renderiza el rectángulo de colisiones.
        """
              
        if(DEBUG):
            pygame.draw.rect(screen,ORANGE,self.rect_collition)
            
        screen.blit(self.image,self.rect)