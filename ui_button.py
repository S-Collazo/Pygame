import pygame
from pygame.locals import *
from constants import *
from auxiliar import Auxiliar
from ui_widget import Widget
    
class Button(Widget):
    """Widget clickeable."""
    
    def __init__ (self,master_surface,x:int=0,y:int=0,w:int=200,h:int=50,background_color:tuple=GREEN,border_color:tuple=RED,background_image:str=None,text:str="Button",font:str="Arial",font_size:int=14,font_color:tuple=BLUE,on_click=None,on_click_param:str=None) -> None:
        """
        Establece las características del botón (base en clase Widget).
        
        Ejecuta el método render para crear el botón en base a las características establecidas.
        
        No retorna nada.
              
        ----------
        master_surface
            superficie en la que se renderiza el widget
        x : int
            coordenada X en la que se genera el boton. Por defecto, 0
        y : int
            coordenada Y en la que se genera el boton. Por defecto, 0
        w : int
            ancho del boton. Por defecto, 200
        h : int
            alto del boton. Por defecto, 50
        background_color : tuple
            color de fondo del boton. Por defecto, verde
        border_color : tuple
            color de borde del boton. Por defecto, rojo
        background_image : str
            imagen de fondo del widget (opcional)
        text : str
            texto a renderizar en el widget (opcional). Por defecto, "Button"
        font : str
            tipo de fuente del texto. Por defecto, Arial
        font_size : int
            tamaño de fuente del texto. Por defecto, 14
        font_color : tuple
            color de fuente del texto. Por defecto, azul
        on_click
            método a ejecutar al clickear el boton
        on_click_param : str
            parámetro a pasar a la función indicada en "on_click"
        """
        
        super().__init__(master_surface,x,y,w,h,background_color,border_color,background_image,text,font,font_size,font_color)
        
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
                
        self.render()
            
    def render (self) -> None:
        """
        Ejecuta el método heredado de renderización de widget.
        
        Establece los cambios visuales en el botón en caso de ser clickeado.
        
        No retorna nada.
        """
        
        super().render()
        
        if self.state == M_STATE_HOVER:
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.state == M_STATE_CLICK:
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 
                         
    def update (self,lista_eventos:list) -> None:
        """
        Comprueba si se clickeó el botón.
        
        De ser el caso, cambia el estado del mismo, ejecuta la función pasada y 
        actualiza su apariencia.
        
        No retorna nada.

        ----------
        lista_eventos : list
            lista de distintos tipos de eventos registrados por Pygame
        """
        
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if(pygame.mouse.get_pressed()[0]):
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER
              
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if(self.slave_rect_collide.collidepoint(evento.pos)):
                    self.on_click(self.on_click_param)

        self.render()