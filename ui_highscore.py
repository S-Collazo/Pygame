import pygame
import sys
from pygame.locals import *
from constants import *
from ui_highscore_main import HighscoreMain
from ui_highscore_table import HighscoreTable
from ui_highscore_register import HighscoreRegister
from sounds import Sounds

class Highscore:
    """Pantalla de puntuaciones del juego."""
    
    def __init__ (self,screen,sounds) -> None:
        """
        Crea los formularios de la pantalla de puntuaciones.
              
        No retorna nada.
              
        ----------
        screen
            superficie en la que se renderizan los formularios
        sounds
            objeto controlador de sonidos
        """
        
        self.screen = screen
        
        self.background_image = pygame.image.load(PATH_RECURSOS + "\\images\\background_end.png")
        self.background_image = pygame.transform.scale(self.background_image,(ANCHO_VENTANA,ALTO_VENTANA))
        
        self.highscore_main = HighscoreMain(name="highscore_main",master_surface=screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,background_color=None,border_color=None,active=True)
        self.highscore_table = HighscoreTable(name="highscore_table",master_surface=screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,background_color=None,border_color=None,active=False)
        self.highscore_register = HighscoreRegister(name="highscore_register",master_surface=screen,x=300,y=300,w=300,h=100,background_color=BLACK,border_color=None,active=False)
        
        self.sounds = sounds
        self.highscore_sound = "\\sounds\\effects\\highscore.wav"
        self.sound_flag = True
        
        self.score = 0
        self.exit = False
        
    def highscore_screen (self,delta_ms:int,lista_eventos:list,score_list:list) -> int:
        """
        Controla el estado de los formularios de la pantalla de puntuaciones. Si están activos, los
        actualiza y renderiza.
        
        Si es la primera vez que se ejecuta, silencia todos los efectos de sonidos previos, 
        y reproduce el efecto de sonido asignado.
        
        Si el formulario principal está activo, extrae de este la variable de puntuación final.
        
        Si no queda ningún formulario activo y el último formulario devolvió la variable de salida como True, 
        regresa el juego al menú principal.
        
        Retorna el estado de juego.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_eventos : list
            lista de distintos tipos de eventos registrados por Pygame
        score_list : list
            puntuación del jugador en cada nivel
        """
        
        self.game_state = GAME_END
         
        if(self.sound_flag):    
            self.sounds.sound_stop()
            self.sounds.sound_effect(sound=self.highscore_sound)
            self.sound_flag = False
            
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        self.screen.blit(self.background_image,self.background_image.get_rect())
                                         
        if(self.highscore_main.active):
            self.highscore_main.update(lista_eventos,score_list)
            self.highscore_main.draw()
            self.score = self.highscore_main.final
            self.exit = self.highscore_main.exit
        elif(self.highscore_table.active):
            self.highscore_table.update(lista_eventos)
            self.highscore_table.draw()
            self.exit = self.highscore_table.exit
        elif(self.highscore_register.active):
            self.highscore_register.update(lista_eventos,self.score)
            self.highscore_register.draw()
            self.exit = self.highscore_register.exit
        else:
            if (self.exit):
                self.game_state = GAME_MENU
                    
        return self.game_state
