import pygame
import sys
from pygame.locals import *
from constants import *
from ui_start_main import StartMain
from ui_start_options import StartOptions
from ui_start_level_selector import LevelSelector

class Start:
    def __init__ (self,screen):
        self.screen = screen
        
        self.background_image = pygame.image.load(PATH_RECURSOS + "\\images\\background.png")
        self.background_image = pygame.transform.scale(self.background_image,(ANCHO_VENTANA,ALTO_VENTANA))
        
        self.start_main = StartMain(name="main",master_surface = self.screen,x=100,y=250,w=600,h=300,background_color=None,border_color=None,active=True)
        self.start_options = StartOptions(name="options",master_surface = self.screen,x=100,y=200,w=600,h=300,background_color=None,border_color=None,active=False)
        self.level_selector = LevelSelector(name="level_selector",master_surface = self.screen,x=100,y=200,w=600,h=300,background_color=None,border_color=None,active=False)

        self.level_number_value = 0
        self.level_difficulty = 0
        
    def start_menu (self,delta_ms,lista_eventos,keys):
        self.game_state = GAME_MENU
        
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                                 
        self.screen.blit(self.background_image,self.background_image.get_rect())
          
        if(self.start_main.active):
            self.start_main.update(lista_eventos)
            self.start_main.draw()
        elif(self.start_options.active):
            self.start_options.update(lista_eventos)
            self.start_options.draw()
        elif(self.level_selector.active):
            self.level_selector.update(lista_eventos)
            self.level_selector.draw()
        else:
            self.level_number_value = self.level_selector.level_number_value
            self.level_difficulty = self.level_selector.level_difficulty
            self.game_state = GAME_RUNNING
               
        return self.game_state 