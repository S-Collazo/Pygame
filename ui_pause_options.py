import pygame
import sys
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_button import Button
from ui_textbox import TextBox

class PauseOptions(Form):
    def __init__(self,name,master_surface,x,y,w,h,background_color,border_color,active,sounds):
        super().__init__(name,master_surface,x,y,w,h,background_color,border_color,active)
        self.menu_x = self.w / 5
        
        self.sounds = sounds
        self.mute_state = False
        
        self.button_sounds_mute_on = Button(master_surface=self,x=self.menu_x,y=100,w=25,h=25,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_S_08.png",on_click=self.on_click_button_sounds_mute,on_click_param=True,text="ON",font="Verdana",font_size=10,font_color=BLACK)
        self.button_sounds_mute_off = Button(master_surface=self,x=self.menu_x + 55,y=100,w=25,h=25,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_S_06.png",on_click=self.on_click_button_sounds_mute,on_click_param=False,text="OFF",font="Verdana",font_size=10,font_color=BLACK)
        
        self.button_sound_low = Button(master_surface=self,x=self.menu_x,y=160,w=25,h=25,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_S_05.png",on_click=self.on_click_button_sound_volume,on_click_param=0.25,text="Bajo",font="Verdana",font_size=10,font_color=BLACK)
        self.button_sound_mid = Button(master_surface=self,x=self.menu_x + 55,y=160,w=25,h=25,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_S_08.png",on_click=self.on_click_button_sound_volume,on_click_param=0.50,text="Medio",font="Verdana",font_size=10,font_color=BLACK)
        self.button_sound_high = Button(master_surface=self,x=self.menu_x + 110,y=160,w=25,h=25,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_S_09.png",on_click=self.on_click_button_sound_volume,on_click_param=1.00,text="Alto",font="Verdana",font_size=10,font_color=BLACK)
     
        self.button_music_low = Button(master_surface=self,x=self.menu_x,y=220,w=25,h=25,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_S_05.png",on_click=self.on_click_button_music_volume,on_click_param=0.25,text="Baja",font="Verdana",font_size=10,font_color=BLACK)
        self.button_music_mid = Button(master_surface=self,x=self.menu_x + 55,y=220,w=25,h=25,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_S_08.png",on_click=self.on_click_button_music_volume,on_click_param=0.50,text="Medie",font="Verdana",font_size=10,font_color=BLACK)
        self.button_music_high = Button(master_surface=self,x=self.menu_x + 110,y=220,w=25,h=25,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_S_09.png",on_click=self.on_click_button_music_volume,on_click_param=1.00,text="Alta",font="Verdana",font_size=10,font_color=BLACK)
     
        self.button_exit = Button(master_surface=self,x=self.menu_x + 50,y=255,w=150,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_05.png",on_click=self.on_click_button_exit,on_click_param="pause_main",text="Volver",font="Verdana",font_size=20,font_color=BLACK)
              
        self.txt1 = TextBox(master_surface=self,x=self.menu_x,y=10,w=240,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_XL_06.png",text="Opciones",font="Verdana",font_size=30,font_color=WHITE)
        self.txt2 = TextBox(master_surface=self,x=self.menu_x,y=70,w=200,h=25,background_color=None,border_color=None,background_image=None,text="Silenciar juego:",font="Verdana",font_size=15,font_color=WHITE)
        self.txt3 = TextBox(master_surface=self,x=self.menu_x,y=125,w=200,h=25,background_color=None,border_color=None,background_image=None,text="Volumen de sonidos:",font="Verdana",font_size=15,font_color=WHITE)
        self.txt4 = TextBox(master_surface=self,x=self.menu_x,y=185,w=200,h=25,background_color=None,border_color=None,background_image=None,text="Volumen de musica:",font="Verdana",font_size=15,font_color=WHITE)
        
        self.lista_widget = [self.button_sounds_mute_on,self.button_sounds_mute_off,self.button_sound_low,self.button_sound_mid,self.button_sound_high,self.button_music_low,self.button_music_mid,self.button_music_high,self.button_exit,self.txt1,self.txt2,self.txt3,self.txt4]

    def on_click_button_sounds_mute(self,parametro):
        self.mute_state = parametro
        self.sounds.music_pause(parametro)

    def on_click_button_sound_volume (self, parametro):
        self.sounds.set_sound_volume(parametro)
        
    def on_click_button_music_volume (self, parametro):
        self.sounds.set_music_volume(parametro)
    
    def on_click_button_exit (self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()