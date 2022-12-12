import pygame
import sys
import re
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_textbox import TextBox
from database import Database

class HighscoreRegister(Form):
    """Formulario de registro de puntuaciones."""
    
    def __init__(self,name:str,master_surface,x:int,y:int,w:int,h:int,background_color:tuple,border_color:tuple,active:bool) -> None:
        """
        Crea el formulario en base a los parámetros recibidos.
        
        Extrae información de un objeto Base de datos para obtener las puntuaciones 
        y nombres de jugadores registrados.
        
        También crea dos cuadros de texto (uno indicando al jugador que escriba un 
        nombre de cuatro letras y otro que reflejará y registrará lo que el jugador 
        escriba).
        
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
        self.menu_x = self.w / 5
               
        self.score = 0
                  
        self.name = TextBox(master_surface=self,x=self.menu_x-75,y=0,w=300,h=50,background_color=None,border_color=None,background_image=None,text="Nombre (cuatro letras):",font="Verdana",font_size=15,font_color=WHITE)
        self.name_entry = TextBox(master_surface=self,x=self.menu_x,y=40,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_08.png",text="",font="Verdana",font_size=15,font_color=BLACK)
        
        self.lista_widget = [self.name,self.name_entry]
        
        self.game_state = GAME_END
        self.exit = False
        
    def register_name (self) -> None:
        """
        Registra el nombre ingresado por el jugador en el cuadro de texto apropiado.
        
        Corrobora si cumple con los requisitos indicados (cuatro carácteres alfabeticos 
        de extensión). De no ser el caso, vacía el cuadro de texto y se mantiene en el
        formulario.
        
        Si el nombre cumple con los requisitos, comprueba si ya está registrado en la 
        base de datos.
        
        Si ya está registrado, compara la puntuación registrada junto a ese nombre con 
        la puntuación a registrar. Solo actualiza la base de datos si la nueva puntuación
        es más alta.
        
        Si no está registrado, lo registra como una entrada nueva en la base de datos.
        
        No retorna nada.
        """
        
        self.nombre = self.name_entry._text
        self.nombre = self.nombre.upper()
        
        if not (re.match("^[A-Z]{4}$",self.nombre) == None):            
            old_player = Database.check_registered_highscore(self.nombre)
            
            if(old_player):
                higher_score = Database.compare_highscore(self.nombre,self.score)
                if (higher_score):
                    Database.update_highscore(self.nombre,self.score)
            else:
                Database.add_highscore(self.nombre,self.score)
                
            self.set_active("highscore_table")
        else:
            self.name_entry._text = ""
    
    def update(self, lista_eventos:list,score:int) -> None:
        """
        Actualiza los elementos del formulario.
        
        Si el jugador presiona ENTER, ejecuta el método de 
        registro de nombre y puntuación.
        
        Si el jugador presioan ESCAPE, vacía el cuadro de texto 
        y ejecuta el método de retorno a pantalla principal.
        
        No retorna nada.
        
        ----------
        lista_eventos : list
            lista de distintos tipos de eventos registrados por Pygame
        score : int
            puntuación final del jugador
        """
        
        self.score = score
        
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.name_entry._text = ""
                    self.set_active("highscore_table")
                elif event.key == pygame.K_RETURN:
                    self.register_name()   
                    
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
