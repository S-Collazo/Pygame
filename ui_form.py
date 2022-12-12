import pygame
from pygame.locals import *
from constants import *
from auxiliar import Auxiliar
from ui_widget import Widget
from ui_button import Button

class Form ():
    """Formulario base de todos los menues del juego."""
    
    forms_dict = {}
    def __init__ (self,name:str,master_surface,x:int,y:int,w:int,h:int,background_color:tuple,border_color:tuple,active:bool) -> None:
        """
        Crea el formulario en base a los parámetros recibidos.
        
        También crea un rectángulo de superficie del mismo tamaño que el formulario.
        
        No retorna nada.
        
        ----------
        name : str
            nombre identificador del formulario
        master_surface
            superficie en la que se renderiza el formulario
        x : int
            coordenada X en la que se genera el formulario
        y : int
            coordenada Y en la que se genera el formulario
        w : int
            ancho del formulario
        h : int
            alto del formulario
        background_color : tuple
            color de fondo del formulario
        border_color : tuple
            color de borde del formulario
        active : bool
            indica si el formulario se encuentra activo o no
        """
        
        self.forms_dict[name] = self
        self.master_form = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.background_color = background_color
        self.border_color = border_color
        
        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        
        self.active = active
             
        if(self.background_color != None):
            self.surface.fill(self.background_color)
        else:
            self.surface = pygame.Surface((w,h))
            self.surface = self.surface.convert_alpha()
            self.surface.fill((0, 0, 0, 0))
            
    def set_active(self,name:str) -> None:
        """
        Desactiva el formulario que ejecuta el método y activa 
        el formulario indicado en el parámetro (si se recibió uno).
        
        No retorna nada.

        ----------
        name : str
            nombre del formulario a activar (opcional)
        """
        
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        if (name != None):
            self.forms_dict[name].active = True

    def render(self) -> None:
        """
        Pasa el método render del formulario creado en base a esta clase.
        
        No retorna nada.
        """
        
        pass

    def update(self,lista_eventos:list) -> None:
        """
        Pasa el método update del formulario creado en base a esta clase.
        
        No retorna nada.
        
        ----------
        lista_eventos : list
            lista de distintos tipos de eventos registrados por Pygame
        """
        
        pass

    def draw(self) -> None:
        """
        Renderiza el formulario y su rectángulo de superficie.
        
        No retorna nada.
        """
        
        self.master_form.blit(self.surface,self.slave_rect)