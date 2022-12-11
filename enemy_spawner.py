import pygame
import random
from constants import *
from auxiliar import Auxiliar
from enemy_goblin import *

class Spawner:
    """Generador aleatorio de enemigos"""
    
    def __init__ (self,difficulty:int,enemy:dict,lista_enemigos:list,gravity:int,frame_rate_ms:int,move_rate_ms:int,sounds) -> None:
        """
        Asigna los parámetros a atributos, inicializa el contador de tiempo pasado y tiempo desde la última generación
        y activa el generador.
        
        No retorna nada.
        
        ----------
        difficulty : int
            dificultad de nivel, modifica la cantidad de enemigos a generar y el intervalo de tiempo
        enemy : dict
            diccionario con toda la información de los enemigos a generar
        lista_enemigos : list
            lista de los enemigos activos en el nivel
        gravity : int
            velocidad de caída
        frame_rate_ms : int
            velocidad de las animaciones     
        move_rate_ms : int
            velocidad de desplazamiento
        sounds
            objeto controlador de sonidos
        """
        
        self.enemy_info = enemy
        self.difficulty = difficulty
        self.enemy_list = lista_enemigos
        self.spawn_quantity = self.enemy_info["enemy_quantity"][self.difficulty]
        self.spawned_enemies = self.spawn_quantity
        self.lv_gravity = gravity
        self.lv_frame_rate_ms = frame_rate_ms
        self.lv_move_rate_ms = move_rate_ms
        self.time_passed = 0
        self.time_last_spawn = 0
        self.sounds = sounds
        self.active = True
        
    def spawn(self,time:int,lista_enemigos:list) -> None:
        """
        Genera un enemigo con tipo y posición elegidas aleatoriamente dentro de una lista.
        
        No aplica si el tiempo pasado desde la última ejecución del método es inferior al intervalo de tiempo indicado 
        o si se supera el máximo de enemigos a generar.
        
        No retorna nada.
        
        ----------
        time : int
            variable de tiempo
        lista_enemigos : list
            lista de los enemigos activos en el nivel
        """
        
        self.lista_enemigos = lista_enemigos
        self.time = time
        self.interval_time_spawn = self.enemy_info["interval_time_spawn"][self.difficulty]
        self.time_passed += time
        
        if (self.spawned_enemies > 0):
            if (self.time_passed - self.time_last_spawn) > (self.interval_time_spawn):
                enemy_type_value = random.randrange(self.enemy_info["enemy_type_number"][self.difficulty])
                enemy_coordinates_value = random.randrange(len(self.enemy_info["enemy_starter_position"]))

                enemy_type = Auxiliar.splitIntoString(self.enemy_info["enemy_type"][self.difficulty],"/")
                enemy_coordinates = Auxiliar.splitIntoInt(self.enemy_info["enemy_starter_position"][enemy_coordinates_value],",")
                
                if (enemy_type[enemy_type_value] == "Standard"):
                    self.lista_enemigos.append(Goblin_Standard(asset=self.enemy_list,x=enemy_coordinates[0],y=enemy_coordinates[1],gravity=self.lv_gravity,frame_rate_ms=self.lv_frame_rate_ms,move_rate_ms=self.lv_move_rate_ms,sounds=self.sounds,p_scale=self.enemy_info["p_scale"]))  
                elif (enemy_type[enemy_type_value] == "Grunt"):
                    self.lista_enemigos.append(Goblin_Grunt(asset=self.enemy_list,x=enemy_coordinates[0],y=enemy_coordinates[1],gravity=self.lv_gravity,frame_rate_ms=self.lv_frame_rate_ms,move_rate_ms=self.lv_move_rate_ms,sounds=self.sounds,p_scale=self.enemy_info["p_scale"]))  
                else:
                    self.lista_enemigos.append(Goblin_Shaman(asset=self.enemy_list,x=enemy_coordinates[0],y=enemy_coordinates[1],gravity=self.lv_gravity,frame_rate_ms=self.lv_frame_rate_ms,move_rate_ms=self.lv_move_rate_ms,sounds=self.sounds,p_scale=self.enemy_info["p_scale"]))

                self.spawned_enemies -= 1
                self.time_last_spawn = self.time_passed
                
    def boss_spawn(self,lista_enemigos:list,ammount:int) -> None:
        """
        Método de generación especial. Genera la cantidad indicada de enemigos con tipo 
        y posición elegidas aleatoriamente dentro de una lista.
        
        No aplica si se supera el máximo de enemigos a generar.
        
        No retorna nada.
        
        ----------
        lista_enemigos : list
            lista de los enemigos activos en el nivel
        ammount : int
            cantidad de enemigos a generar
        """
        
        self.lista_enemigos = lista_enemigos
        self.ammount = ammount
        
        if (self.spawned_enemies > 0):
            for n in range(self.ammount):
                enemy_type_value = random.randrange(self.enemy_info["enemy_type_number"][self.difficulty])
                enemy_coordinates_value = random.randrange(len(self.enemy_info["enemy_starter_position"]))

                enemy_type = Auxiliar.splitIntoString(self.enemy_info["enemy_type"][self.difficulty],"/")
                enemy_coordinates = Auxiliar.splitIntoInt(self.enemy_info["enemy_starter_position"][enemy_coordinates_value],",")
                
                if (enemy_type[enemy_type_value] == "Standard"):
                    self.lista_enemigos.append(Goblin_Standard(asset=self.enemy_list,x=enemy_coordinates[0],y=enemy_coordinates[1],gravity=self.lv_gravity,frame_rate_ms=self.lv_frame_rate_ms,move_rate_ms=self.lv_move_rate_ms,sounds=self.sounds,p_scale=self.enemy_info["p_scale"]))  
                elif (enemy_type[enemy_type_value] == "Grunt"):
                    self.lista_enemigos.append(Goblin_Grunt(asset=self.enemy_list,x=enemy_coordinates[0],y=enemy_coordinates[1],gravity=self.lv_gravity,frame_rate_ms=self.lv_frame_rate_ms,move_rate_ms=self.lv_move_rate_ms,sounds=self.sounds,p_scale=self.enemy_info["p_scale"]))  
                else:
                    self.lista_enemigos.append(Goblin_Shaman(asset=self.enemy_list,x=enemy_coordinates[0],y=enemy_coordinates[1],gravity=self.lv_gravity,frame_rate_ms=self.lv_frame_rate_ms,move_rate_ms=self.lv_move_rate_ms,sounds=self.sounds,p_scale=self.enemy_info["p_scale"]))

            self.spawned_enemies -= self.ammount
            