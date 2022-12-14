import pygame
import sys
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_button import Button
from ui_textbox import TextBox

class DeathMain(Form):
    """Formulario principal de la pantalla de muerte."""
    
    def __init__(self,name:str,master_surface,x:int,y:int,w:int,h:int,background_color:tuple,border_color:tuple,active:bool) -> None:
        """
        Crea el formulario en base a los parámetros recibidos.
        
        También crea dos botones (uno para reiniciar el nivel y otro para regresar 
        al menú principal) y un cuadro de texto con el título del formulario.
        
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
        
        super().__init__(name,master_surface,x,y,w,h,background_color,border_color,active)
        self.menu_x = self.w / 3
        
        self.button_restart = Button(master_surface=self,x=self.menu_x + 50,y=350,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_L_08.png",on_click=self.on_click_button_restart,on_click_param="ScreenInfo",text="Reiniciar Nivel",font="Verdana",font_size=20,font_color=WHITE)
        self.button_exit = Button(master_surface=self,x=self.menu_x + 50,y=450,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_L_06.png",on_click=self.on_click_button_exit,on_click_param=None,text="Menu Principal",font="Verdana",font_size=20,font_color=WHITE)
              
        self.txt1 = TextBox(master_surface=self,x=self.menu_x,y=200,w=300,h=150,background_color=None,border_color=None,background_image=None,text="MUERTO",font="Verdana",font_size=60,font_color=WHITE)
        
        self.lista_widget = [self.button_restart,self.button_exit,self.txt1]
        
        self.game_state = GAME_DEATH
        self.exit = False

    def on_click_button_restart(self,parametro:str) -> None:
        """
        Desactiva el formulario de pantalla de la muerte y 
        regresa el juego al nivel activo.
        
        No retorna nada.
        
        ----------
        parametro : str
            elementos de información de usuario del nivel a reactivar
        """
        
        self.set_active(parametro)
        self.exit = False
    
    def on_click_button_exit (self, parametro) -> None:
        """
        Desactiva el formulario de pantalla de la muerte y 
        regresa el juego al menú principal.
        
        No retorna nada.
        
        ----------
        parametro : str
            indicador vacío
        """
        
        self.set_active(parametro)
        self.exit = True

    def update(self, lista_eventos:list) -> None:
        """
        Actualiza los elementos del formulario.
        
        No retorna nada.
        
        ----------
        lista_eventos : list
            lista de distintos tipos de eventos registrados por Pygame
        """
        
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self) -> None: 
        """
        Ejecuta el método heredado de renderización y 
        hace lo mismo con los elementos del formulario.
        
        No retorna nada.
        """
        
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()
