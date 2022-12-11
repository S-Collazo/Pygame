import pygame
from constants import *
from entity import Entity
from ammo import Ammo

class Player(Entity):
    def __init__ (self,asset:dict,name:str,x:int,y:int,gravity:int,frame_rate_ms:int,move_rate_ms:int,sounds,direction_inicial:int=DIRECTION_R,p_scale:float=0.1) -> None:
        """
        Extrae información del diccionario para generar un personaje jugador (base en clase Entity).
                
        No retorna nada.
        
        ----------
        asset : dict
            diccionario con toda la información del personaje
        name : str
            tipo de jugador del personaje
        x : int
            coordenada X en la que aparece el personaje al inicio del nivel
        y : int
            coordenada Y en la que aparece el personaje al inicio del nivel
        gravity : int
            velocidad de caída
        frame_rate_ms : int
            velocidad de las animaciones     
        move_rate_ms : int
            velocidad de desplazamiento
        sounds
            objeto controlador de sonidos
        direction_inicial : int
            dirección del personaje al inicio del nivel. Por defecto, derecha
        p_scale : float
            escala del sprite. Por defecto, 0.1
        """
        
        self.asset = asset["Player"][name]
        
        super().__init__(self.asset,x,y,gravity,frame_rate_ms,move_rate_ms,sounds,direction_inicial,p_scale)
    
        self.currency = 0
                                                                                     
    def update(self,delta_ms:int,lista_plataformas:list) -> None:
        """
        Ejecuta el método update heredado, actualizando los atributos de tiempo pasado y plataformas activas.
        
        No retorna nada.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_plataformas : list
            lista de las plataformas activas en el nivel
        """
        
        super().update(delta_ms,lista_plataformas)

    def draw (self,screen) -> None:
        """
        Ejecuta el método draw heredado.
        
        No retorna nada.
        
        ----------
        screen
            superficie en la que se renderizan los sprites       
        """
        
        super().draw(screen)
                
    def events(self,delta_ms:int,keys,lista_eventos:list,lista_balas:list) -> None:
        """
        Controla los movimiento y acciones del personaje.
        
        Realiza las distintas acciones (con sus correspondientes animaciones) en 
        base a las teclas presionadas.
        
        No aplica is el personaje se encuentra en el estado "muriendo" o "herido".
        
        No retorna nada.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_eventos : list
            lista de distintos tipos de eventos registrados por Pygame
        keys
            teclas presionadas por el jugador
        lista_balas : list
            lista de las balas activas en el nivel
        """
        
        self.tiempo_transcurrido += delta_ms
        self.is_shooting = Ammo.is_shooting(lista_balas=lista_balas,asset=self.asset)
        
        if not (self.is_dying or self.is_hurt):
            if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
                super().walk(DIRECTION_L)
            if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
                super().walk(DIRECTION_R)
            if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
                super().stay()
            if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
                super().stay()
            if not (keys[pygame.K_d]):
                self.block(False)              
            if(keys[pygame.K_d] and not (keys[pygame.K_s] or keys[pygame.K_a])):
                if((self.tiempo_transcurrido - self.tiempo_last_block) > (self.interval_time_block)):
                    self.block()
                    self.tiempo_last_block = self.tiempo_transcurrido
        
            self.attack(False)
            self.shoot(lista_balas,False)
            
            for event in lista_eventos:
                if (event.type == pygame.KEYDOWN):
                    if(keys[pygame.K_SPACE] or keys[pygame.K_LEFT] and keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]):
                        if((self.tiempo_transcurrido - self.tiempo_last_jump) > (self.interval_time_jump)):
                            super().jump(True)
                            self.tiempo_last_jump = self.tiempo_transcurrido
                            
                    if(keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d] and self.is_shooting == False):
                        if((self.tiempo_transcurrido - self.tiempo_last_shoot) > (self.interval_time_shoot)):
                            self.shoot(lista_balas)
                            self.tiempo_last_shoot = self.tiempo_transcurrido

                    if(keys[pygame.K_a] and not (keys[pygame.K_s] or keys[pygame.K_d])):
                        if((self.tiempo_transcurrido - self.tiempo_last_attack) > (self.interval_time_attack)):
                            self.attack()
                            self.tiempo_last_attack = self.tiempo_transcurrido