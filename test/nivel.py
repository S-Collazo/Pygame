import pygame
from constants import *
from plataform import Platform

class Level:
    def createPlaforms(lista_plataformas,x,y,w,h,step=1,tile_total=2,p_scale=1,tile_type=0,collition_enabled=True,add_bottom=False):              
        type_start = tile_type
        type_mid = type_start + 1
        type_end = type_mid + 1
        
        lista_plataformas.append(Platform(x=x,y=y,w=w,h=h,type=type_start,p_scale=p_scale,collition_enabled=collition_enabled))
        for n in range(step,tile_total - 1):
            tile_separation = h * n
            lista_plataformas.append(Platform(x=x + tile_separation,y=y,w=w,h=h,type=type_mid,p_scale=p_scale,collition_enabled=collition_enabled))
        tile_separation = h * (tile_total - 1)
        lista_plataformas.append(Platform(x=x + tile_separation,y=y,w=w,h=h,type=type_end,p_scale=p_scale,collition_enabled=collition_enabled))

        if(add_bottom):
            tile_range = int((GROUND_LEVEL - y) / h)

            for n in range(step,tile_range):
                y_position = y + (h * n)
                Level.createPlaforms(lista_plataformas,x=x,y=y_position,w=w,h=h,tile_total=tile_total,p_scale=p_scale,tile_type=3,collition_enabled=False)