import pygame
import sys
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_button import Button
from ui_textbox import TextBox

class HighscoreMain(Form):
    """Formulario principal de la pantalla de puntuación."""
    
    def __init__(self,name:str,master_surface,x:int,y:int,w:int,h:int,background_color;tuple,border_color:tuple,active:bool) -> None:
        """
        Crea el formulario en base a los parámetros recibidos.
        
        También crea dos botones (uno para ir a la tabla de puntuaciones y 
        otro para regresar al menú principal) y cinco cuadros de texto (el título 
        del formulario, las puntuaciones de cada uno de los tres niveles y la 
        puntuación final).
        
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

        self.lvl1 = 0
        self.lvl2 = 0
        self.lvl3 = 0
        
        self.final = 0
        
        self.score_lvl1 = "Puntuación Nivel 1: {0}".format(self.lvl1)
        self.score_lvl2 = "Puntuación Nivel 2: {0}".format(self.lvl2)
        self.score_lvl3 = "Puntuación Nivel 3: {0}".format(self.lvl1)
        self.score_final = "Puntuación Final: {0}".format(self.final)
                
        self.button_table = Button(master_surface=self,x=self.menu_x + 50,y=600,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_L_07.png",on_click=self.on_click_button_table,on_click_param="highscore_table",text="Tabla",font="Verdana",font_size=20,font_color=WHITE)
        self.button_exit = Button(master_surface=self,x=self.menu_x + 50,y=660,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_L_06.png",on_click=self.on_click_button_exit,on_click_param=None,text="Menu Principal",font="Verdana",font_size=20,font_color=WHITE)
              
        self.txt1 = TextBox(master_surface=self,x=self.menu_x,y=100,w=400,h=150,background_color=None,border_color=None,background_image=None,text="FIN DEL JUEGO",font="Verdana",font_size=20,font_color=BLACK)
        self.txt2 = TextBox(master_surface=self,x=self.menu_x,y=300,w=200,h=50,background_color=None,border_color=None,background_image=None,text=self.score_lvl1,font="Verdana",font_size=15,font_color=BLACK)
        self.txt3 = TextBox(master_surface=self,x=self.menu_x,y=350,w=200,h=50,background_color=None,border_color=None,background_image=None,text=self.score_lvl2,font="Verdana",font_size=15,font_color=BLACK)
        self.txt4 = TextBox(master_surface=self,x=self.menu_x,y=400,w=200,h=50,background_color=None,border_color=None,background_image=None,text=self.score_lvl3,font="Verdana",font_size=15,font_color=BLACK)
        self.txt5 = TextBox(master_surface=self,x=self.menu_x + 25,y=450,w=200,h=50,background_color=None,border_color=None,background_image=None,text=self.score_final,font="Verdana",font_size=15,font_color=BLACK)
        
        self.lista_widget = [self.button_table,self.button_exit,self.txt1,self.txt2,self.txt3,self.txt4,self.txt5]
        
        self.game_state = GAME_END
        self.exit = False
    
    def on_click_button_table (self, parametro:str) -> None:
        """
        Desactiva el formulario principal y pasa al 
        formulario de la tabla de puntuaciones.
        
        No retorna nada.
        
        ----------
        parametro : str
            nombre del formulario a activar
        """
        
        self.set_active(parametro)
        
    def on_click_button_exit (self, parametro:str) -> None:
        """
        Desactiva el formulario de pantalla de puntuación 
        y regresa el juego al menú principal.
        
        No retorna nada.
        
        ----------
        parametro : str
            indicador vacío
        """
        
        self.set_active(parametro)
        self.exit = True

    def update(self, lista_eventos:list,score_list:list) -> None:
        """
        Carga las puntuaciones de cada nivel a las variables respondientes.
        
        Calcula la puntuación final en base a esos valores.
        
        Actualiza los elementos del formulario (incluyendo las puntuaciones obtenidas).
        
        No retorna nada.
        
        ----------
        lista_eventos : list
            lista de distintos tipos de eventos registrados por Pygame
        score_list : list
            puntuación del jugador en cada nivel
        """
        
        self.lvl1 = score_list[0]
        self.lvl2 = score_list[1]
        self.lvl3 = score_list[2]
        
        self.final = self.lvl1 + self.lvl2 + self.lvl3
          
        self.txt2._text = "Puntuación Nivel 1: {0}".format(self.lvl1)
        self.txt3._text = "Puntuación Nivel 2: {0}".format(self.lvl2)
        self.txt4._text = "Puntuación Nivel 3: {0}".format(self.lvl3)
        self.txt5._text = "Puntuación Final: {0}".format(self.final)
        
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
