import pygame
import sys
from pygame.locals import *
from constants import *
from ui_pause_main import PauseMain
from ui_pause_options import PauseOptions
from sounds import Sounds

class Pause:
    def __init__ (self,screen,sounds):
        self.screen = screen
        self.pause_main = PauseMain(name="pause_main",master_surface = screen,x=300,y=200,w=400,h=300,background_color=BLACK,border_color=None,active=True)
        self.pause_options = PauseOptions(name="pause_options",master_surface = screen,x=300,y=200,w=400,h=300,background_color=BLACK,border_color=None,active=False,sounds=sounds)
        
        self.sounds = sounds
        self.mute_state = False
        
        self.exit = False
        
    def pause_level (self,delta_ms,lista_eventos):
        self.game_state = GAME_PAUSE
        
        self.sounds.music_pause()
        
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.sounds.music_pause(self.mute_state)
                    self.game_state = GAME_RUNNING
                    return self.game_state
                                    
        if(self.pause_main.active):
            self.pause_main.update(lista_eventos)
            self.pause_main.draw()
            self.exit = self.pause_main.exit
        elif(self.pause_options.active):
            self.pause_options.update(lista_eventos)
            self.pause_options.draw()
            self.mute_state = self.pause_options.mute_state
        else:
            if (self.exit):
                self.game_state = GAME_MENU
            else:
                self.sounds.music_pause(self.mute_state)
                self.game_state = GAME_RUNNING
                    
        return self.game_state