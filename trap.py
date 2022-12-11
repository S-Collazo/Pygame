import pygame
from constants import *
from auxiliar import Auxiliar

class Trap:
    """Elemento especial que causa daño a cualquier personaje que colisiona con él."""
    
    def __init__ (self,x:int,y:int,w:int,h:int,p_scale:float=1) -> None:
        """
        Crea la trampa en base a la carpeta de imagenes indicada y le asigna un 
        valor de daño (hardcodeado para ser igual a la vida máxima del jugador) y 
        un efecto de sonido.
        
        También genera un rectángulo con las mismas dimensiones que el sprite.
        
        No retorna nada.
              
        ----------
        x : int
            coordenada X en la que se genera la trampa en el nivel
        y : int
            coordenada Y en la que se genera la trampa en el nivel
        w : int
            ancho del sprite
        h : int
            alto del sprite
        p_scale : float
            escala del sprite. Por defecto, 1
        """
        
        self.asset_name = "Trap"
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\traps\\creepy_forest\\spikes_{:02d}.png",1,step=0,flip=False,scale=p_scale,w=w,h=h)
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.is_attack = True
        self.attack_power = 100
        self.attack_sound = "\\sounds\\effects\\trap.wav"
        
        self.rect_body_collition = pygame.Rect(self.rect)
    
    def draw (self,screen):       
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
            pygame.draw.rect(screen,ORANGE,self.rect_body_collition)
            
        screen.blit(self.image,self.rect)
        
