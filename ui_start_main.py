import pygame
import sys
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_button import Button

class StartMain(Form):
    def __init__(self,name,master_surface,x,y,w,h,background_color,border_color,active):
        super().__init__(name,master_surface,x,y,w,h,background_color,border_color,active)
        self.menu_x = self.w / 2
        
        self.button_play = Button(master_surface=self,x=self.menu_x + 25,y=75,w=150,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_07.png",on_click=self.on_click_button_play,on_click_param="level_selector",text="Jugar",font="Verdana",font_size=20,font_color=BLACK)
        self.button_options = Button(master_surface=self,x=self.menu_x + 25,y=140,w=150,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_07.png",on_click=self.on_click_button_options,on_click_param="options",text="Opciones",font="Verdana",font_size=20,font_color=BLACK)
        self.button_exit = Button(master_surface=self,x=self.menu_x + 25,y=205,w=150,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_07.png",on_click=self.on_click_button_exit,on_click_param=None,text="Cerrar Juego",font="Verdana",font_size=20,font_color=BLACK)
        
        self.lista_widget = [self.button_play,self.button_options,self.button_exit]
        
    def on_click_button_play(self,parametro) -> bool:
        self.set_active(parametro)

    def on_click_button_options(self, parametro):
        self.set_active(parametro)
    
    def on_click_button_exit (self, parametro):
            pygame.quit()
            sys.exit()

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()