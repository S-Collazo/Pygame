import pygame
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_button import Button
from ui_textbox import TextBox
from database import Database

class HighscoreTable(Form):
    """Formulario de la tabla de puntuaciones."""
    
    def __init__(self,name:str,master_surface,x:int,y:int,w:int,h:int,background_color:tuple,border_color:tuple,active:bool) -> None:
        """
        Crea el formulario en base a los parámetros recibidos.
        
        Extrae información de un objeto Base de datos para obtener las puntuaciones 
        y nombres de jugadores registrados.
        
        También crea dos botones (uno para registrar una puntuación nueva y 
        otro para regresar al menú principal), un cuadro de texto principal con
        el título del formulario y cinco pares de cuadros de texto con los nombres 
        y puntuaciones obtenidas.
        
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
        self.menu_x = self.w / 4

        self.score = 0
        
        self.highscore_list = Database.display_all_highscore()
                        
        self.button_register_score = Button(master_surface=self,x=self.menu_x + 50,y=600,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_L_07.png",on_click=self.on_click_button_register_score,on_click_param="highscore_register",text="Registrar puntuación",font="Verdana",font_size=15,font_color=WHITE)
        self.button_exit = Button(master_surface=self,x=self.menu_x + 50,y=660,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_L_06.png",on_click=self.on_click_button_exit,on_click_param=None,text="Menu Principal",font="Verdana",font_size=20,font_color=WHITE)
              
        self.txt1 = TextBox(master_surface=self,x=self.menu_x + 100,y=50,w=300,h=150,background_color=None,border_color=None,background_image=None,text="TABLA DE PUNTUACIONES",font="Verdana",font_size=20,font_color=BLACK)
        
        self.highscore_name_1 = TextBox(master_surface=self,x=self.menu_x,y=210,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=self.highscore_list[0][1],font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_score_1 = TextBox(master_surface=self,x=self.menu_x + 200,y=210,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=str(self.highscore_list[0][2]),font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_name_2 = TextBox(master_surface=self,x=self.menu_x,y=260,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=self.highscore_list[1][1],font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_score_2 = TextBox(master_surface=self,x=self.menu_x + 200,y=260,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=str(self.highscore_list[1][2]),font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_name_3 = TextBox(master_surface=self,x=self.menu_x,y=310,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=self.highscore_list[2][1],font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_score_3 = TextBox(master_surface=self,x=self.menu_x + 200,y=310,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=str(self.highscore_list[2][2]),font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_name_4 = TextBox(master_surface=self,x=self.menu_x,y=360,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=self.highscore_list[3][1],font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_score_4 = TextBox(master_surface=self,x=self.menu_x + 200,y=360,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=str(self.highscore_list[3][2]),font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_name_5 = TextBox(master_surface=self,x=self.menu_x,y=410,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=self.highscore_list[4][1],font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_score_5 = TextBox(master_surface=self,x=self.menu_x + 200,y=410,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=str(self.highscore_list[4][2]),font="Verdana",font_size=15,font_color=WHITE)
        
        self.lista_widget = [self.button_register_score,self.button_exit,self.txt1,self.highscore_name_1,self.highscore_score_1,self.highscore_name_2,self.highscore_score_2,self.highscore_name_3,self.highscore_score_3,self.highscore_name_4,self.highscore_score_4,self.highscore_name_5,self.highscore_score_5]
        
        self.game_state = GAME_END
        self.exit = False
    
    def on_click_button_register_score (self,parametro:str) -> None:
        """
        Desactiva el formulario de tabla de puntuaciones y 
        activa el formulario de registro de puntuación.
        
        No retorna nada.
        
        ----------
        parametro : str
            nombre del formulario a activar
        """
        
        self.set_active(parametro)
                
    def on_click_button_exit (self, parametro:str) -> None:
        """
        Desactiva el formulario de tabla de puntuaciones 
        y regresa el juego al menú principal.
        
        No retorna nada.
        
        ----------
        parametro : str
            indicador vacío
        """
        
        self.set_active(parametro)
        self.exit = True

    def update(self, lista_eventos:list) -> None:
        """
        Carga nuevamente los nombres y puntuaciones registrados en la base de datos (en 
        caso de que haya una nueva puntuación en una de las entradas, se actualiza).
        
        Actualiza los elementos del formulario.
        
        No retorna nada.
        
        ----------
        lista_eventos : list
            lista de distintos tipos de eventos registrados por Pygame
        """
        
        self.highscore_list = Database.display_all_highscore()
        self.highscore_name_1._text = self.highscore_list[0][1]
        self.highscore_score_1._text = str(self.highscore_list[0][2])
        self.highscore_name_2._text = self.highscore_list[1][1]
        self.highscore_score_2._text = str(self.highscore_list[1][2])
        self.highscore_name_3._text = self.highscore_list[2][1]
        self.highscore_score_3._text = str(self.highscore_list[2][2])
        self.highscore_name_4._text = self.highscore_list[3][1]
        self.highscore_score_4._text = str(self.highscore_list[3][2])
        self.highscore_name_5._text = self.highscore_list[4][1]
        self.highscore_score_5._text = str(self.highscore_list[4][2])
        
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
