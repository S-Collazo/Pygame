import pygame
import sys
from pygame.locals import *
from constants import *
from ui_win_main import WinMain
from sounds import Sounds

class Win:
    def __init__ (self,screen,player,time,sounds,spawner=False,boss=False):
        self.screen = screen
        self.win_main = WinMain(player,time,name="win_main",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,background_color=GREY,border_color=None,active=True,spawner=spawner,boss=boss)
        
        self.sounds = sounds
        self.win_sound = "\\sounds\\effects\\win.wav"
        self.sound_flag = True
        
        self.exit = False
        self.next = False
        
    def win_screen (self,delta_ms,lista_eventos,player,time):
        self.game_state = GAME_VICTORY
        
        if(self.sound_flag):
            self.sounds.sound_stop()  
            self.sounds.sound_effect(sound=self.win_sound)
            self.sound_flag = False
                    
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                                         
        if(self.win_main.active):
            self.win_main.update(lista_eventos,player,time)
            self.win_main.draw()
            self.exit = self.win_main.exit
            self.next = self.win_main.next
        else:
            if (self.exit):
                self.game_state = GAME_MENU
            elif (self.next):
                self.game_state = GAME_CONTINUE
            else:
                self.game_state = GAME_RESTART
                    
        return self.game_state