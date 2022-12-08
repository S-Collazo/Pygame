import pygame
from constants import *
from enemy import Enemy
from ammo import Ammo
from auxiliar import Auxiliar

class Boss(Enemy):
    """Enemigo jefe."""
    
    def __init__(self,asset:dict,name:str,x:int,y:int,gravity:int,frame_rate_ms:int,move_rate_ms:int,difficulty:int,sounds,p_scale:float=1.2) -> None:
        """
        Extrae información del diccionario para generar un personaje (base en clase Entity).
        
        También genera una animación única "ataque especial" con su correspondiente intervalo de tiempo
        y efecto de sonido.
        
        No retorna nada.
        
        ----------
        asset : dict
            diccionario con toda la información del personaje
        name : str
            nombre del personaje
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
        difficulty : int
            dificultad de nivel, modifica ciertos valores
        sounds
            objeto controlador de sonidos
        p_scale : float
            escala del sprite. Por defecto, 1.2
        """
        
        self.asset = asset
        self.difficulty = difficulty
        self.sounds = sounds
        
        super().__init__(self.asset, "Bosses", name, x, y, gravity,frame_rate_ms, move_rate_ms, self.sounds, p_scale)
        
        # Variables de ataque especial:
        self.tiempo_last_attack_special = 0
        self.interval_time_attack_special = self.interval_time * self.asset["interval_attack_special"]
        
        self.direction = DIRECTION_L

        self.attack_special_r = Auxiliar.getSurfaceFromJson(self.asset,"Special Attack",flip=False,p_scale=self.p_scale)
        self.attack_special_l = Auxiliar.getSurfaceFromJson(self.asset,"Special Attack",flip=True,p_scale=self.p_scale)
        self.attack_special_value = self.asset["attack_special_value"][self.difficulty]
        
        self.attack_special_sound = Auxiliar.getSoundFromJson(self.asset,"Special Attack")

    def attack_special (self,lista_enemigos:list,spawner,on_off:bool=False) -> None:
        """
        Si on_off es True, inicia la animación de ataque especial en la dirección actual 
        y reproduce el sonido de ataque especial asignado.
        
        También activa un objeto Spawner especial que genera enemigos en base a un atributo del personaje.
        
        No funciona si on_off es False o el personaje está saltando o cayendo. 
        
        No retorna nada.
        
        ----------
        lista_enemigos : list
            lista de los enemigos activos en el nivel
        spawner
            objeto que genera enemigos en el mapa de forma aleatoria
        on_off : bool
            permite o impide iniciar el bloqueo. Por defecto, False
        """
        
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.attack_special_r and self.animation != self.attack_special_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.attack_r
                else:
                    self.animation = self.attack_l
                    
                self.sounds.sound_effect(self.attack_special_sound)
                    
                spawner.boss_spawn(lista_enemigos,self.attack_special_value)
            
    def drop_loot (self,lista_items:list,item_asset:dict,boss_drop:bool=True) -> None:
        """
        Ejecuta el método drop_loot de la clase Enemy, pasándole la variable especial boss_drop.
        
        No retorna nada.
        
        ----------
        lista_items : list
            lista de los objetos activos en el nivel
        item_asset : dict
            diccionario que contiene la información del objeto
        boss_drop : bool
            modificador de la clase Item
        """
        
        super().drop_loot(lista_items,item_asset,boss_drop)
        
    def update(self,delta_ms:int,lista_plataformas:list,lista_oponente:list,lista_balas:list,lista_items:list,item_asset:dict,lista_enemigos:list,spawner) -> None:
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
        lista_enemigos : list
            lista de los enemigos activos en el nivel
        spawner
            objeto que genera enemigos en el mapa de forma aleatoria
        """
        
        super().update(delta_ms, lista_plataformas, lista_items,item_asset)
        if(self.is_alive):
            self.events(delta_ms,lista_oponente,lista_balas, lista_enemigos, spawner)

    def draw(self, screen):
        """
        Ejecuta el método draw heredado.
        
        No retorna nada.
        
        ----------
        screen
            superficie en la que se renderizan los sprites       
        """

        super().draw(screen)

    def events(self,delta_ms:int,lista_oponente:list,lista_balas:list,lista_enemigos:list,spawner) -> None:
        """
        Controla los movimiento y acciones del personaje.
        
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
        lista_enemigos : list
            lista de los enemigos activos en el nivel
        spawner
            objeto que genera enemigos en el mapa de forma aleatoria
        """
        
        self.tiempo_transcurrido += delta_ms
        
        if not (self.is_dying or self.is_hurt):
            # Comprueba si hay una bala activa disparada por el personaje:
            self.is_shooting = Ammo.is_shooting(lista_balas=lista_balas,asset=self.asset_type)

            for oponente in lista_oponente:
                # Distancias entre personaje y jugador en el eje X e Y:
                self.player_position_x = oponente.rect_body_collition.x
                self.player_position_y = oponente.rect.y
                self.distance_difference_x = self.rect_body_collition.x - oponente.rect_body_collition.x
                self.distance_difference_y = self.rect.y - oponente.rect.y

                # Desactiva animaciones de ataque, disparo y bloqueo (impide repetición infinita):
                self.attack(False)
                self.block(False)
                self.shoot(lista_balas,False)

                if(abs(self.distance_difference_x) <= (ANCHO_VENTANA - 100)):
                    if (abs(self.distance_difference_x) <= 300):
                        # Si la distancia X es inferior a 300, realiza ataque especial o dispara (si está habilitado):
                        if((self.tiempo_transcurrido - self.tiempo_last_attack_special) > (self.interval_time_attack_special)):
                            self.attack_special(lista_enemigos,spawner,True)
                            self.tiempo_last_attack_special = self.tiempo_transcurrido
                        else:
                            if(self.is_shooting == False and ((self.tiempo_transcurrido - self.tiempo_last_shoot) > self.interval_time_shoot)):
                                self.shoot(lista_balas)
                                self.tiempo_last_shoot = self.tiempo_transcurrido
                    
                    elif(abs(self.distance_difference_x) <= 50):
                        # Si la distancia X es inferior a 50, bloquea en caso de que el oponente ataque o realiza ataque normal (si está habilitado):
                        if(oponente.is_attack and (self.tiempo_transcurrido - self.tiempo_last_block) > (self.interval_time_block)):
                            self.block()
                            self.tiempo_last_block = self.tiempo_transcurrido
                        else:
                            if ((self.tiempo_transcurrido - self.tiempo_last_attack) > (self.interval_time_attack)):
                                self.attack()
                                self.tiempo_last_attack = self.tiempo_transcurrido
                                    
                    else:
                        # Si la distancia X es superior a 300, camina hacia el jugador activo:
                        if(self.distance_difference_x >= 0):
                            super().walk(DIRECTION_L)
                        else:
                            super().walk(DIRECTION_R)
            
                    for bala in lista_balas:
                        # Si una bala enemiga está por impactarlo, la bloquea (si está habilitado):
                        if(abs(self.rect.x - bala.rect.x) <= (self.rect.w + 50)):
                            if((self.tiempo_transcurrido - self.tiempo_last_block) > (self.interval_time_block)):
                                self.block()
                                self.tiempo_last_block = self.tiempo_transcurrido