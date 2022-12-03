import pygame
from pygame.locals import *
from constants import *
from auxiliar import Auxiliar
from ui_widget import Widget
    
class Button(Widget):
    def __init__ (self,master_surface,x=0,y=0,w=200,h=50,background_color=GREEN,border_color=RED,background_image=None,text="Button",font="Arial",font_size=14,font_color=BLUE,on_click=None,on_click_param=None):
        super().__init__(master_surface,x,y,w,h,background_color,border_color,background_image,text,font,font_size,font_color)
        
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
                
        self.render()
            
    def render (self):
        super().render()
        
        if self.state == M_STATE_HOVER:
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.state == M_STATE_CLICK:
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 
                         
    def update (self,lista_eventos):
        self.slave_rect_collide.x = self.x
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if(pygame.mouse.get_pressed()[0]):
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER
              
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if(self.slave_rect_collide.collidepoint(evento.pos)):
                    self.on_click(self.on_click_param)

        self.render()