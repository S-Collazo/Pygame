import pygame
import sys
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_button import Button
from ui_textbox import TextBox

class LevelSelector(Form):
    def __init__(self,name,master_surface,x,y,w,h,background_color,border_color,active):
        super().__init__(name,master_surface,x,y,w,h,background_color,border_color,active)
        self.menu_x = self.w / 5
        
        self.lvl1 = Button(master_surface=self,x=self.menu_x + 25,y=10,w=150,h=100,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_XL_06.png",on_click=self.on_click_lvl1,on_click_param=1,text="Nivel 1",font="Verdana",font_size=30,font_color=WHITE)
        self.lvl2 = Button(master_surface=self,x=self.menu_x + 180,y=10,w=150,h=100,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_XL_06.png",on_click=self.on_click_lvl2,on_click_param=2,text="Nivel 2",font="Verdana",font_size=30,font_color=WHITE)
        self.lvl3 = Button(master_surface=self,x=self.menu_x + 335,y=10,w=150,h=100,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_XL_06.png",on_click=self.on_click_lvl3,on_click_param=3,text="Nivel 3",font="Verdana",font_size=30,font_color=WHITE)
        
        self.lvl_easy = Button(master_surface=self,x=self.menu_x,y=35,w=50,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_S_05.png",on_click=self.on_click_lvl_easy,on_click_param=None,text="Facil",font="Verdana",font_size=10,font_color=BLACK)
        self.lvl_normal = Button(master_surface=self,x=self.menu_x + 50,y=35,w=50,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_S_08.png",on_click=self.on_click_lvl_normal,on_click_param=None,text="Normal",font="Verdana",font_size=10,font_color=BLACK)
        self.lvl_hard = Button(master_surface=self,x=self.menu_x + 100,y=35,w=50,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_S_09.png",on_click=self.on_click_lvl_hard,on_click_param=None,text="Dificil",font="Verdana",font_size=10,font_color=BLACK)
        
        self.button_exit = Button(master_surface=self,x=(self.menu_x + 150),y=(self.h - 50),w=150,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_02.png",on_click=self.on_click_button_exit,on_click_param="main",text="Volver",font="Verdana",font_size=20,font_color=BLACK)
        
        self.lista_widget = [self.lvl1,self.lvl2,self.lvl3,self.button_exit]
        
        self.level_number_value = 0
        self.level_difficulty = -1
        
    def on_click_lvl1(self,parametro):
        self.lvl1_x = self.lvl1.x
        self.move_buttons (self.lvl1_x)
        self.level_number_value = parametro
        
    def on_click_lvl2(self,parametro):
        self.lvl2_x = self.lvl2.x
        self.move_buttons (self.lvl2_x)
        self.level_number_value = parametro
        
    def on_click_lvl3(self,parametro):
        self.lvl3_x = self.lvl3.x
        self.move_buttons (self.lvl3_x)
        self.level_number_value = parametro
    
    def on_click_lvl_easy(self, parametro):
        if (self.level_difficulty >= 0):
            self.set_active(parametro)
        self.level_difficulty = 0
    
    def on_click_lvl_normal (self, parametro):
        if (self.level_difficulty >= 0):
            self.set_active(parametro)
        self.level_difficulty = 1
        
    def on_click_lvl_hard (self, parametro):
        if (self.level_difficulty >= 0):
            self.set_active(parametro)
        self.level_difficulty = 2
        
    def on_click_button_exit (self, parametro):
        self.set_active(parametro)
        
    def move_buttons (self,new_x):
        self.lvl_easy.x = new_x
        self.lvl_easy.slave_rect_collide.x = new_x
        self.lvl_normal.x = new_x + 50
        self.lvl_normal.slave_rect_collide.x = new_x + 50
        self.lvl_hard.x = new_x + 100
        self.lvl_hard.slave_rect_collide.x = new_x + 100
        self.lista_widget.append(self.lvl_easy)
        self.lista_widget.append(self.lvl_normal)
        self.lista_widget.append(self.lvl_hard)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()