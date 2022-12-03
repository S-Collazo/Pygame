import pygame
from pygame.locals import *
from constants import *
from auxiliar import Auxiliar
from ui_widget import Widget
from ui_button import Button

class Form ():
    forms_dict = {}
    def __init__ (self,name,master_surface,x,y,w,h,background_color,border_color,active):
        self.forms_dict[name] = self
        self.master_form = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.background_color = background_color
        self.border_color = border_color
        
        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        
        self.active = active
             
        if(self.background_color != None):
            self.surface.fill(self.background_color)
        else:
            self.surface = pygame.Surface((w,h))
            self.surface = self.surface.convert_alpha()
            self.surface.fill((0, 0, 0, 0))
            
    def set_active(self,name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        if (name != None):
            self.forms_dict[name].active = True

    def render(self):
        pass

    def update(self,lista_eventos):
        pass

    def draw(self):
        self.master_form.blit(self.surface,self.slave_rect)
    
class FormMenu(Form):
    def __init__ (self,master_surface,x,y,w,h,background_color,border_color,active):
        super().__init__(master_surface,x,y,w,h,background_color,border_color,active)
        
        self.boton1 = Button(master=self,x=100,y=50,w=200,h=50,background_color=(255,0,0),border_color=(255,0,255),on_click=self.on_click_boton1,on_click_param="1234",text="MENU",font="Verdana",font_size=30,font_color=(0,255,0))
        self.boton2 = Button(master=self,x=200,y=50,w=200,h=50,background_color=(255,0,0),border_color=(255,0,255),on_click=self.on_click_boton1,on_click_param="8",text="MENU 2",font="Verdana",font_size=30,font_color=(0,255,0))
        self.lista_widget = [self.boton1,self.boton2]
     
    def on_click_boton1(self, parametro):
        print("CLICK",parametro)
        
    def update(self,lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)
        
    def draw (self):
        super().draw()
        for aux_boton in self.lista_widget:
            aux_boton.draw()