import pygame
from constants import *
from enemy import Enemy
from ammo import Ammo
                                    
class Goblin_Standard (Enemy):
    """Enemigo estandar"""
    
    def __init__(self,asset:dict,x:int,y:int,gravity:int,frame_rate_ms:int,move_rate_ms:int,sounds,p_scale:float=0.1) -> None:
        """
        Extrae información del diccionario para generar un personaje (base en clase Enemy).
        
        No retorna nada.
        
        ----------
        asset : dict
            diccionario con toda la información del personaje
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
        p_scale : float
            escala del sprite. Por defecto, 0.1
        """
        
        super().__init__(asset, "Goblins", "Goblin Standard", x, y, gravity,frame_rate_ms, move_rate_ms, sounds,p_scale)

    def update(self,delta_ms:int,lista_plataformas:list,lista_oponente:list,lista_balas:list,lista_items:list,item_asset:list) -> None:
        """
        Ejecuta el método update heredado, actualizando los atributos de tiempo pasado, plataformas e items activos 
        y objeto a generar cuando muera el personaje.
        
        También ejecuta el método de control de acciones, a menos que el personaje ya no este vivo.
        
        No retorna nada.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_plataformas : list
            lista de las plataformas activas en el nivel
        lista_oponente : list
            lista de los jugadores activos en el nivel
        lista_balas : list
            lista de las balas activas en el nivel
        lista_items : list
            lista de los objetos activos en el nivel
        item_asset : dict
            diccionario que contiene la información del objeto a generar en caso de muerte
        """
        
        super().update(delta_ms, lista_plataformas, lista_items,item_asset)
        if(self.is_alive):
            self.events(delta_ms,lista_oponente)

    def draw(self,screen) -> None:
        """
        Ejecuta el método draw heredado.
        
        No retorna nada.
        
        ----------
        screen
            superficie en la que se renderizan los sprites       
        """
        
        super().draw(screen)

    def events(self,delta_ms:int,lista_oponente:list) -> None:
        """
        Controla los movimiento y acciones del personaje.
        
        Calcula la distancia entre el personaje y el jugador activo y determina qué acciones tomará 
        en base a esa distancia. En caso de que la distancia sea mayor al número indicado, determina 
        una zona de patrullaje para el personaje.
        
        No aplica is el personaje se encuentra en el estado "muriendo" o "herido".
        
        No retorna nada.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_oponente : list
            lista de los jugadores activos en el nivel
        """
        
        self.tiempo_transcurrido += delta_ms

        if(self.x <= ANCHO_VENTANA / 2):
            self.posicion_extremo_a = 5
            self.posicion_extremo_b = ANCHO_VENTANA / 2
        else:
            self.posicion_extremo_a = ANCHO_VENTANA / 2
            self.posicion_extremo_b = ANCHO_VENTANA - self.rect.w - 5
            
        if not (self.is_dying or self.is_hurt):
            for oponente in lista_oponente:
                self.player_position_x = oponente.rect_body_collition.x
                self.player_position_y = oponente.rect.y
                self.distance_difference_x = self.rect_body_collition.x - oponente.rect_body_collition.x
                self.distance_difference_y = self.rect.y - oponente.rect.y

                self.attack(False)

                if(abs(self.distance_difference_x) <= 500 and abs(self.distance_difference_y) <= 50):
                    if(abs(self.distance_difference_x) <= 100):
                        if ((self.tiempo_transcurrido - self.tiempo_last_attack) > (self.interval_time_attack)):
                            self.attack()
                            self.tiempo_last_attack = self.tiempo_transcurrido
                    else:
                        if(self.distance_difference_x >= 0):
                            super().walk(DIRECTION_L)
                        else:
                            super().walk(DIRECTION_R)
                else:
                    if(self.rect.x >= self.posicion_extremo_a and self.rect.x <= self.posicion_extremo_b):
                        super().walk(self.direction)
                    else:
                        if(self.rect.x < self.posicion_extremo_a):
                            super().walk(DIRECTION_R)
                        if(self.rect.x > self.posicion_extremo_b):
                            super().walk(DIRECTION_L)
                        
