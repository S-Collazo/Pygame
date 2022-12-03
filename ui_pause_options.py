import pygame
import sys
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_button import Button
from ui_textbox import TextBox

class PauseOptions(Form):
    def __init__(self,name,master_surface,x,y,w,h,background_color,border_color,active):
        super().__init__(name,master_surface,x,y,w,h,background_color,border_color,active)
        self.menu_x = self.w / 5
        
        #self.button_continue = Button(master_surface=self,x=self.menu_x + 50,y=75,w=150,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_M_09.png",on_click=self.on_click_button_continue,on_click_param=False,text="Reanudar",font="Verdana",font_size=20,font_color=BLACK)
        #self.button_options = Button(master_surface=self,x=self.menu_x + 50,y=140,w=150,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/gui/set_gui_01/Paper/Buttons/Button_M_08.png",on_click=self.on_click_button_options,on_click_param="options_menu",text="Opciones",font="Verdana",font_size=20,font_color=BLACK)
        self.button_exit = Button(master_surface=self,x=self.menu_x + 50,y=205,w=150,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_05.png",on_click=self.on_click_button_exit,on_click_param="pause_main",text="Volver",font="Verdana",font_size=20,font_color=BLACK)
              
        self.txt1 = TextBox(master_surface=self,x=self.menu_x,y=10,w=240,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_XL_06.png",text="Opciones",font="Verdana",font_size=30,font_color=WHITE)
        
        #self.lista_widget = [self.button_continue,self.button_options,self.button_exit,self.txt1]
        self.lista_widget = [self.button_exit,self.txt1]

    def on_click_button_continue(self,parametro) -> bool:
        self.set_active(parametro)

    def on_click_button_options(self, parametro):
        self.set_active(parametro)
    
    def on_click_button_exit (self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()