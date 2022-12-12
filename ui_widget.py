import pygame
from pygame.locals import *
from constants import *

class Widget:
    """Elemento base de la IU."""
    
    def __init__ (self,master_surface,x:int,y:int,w:int,h:int,background_color:tuple,border_color:tuple,background_image:str,text:str,font:str,font_size:int,font_color:tuple,bold:bool=False) -> None:
        """
        Establece las características del widget en base a los parámetros recibidos.
        
        No retorna nada.
              
        ----------
        master_surface
            superficie en la que se renderizan el widget
        x : int
            coordenada X en la que se genera el widget en la superficie
        y : int
            coordenada Y en la que se genera el widget en la superficie
        w : int
            ancho del widget
        h : int
            alto del widget
        background_color : tuple
            color de fondo del widget
        border_color : tuple
            color de borde del widget
        background_image : str
            imagen de fondo del widget (opcional)
        text : str
            texto a renderizar en el widget (opcional)
        font : str
            tipo de fuente del texto
        font_size : int
            tamaño de fuente del texto
        font_color : tuple
            color de fuente del texto
        bold : bool
            indica si el texto es en negrita. Por defecto, False
        """
        
        self.master_form = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.background_color = background_color
        self.border_color = border_color
        
        if background_image != None:
            self.background_image = pygame.image.load(background_image)
            self.background_image = pygame.transform.scale(self.background_image,(w, h)).convert_alpha()
        else:
            self.background_image = pygame.Surface((w, h))
            self.background_image = self.background_image.convert_alpha()
            self.background_image.fill((0, 0, 0, 0))
            
        self._text = text
        if(self._text != None):
            pygame.font.init()
            self._font_sys = pygame.font.SysFont(font,font_size,bold)
            self._font_color = font_color
    
    def render (self) -> None:
        """
        Crea el widget. También crea un rectángulo de colisión del mismo tamaño.
        
        No retorna nada.
        """
        
        self.slave_surface = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y
        
        if self.background_color:
            self.slave_surface.fill(self.background_color)
        
        if self.background_image:
            self.slave_surface.blit(self.background_image,(0,0))
        
        if(self._text != None):
            image_text = self._font_sys.render(self._text,True,self._font_color,self.background_color)
            self.slave_surface.blit(image_text,[
                self.slave_rect.width/2 - image_text.get_rect().width/2,
                self.slave_rect.height/2 - image_text.get_rect().height/2
            ])
            
        if self.border_color:
            pygame.draw.rect(self.slave_surface, self.border_color, self.slave_surface.get_rect(), 2)
            
    def update (self) -> None:
        """
        Pasa el método update del elemento creado en base a esta clase.
        
        No retorna nada.
        """
        pass
    
    def draw (self) -> None:
        """
        Renderiza el widget y su rectángulo de colisión.
        
        No retorna nada.
        """
        
        self.master_form.surface.blit(self.slave_surface,self.slave_rect)