class Goblin_Grunt (Enemy):
    """Enemigo con capacidad de bloqueo"""
    
    def __init__(self,asset:dict,x:int,y:int,gravity:int,frame_rate_ms:int,move_rate_ms:int,sounds,p_scale:float=0.1) -> None:
        """
        Extrae información del diccionario para generar un personaje (base en clase Enemy). 
        Activa variable que permite acción de bloqueo.
        
        No retorna nada.
        
        ----------
        asset : dict
            diccionario con toda la información del personaje
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
        p_scale : float
            escala del sprite. Por defecto, 0.1
        """
        
        super().__init__ (asset,"Goblins","Goblin Grunt",x,y,gravity,frame_rate_ms,move_rate_ms,sounds,p_scale)
        self.can_block = True
        
    def update (self,delta_ms:int,lista_plataformas:list,lista_oponente:list,lista_balas:list,lista_items:list,item_asset:list) -> None:
        """
        Ejecuta el método update heredado, actualizando los atributos de tiempo pasado, plataformas e items activos 
        y objeto a generar cuando muera el personaje.
        
        También ejecuta el método de control de acciones, a menos que el personaje ya no este vivo.
        
        No retorna nada.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_plataformas : list
            lista de las plataformas activas en el nivel
        lista_oponente : list
            lista de los jugadores activos en el nivel
        lista_balas : list
            lista de las balas activas en el nivel
        lista_items : list
            lista de los objetos activos en el nivel
        item_asset : dict
            diccionario que contiene la información del objeto a generar en caso de muerte
        """
        
        super().update(delta_ms,lista_plataformas,lista_items,item_asset)
        if(self.is_alive):
            self.events(delta_ms,lista_oponente,lista_balas)
        
    def draw (self,screen) -> None:
        """
        Ejecuta el método draw heredado.
        
        No retorna nada.
        
        ----------
        screen
            superficie en la que se renderizan los sprites       
        """
        
        super().draw(screen)
        
    def events(self,delta_ms:int,lista_oponente:list,lista_balas:list) -> None:
        """
        Controla los movimiento y acciones del personaje.
        
        Calcula la distancia entre el personaje y el jugador activo y determina qué acciones tomará 
        en base a esa distancia. En caso de que la distancia sea mayor al número indicado, determina 
        una zona de patrullaje para el personaje.
        
        No aplica is el personaje se encuentra en el estado "muriendo" o "herido".
        
        No retorna nada.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_oponente : list
            lista de los jugadores activos en el nivel
        lista_balas : list
            lista de las balas activas en el nivel
        """
        
        self.tiempo_transcurrido += delta_ms
  
        if(self.x <= ANCHO_VENTANA / 2):
            self.posicion_extremo_a = 5
            self.posicion_extremo_b = ANCHO_VENTANA / 2
        else:
            self.posicion_extremo_a = ANCHO_VENTANA / 2
            self.posicion_extremo_b = ANCHO_VENTANA - self.rect.w - 5
        
        if not (self.is_dying or self.is_hurt):             
            for oponente in lista_oponente:
                self.player_position_x = oponente.rect_body_collition.x
                self.player_position_y = oponente.rect.y
                self.distance_difference_x = self.rect_body_collition.x - oponente.rect_body_collition.x
                self.distance_difference_y = self.rect.y - oponente.rect.y
                
                self.attack(False)
                self.block(False)
                
                if(abs(self.distance_difference_x) <= 500 and abs(self.distance_difference_y) <= 50):
                    if(abs(self.distance_difference_x) <= 100):
                        if(oponente.is_attack and (self.tiempo_transcurrido - self.tiempo_last_block) > (self.interval_time_block)):
                            self.block()
                            self.tiempo_last_block = self.tiempo_transcurrido
                        else:
                            if ((self.tiempo_transcurrido - self.tiempo_last_attack) > (self.interval_time_attack)):
                                self.attack()
                                self.tiempo_last_attack = self.tiempo_transcurrido
                    else:
                        if(self.distance_difference_x >= 0):
                            super().walk(DIRECTION_L)
                        else:
                            super().walk(DIRECTION_R)
            
                    for bala in lista_balas:
                        if(abs(self.rect.x - bala.rect.x) <= (self.rect.w + 50)):
                            if((self.tiempo_transcurrido - self.tiempo_last_block) > (self.interval_time_block)):
                                self.block()
                                self.tiempo_last_block = self.tiempo_transcurrido
                else:   
                    if(self.rect.x >= self.posicion_extremo_a and self.rect.x <= self.posicion_extremo_b):
                        super().walk(self.direction)
                    else:
                        if(self.rect.x < self.posicion_extremo_a):
                            super().walk(DIRECTION_R)
                        if(self.rect.x > self.posicion_extremo_b):
                            super().walk(DIRECTION_L)
                                    
