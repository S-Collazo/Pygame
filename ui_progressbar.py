import pygame
from pygame.locals import *
from ui_widget import Widget
from constants import *

class ProgressBar(Widget):
    def __init__(self,master_surface,x=10,y=10,w=200,h=50,background_color=GREEN,border_color=RED,background_image=None,image_progress=None,value=1,value_max=5):
        super().__init__(master_surface,x,y,w,h,background_color,border_color,background_image,None,None,None,None)
       
        self.surface_element = pygame.image.load(image_progress)
        self.surface_element = pygame.transform.scale(self.surface_element,(w/value_max, h)).convert_alpha()

        self.value = value
        self.value_max = value_max
        self.render()
        
    def render(self):
        super().render()
        for x in range(self.value):
            self.slave_surface.blit(self.surface_element, (x*self.w/self.value_max, 0))

    def update(self,lista_eventos):
        self.render()
        
class HitpointBar(Widget):
    def __init__(self,entity,master_surface,x=5,y=0,w=200,h=25,background_color=None,border_color=BLACK):
        self.background_image=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Bars/Bar_Background01.png"
        self.image_progress=PATH_RECURSOS + "/images/gui/set_gui_01/Paper/Bars/Bar_Segment01.png"
        super().__init__(master_surface,x,y,w,h,background_color,border_color,self.background_image,None,None,None,None)
       
        self.value = entity.hitpoints
        self.value_max = entity.hitpoints_max
       
        self.surface_element = pygame.image.load(self.image_progress)
        self.surface_element = pygame.transform.scale(self.surface_element,(w/self.value_max, h)).convert_alpha()

        self.render(entity)
        
    def render(self,entity):
        if(entity.hitpoints > 0):
            self.value = entity.hitpoints
        else:
            self.value = 0
        super().render()
        for x in range(self.value):
            self.slave_surface.blit(self.surface_element, (x*self.w/self.value_max, 0))

    def update(self,lista_eventos,entity,timer):
        self.render(entity)