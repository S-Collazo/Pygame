import pygame
import json
from constants import *

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path, columnas, filas,flip=False, step = 1):
        lista_sprite = []
        surface_image = pygame.image.load(path)
        
        fotograma_ancho = int(surface_image.get_width() / columnas)
        fotograma_alto = int(surface_image.get_height() / filas)
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_image.subsurface(x,y,fotograma_ancho,fotograma_alto)
                
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
                
                lista_sprite.append(surface_fotograma)
                
        return lista_sprite
    
    @staticmethod
    def getSurfaceFromSeparateFiles(path_format,quantity,flip=False,step = 1,scale=1,w=0,h=0,repeat_frame=1):     
        lista = []
        for i in range(step,quantity):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
            if(scale != 1):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista
    
    @staticmethod
    def getSurfaceFromJson(asset,animation,flip=False,p_scale=1):
        asset_folder = asset["asset_folder"]
        asset_anim = asset["animations"]
        sprite = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + asset_anim[animation]["path"] + "{:03d}.png",asset_anim[animation]["quantity"],flip=flip,step = 0,scale=p_scale,repeat_frame=1)
        return sprite
    
    @staticmethod
    def drawGrid(screen,block_size=10):
        for x in range(0, ANCHO_VENTANA, block_size):
            for y in range(0, ALTO_VENTANA, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(screen, WHITE, rect, 1)
                
    @staticmethod
    def readJson(file):
        with open(file, 'r') as f:
            data = json.load(f)
        return data
    
    @staticmethod
    def splitIntoString(text,splitter):
        split_text = text.split(splitter)
        return split_text
    
    @staticmethod
    def splitIntoInt(text,splitter):
        split_text = Auxiliar.splitIntoString(text,splitter)
        int_text = list(map(int,split_text))
        return int_text
    
