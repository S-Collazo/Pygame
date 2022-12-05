import pygame
import sys
from pygame.locals import *
from constants import *
from ui_death_main import DeathMain
from sounds import Sounds

class Death:
    def __init__ (self,screen,sounds):
        self.screen = screen
        self.death_main = DeathMain(name="death_main",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,background_color=BLACK,border_color=None,active=True)
        
        self.sounds = sounds
        self.death_sound = "\\sounds\\effects\\death.wav"
        self.sound_flag = True
        
        self.exit = False
        
    def death_screen (self,delta_ms,lista_eventos):
        self.game_state = GAME_DEATH
        
        if(self.sound_flag):    
            self.sounds.sound_stop()
            self.sounds.sound_effect(sound=self.death_sound)
            self.sound_flag = False
            
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                                    
        if(self.death_main.active):
            self.death_main.update(lista_eventos)
            self.death_main.draw()
            self.exit = self.death_main.exit
        else:
            if (self.exit):
                self.game_state = GAME_MENU
                return self.game_state
            else:
                self.game_state = GAME_RESTART
                return self.game_state
                    
        return self.game_state