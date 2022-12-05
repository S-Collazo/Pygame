import pygame
from ui_start import Start
from ui_pause import Pause
from ui_death import Death
from ui_win import Win
from ui_highscore import Highscore
from level import Level
from pygame.locals import *
from constants import *
from loot import *
from damage_control import *
from sounds import Sounds

flags = DOUBLEBUF

game_state = GAME_MENU

level_number = 0
level_difficulty = 0
score_list = [0,0,0]

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA),flags, 16)

pygame.init()

clock = pygame.time.Clock()

while True:
    sounds = Sounds()
    start = Start(screen,sounds)
    pause_menu = Pause(screen,sounds)
    death = Death(screen,sounds)
    
    while (game_state == GAME_MENU):
            lista_eventos = pygame.event.get()
            keys = pygame.key.get_pressed()                
            delta_ms = clock.tick(FPS)
                
            game_state = start.start_menu(delta_ms,lista_eventos,keys)
            
            pygame.mixer.stop()
            
            level_number = start.level_number_value
            level_difficulty = start.level_difficulty
            
            pygame.display.flip()

    else:
        if (game_state == GAME_RESTART or game_state == GAME_CONTINUE):
            if (game_state == GAME_CONTINUE):
                level_number += 1
            game_state = GAME_RUNNING
            
        try:
            level = Level(screen,level_number,level_difficulty,sounds)
            win = Win(screen,level.lista_personajes[0],level.time_final,sounds,level.has_spawner,level.boss_room)
        except:
            game_state = GAME_END
            
        highscore = Highscore(screen,sounds)
                
        while not (game_state == GAME_MENU or game_state == GAME_RESTART or game_state == GAME_CONTINUE):
            while (game_state == GAME_PAUSE):
                lista_eventos = pygame.event.get()
                keys = pygame.key.get_pressed()                
                delta_ms = clock.tick(FPS)
                
                start.start_main.active = True
                win.win_main.active = True
                death.death_main.active = True
                            
                game_state = pause_menu.pause_level(delta_ms,lista_eventos)
                
                pygame.display.flip()
                    
            while (game_state == GAME_RUNNING):
                lista_eventos = pygame.event.get()
                keys = pygame.key.get_pressed()                
                delta_ms = clock.tick(FPS)
                
                start.start_main.active = True
                pause_menu.pause_main.active = True
                win.win_main.active = True
                death.death_main.active = True
                
                game_state = level.run_level(delta_ms,lista_eventos,keys)
                    
                pygame.display.flip()
                
            while (game_state == GAME_DEATH):
                lista_eventos = pygame.event.get()
                keys = pygame.key.get_pressed()                
                delta_ms = clock.tick(FPS)
                
                start.start_main.active = True
                win.win_main.active = True
                pause_menu.pause_main.active = True
                
                game_state = death.death_screen(delta_ms,lista_eventos)
                
                pygame.display.flip()
                
            while (game_state == GAME_VICTORY):
                lista_eventos = pygame.event.get()
                keys = pygame.key.get_pressed()                
                delta_ms = clock.tick(FPS)
                
                start.start_main.active = True
                pause_menu.pause_main.active = True
                death.death_main.active = True
                
                game_state = win.win_screen(delta_ms,lista_eventos,level.lista_personajes[0],level.time_final)
                
                score_list[(level_number - 1)] = win.win_main.final_score
                    
                pygame.display.flip()
                    
            while (game_state == GAME_END):
                lista_eventos = pygame.event.get()
                keys = pygame.key.get_pressed()                
                delta_ms = clock.tick(FPS)
                
                start.start_main.active = True
                pause_menu.pause_main.active = True
                death.death_main.active = True
                
                game_state = highscore.highscore_screen(delta_ms,lista_eventos,score_list)
                                
                pygame.display.flip()