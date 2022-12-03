import pygame
from pygame.locals import *
from constants import *

class Widget:
    def __init__ (self,master_surface,x,y,w,h,background_color,border_color,background_image,text,font,font_size,font_color,bold=False):
        self.master_form = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.background_color = background_color
        self.border_color = border_color
        
        if background_image != None:
            self.background_image = pygame.image.load(background_image)
            self.background_image = pygame.transform.scale(self.background_image,(w, h)).convert_alpha()
        else:
            self.background_image = pygame.Surface((w, h))
            self.background_image = self.background_image.convert_alpha()
            self.background_image.fill((0, 0, 0, 0))
            
        self._text = text
        if(self._text != None):
            pygame.font.init()
            self._font_sys = pygame.font.SysFont(font,font_size,bold)
            self._font_color = font_color
    
    def render (self):
        self.slave_surface = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y
        
        if self.background_color:
            self.slave_surface.fill(self.background_color)
        
        if self.background_image:
            self.slave_surface.blit(self.background_image,(0,0))
        
        if(self._text != None):
            image_text = self._font_sys.render(self._text,True,self._font_color,self.background_color)
            self.slave_surface.blit(image_text,[
                self.slave_rect.width/2 - image_text.get_rect().width/2,
                self.slave_rect.height/2 - image_text.get_rect().height/2
            ])
            
        if self.border_color:
            pygame.draw.rect(self.slave_surface, self.border_color, self.slave_surface.get_rect(), 2)
            
    def update (self):
        pass
    
    def draw (self):
        self.master_form.surface.blit(self.slave_surface,self.slave_rect)