import pygame
import sys
from pygame.locals import *
from constants import *
from player import Player
from enemy import Enemy
from plataform import Platform
from level import Level
from auxiliar import Auxiliar

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA),flags, 16)

pygame.init()

clock = pygame.time.Clock()
delta_ms = clock.tick(FPS)

imagen_fondo = pygame.image.load(PATH_RECURSOS + "\\images\\locations\\set_bg_06\\creepy_forest.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

player_1 = Player(asset="knight_main",x=400,y=GROUND_LEVEL-100,gravity=10,frame_rate_ms=100,move_rate_ms=60)

enemy_1 = Enemy(asset="knight_main",x=800,y=0,gravity=10,frame_rate_ms=100,move_rate_ms=60)

lista_personajes = []
lista_personajes.append(player_1)

lista_enemigos = []
lista_enemigos.append(enemy_1)

lista_plataformas = []
lista_plataformas.append(Platform(x=0,y=GROUND_LEVEL,w=ANCHO_VENTANA,h=GROUND_RECT_H,type=1))
Level.createPlaforms(lista_plataformas,x=350,y=550,w=50,h=50,tile_total=5,p_scale=0.4,collition_enabled=True)
Level.createPlaforms(lista_plataformas,x=600,y=450,w=50,h=50,tile_total=4,p_scale=0.4,collition_enabled=True)
Level.createPlaforms(lista_plataformas,x=800,y=350,w=50,h=50,tile_total=4,p_scale=0.4,collition_enabled=True)
Level.createPlaforms(lista_plataformas,x=400,y=250,w=50,h=50,tile_total=5,p_scale=0.4,collition_enabled=True)
Level.createPlaforms(lista_plataformas,x=200,y=150,w=50,h=50,tile_total=4,p_scale=0.4,collition_enabled=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
    keys = pygame.key.get_pressed()
        
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    
    for plataforma in lista_plataformas:
        Platform.draw(plataforma,screen)
       
    player_1.events(delta_ms,keys)   
    player_1.update(delta_ms,lista_plataformas,lista_enemigos)
    player_1.draw(screen)

    if(enemy_1.lives > 0):
        enemy_1.update(delta_ms,lista_plataformas,lista_personajes)
        enemy_1.draw(screen)
                
    if(DEBUG):
        Auxiliar.drawGrid(screen,100)
   
    # screen.fill(FILTER_PURPLE,imagen_fondo.get_rect(),BLEND_RGBA_ADD)
         
    pygame.display.flip()