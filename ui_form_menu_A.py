import pygame
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_button import Button
from ui_textbox import TextBox
from ui_progressbar import ProgressBar


class FormMenuA(Form):
    def __init__(self,name,master_surface,x,y,w,h,background_color,border_color,active):
        super().__init__(name,master_surface,x,y,w,h,background_color,border_color,active)

        self.boton1 = Button(master_surface=self,x=0,y=0,w=140,h=50,background_color=(255,0,0),border_color=(255,0,255),on_click=self.on_click_boton1,on_click_param="form_menu_B",text="ABRIR B",font="Verdana",font_size=30,font_color=(0,255,0))
        self.boton2 = Button(master_surface=self,x=0,y=60,w=140,h=50,background_color=(255,0,0),border_color=(255,0,255),on_click=self.on_click_boton1,on_click_param="form_menu_B",text="MENU 2",font="Verdana",font_size=30,font_color=(0,255,0))
        self.boton3 = Button(master_surface=self,x=0,y=120,w=140,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_menu_B",text="MENU",font="Verdana",font_size=30,font_color=WHITE)
              
        self.txt1 = TextBox(master_surface=self,x=200,y=50,w=240,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",text="Text",font="Verdana",font_size=30,font_color=BLACK)
        self.pb1 = ProgressBar(master_surface=self,x=500,y=50,w=240,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress=PATH_RECURSOS + "/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 3, value_max=8)
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.txt1,self.pb1]

    def on_click_boton1(self, parametro):
        self.pb1.value += 1

    def on_click_boton2(self, parametro):
        self.pb1.value -= 1
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()