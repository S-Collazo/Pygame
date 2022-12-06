import pygame
import sys
import re
import random
from pygame.locals import *
from constants import *
from ui_form import Form
from ui_button import Button
from ui_textbox import TextBox
from database import Database

class HighscoreTable(Form):
    def __init__(self,name,master_surface,x,y,w,h,background_color,border_color,active):
        super().__init__(name,master_surface,x,y,w,h,background_color,border_color,active)
        self.menu_x = self.w / 4

        self.score = 0
        
        self.highscore_list = Database.display_all_highscore()
                        
        self.button_register_score = Button(master_surface=self,x=self.menu_x + 50,y=600,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_L_07.png",on_click=self.on_click_button_register_score,on_click_param="highscore_register",text="Registrar puntuación",font="Verdana",font_size=15,font_color=WHITE)
        self.button_exit = Button(master_surface=self,x=self.menu_x + 50,y=660,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_L_06.png",on_click=self.on_click_button_exit,on_click_param=None,text="Menu Principal",font="Verdana",font_size=20,font_color=WHITE)
              
        self.txt1 = TextBox(master_surface=self,x=self.menu_x + 100,y=50,w=300,h=150,background_color=None,border_color=None,background_image=None,text="TABLA DE PUNTUACIONES",font="Verdana",font_size=20,font_color=BLACK)
        
        self.highscore_name_1 = TextBox(master_surface=self,x=self.menu_x,y=210,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=self.highscore_list[0][1],font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_score_1 = TextBox(master_surface=self,x=self.menu_x + 200,y=210,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=str(self.highscore_list[0][2]),font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_name_2 = TextBox(master_surface=self,x=self.menu_x,y=260,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=self.highscore_list[1][1],font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_score_2 = TextBox(master_surface=self,x=self.menu_x + 200,y=260,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=str(self.highscore_list[1][2]),font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_name_3 = TextBox(master_surface=self,x=self.menu_x,y=310,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=self.highscore_list[2][1],font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_score_3 = TextBox(master_surface=self,x=self.menu_x + 200,y=310,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=str(self.highscore_list[2][2]),font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_name_4 = TextBox(master_surface=self,x=self.menu_x,y=360,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=self.highscore_list[3][1],font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_score_4 = TextBox(master_surface=self,x=self.menu_x + 200,y=360,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=str(self.highscore_list[3][2]),font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_name_5 = TextBox(master_surface=self,x=self.menu_x,y=410,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=self.highscore_list[4][1],font="Verdana",font_size=15,font_color=WHITE)
        self.highscore_score_5 = TextBox(master_surface=self,x=self.menu_x + 200,y=410,w=200,h=50,background_color=None,border_color=None,background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Buttons/Button_M_06.png",text=str(self.highscore_list[4][2]),font="Verdana",font_size=15,font_color=WHITE)
        
        self.lista_widget = [self.button_register_score,self.button_exit,self.txt1,self.highscore_name_1,self.highscore_score_1,self.highscore_name_2,self.highscore_score_2,self.highscore_name_3,self.highscore_score_3,self.highscore_name_4,self.highscore_score_4,self.highscore_name_5,self.highscore_score_5]
        
        self.game_state = GAME_END
        self.exit = False
    
    def on_click_button_register_score (self,parametro):
        self.set_active(parametro)
                
    def on_click_button_exit (self, parametro):
        self.set_active(parametro)
        self.exit = True

    def update(self, lista_eventos):
        self.highscore_list = Database.display_all_highscore()
        self.highscore_name_1._text = self.highscore_list[0][1]
        self.highscore_score_1._text = str(self.highscore_list[0][2])
        self.highscore_name_2._text = self.highscore_list[1][1]
        self.highscore_score_2._text = str(self.highscore_list[1][2])
        self.highscore_name_3._text = self.highscore_list[2][1]
        self.highscore_score_3._text = str(self.highscore_list[2][2])
        self.highscore_name_4._text = self.highscore_list[3][1]
        self.highscore_score_4._text = str(self.highscore_list[3][2])
        self.highscore_name_5._text = self.highscore_list[4][1]
        self.highscore_score_5._text = str(self.highscore_list[4][2])
        
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()