class Goblin_Shaman (Enemy):
    """Enemigo con capacidad de disparo"""
    
    def __init__(self,asset:dict,x:int,y:int,gravity:int,frame_rate_ms:int,move_rate_ms:int,sounds,p_scale:float=0.1) -> None:
        """
        Extrae información del diccionario para generar un personaje (base en clase Enemy). 
        Activa variable que permite acción de disparo.
        
        No retorna nada.
        
        ----------
        asset : dict
            diccionario con toda la información del personaje
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
        p_scale : float
            escala del sprite. Por defecto, 0.1
        """
        
        super().__init__ (asset,"Goblins","Goblin Shaman",x,y,gravity,frame_rate_ms,move_rate_ms,sounds,p_scale)
        self.can_throw = True
        
    def update (self,delta_ms:int,lista_plataformas:list,lista_oponente:list,lista_balas:list,lista_items:list,item_asset:list) -> None:
        """
        Ejecuta el método update heredado, actualizando los atributos de tiempo pasado, plataformas e items activos 
        y objeto a generar cuando muera el personaje.
        
        También ejecuta el método de control de acciones, a menos que el personaje ya no este vivo.
        
        No retorna nada.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_plataformas : list
            lista de las plataformas activas en el nivel
        lista_oponente : list
            lista de los jugadores activos en el nivel
        lista_balas : list
            lista de las balas activas en el nivel
        lista_items : list
            lista de los objetos activos en el nivel
        item_asset : dict
            diccionario que contiene la información del objeto a generar en caso de muerte
        """
        
        super().update(delta_ms,lista_plataformas,lista_items,item_asset)
        if(self.is_alive):
            self.events(delta_ms,lista_oponente,lista_balas)
        
    def draw (self,screen) -> None:
        """
        Ejecuta el método draw heredado.
        
        No retorna nada.
        
        ----------
        screen
            superficie en la que se renderizan los sprites       
        """
        
        super().draw(screen)
        
    def events(self,delta_ms:int,lista_oponente:list,lista_balas:list) -> None:
        """
        Controla las acciones del personaje. El personaje no se mueve.
        
        Calcula la distancia entre el personaje y el jugador activo y determina qué acciones tomará 
        en base a esa distancia.
        
        No aplica is el personaje se encuentra en el estado "muriendo" o "herido".
        
        No retorna nada.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_oponente : list
            lista de los jugadores activos en el nivel
        lista_balas : list
            lista de las balas activas en el nivel
        """
        
        self.tiempo_transcurrido += delta_ms
        
        self.is_shooting = Ammo.is_shooting(lista_balas=lista_balas,asset=self.asset_type)
        
        if not (self.is_dying or self.is_hurt):                      
            for oponente in lista_oponente:
                self.player_position_x = oponente.rect_body_collition.x
                self.player_position_y = oponente.rect.y
                self.distance_difference_x = self.rect_body_collition.x - oponente.rect_body_collition.x
                self.distance_difference_y = self.rect.y - oponente.rect.y
            
                if(self.distance_difference_x > 0):
                    self.direction = DIRECTION_L
                    self.animation = self.stay_l
                else:
                    self.direction = DIRECTION_R
                    self.animation = self.stay_r
                
                self.shoot(lista_balas,False)
                        
                if(abs(self.distance_difference_x) <= 500 and abs(self.distance_difference_y) <= 100):
                    if(self.is_shooting == False and ((self.tiempo_transcurrido - self.tiempo_last_shoot) > self.interval_time_shoot)):
                        self.shoot(lista_balas)
                        self.tiempo_last_shoot = self.tiempo_transcurrido