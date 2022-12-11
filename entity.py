import pygame
from constants import *
from auxiliar import Auxiliar
from ammo import Ammo

class Entity:
    """Base de todos los personajes (jugadores y enemigos) del juego."""
    
    def __init__ (self,asset:dict,x:int,y:int,gravity:int,frame_rate_ms:int,move_rate_ms:int,sounds,direction_inicial:int=DIRECTION_R,p_scale:float=1,interval_time:int=FPS) -> None:
        """
        Extrae información del diccionario para determinar nombre del personaje, las distintas animaciones que podrá realizar,
        puntos de vida y daño, intervalo de espera para ciertas acciones, capacidad de movimiento y sonidos.
        
        También genera un rectángulo con las mismas dimensiones que el sprite y dentro de este tres rectángulos menores:
        rect_collition para las colisiones que causan daño al personaje, ground_collition para las colisiones con el suelo/plataformas
        y body_collition para la acciones de atacar a otros personajes y bloquear sus ataques.
        
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
        direction_inicial : int
            dirección del personaje al inicio del nivel. Por defecto, derecha
        p_scale : float
            escala del sprite. Por defecto, 1
        intervale_time : int
            tiempo base para los tiempos de espera de ciertas acciones. Por defecto, los FPS del juego
        """
        
        self.p_scale = p_scale * GLOBAL_SCALE
        self.asset = asset
        self.asset_name = asset["name"]
        
        self.attack_r = Auxiliar.getSurfaceFromJson(self.asset,"Attack",flip=False,p_scale=self.p_scale)
        self.attack_l = Auxiliar.getSurfaceFromJson(self.asset,"Attack",flip=True,p_scale=self.p_scale)
        self.block_r = Auxiliar.getSurfaceFromJson(self.asset,"Block",flip=False,p_scale=self.p_scale)
        self.block_l = Auxiliar.getSurfaceFromJson(self.asset,"Block",flip=True,p_scale=self.p_scale)
        self.death_r = Auxiliar.getSurfaceFromJson(self.asset,"Die",flip=False,p_scale=self.p_scale)
        self.death_l = Auxiliar.getSurfaceFromJson(self.asset,"Die",flip=True,p_scale=self.p_scale)
        self.hurt_r = Auxiliar.getSurfaceFromJson(self.asset,"Hurt",flip=False,p_scale=self.p_scale)
        self.hurt_l = Auxiliar.getSurfaceFromJson(self.asset,"Hurt",flip=True,p_scale=self.p_scale)
        self.stay_r = Auxiliar.getSurfaceFromJson(self.asset,"Idle",flip=False,p_scale=self.p_scale)
        self.stay_l = Auxiliar.getSurfaceFromJson(self.asset,"Idle",flip=True,p_scale=self.p_scale)
        self.jump_r = Auxiliar.getSurfaceFromJson(self.asset,"Jump",flip=False,p_scale=self.p_scale)
        self.jump_l = Auxiliar.getSurfaceFromJson(self.asset,"Jump",flip=True,p_scale=self.p_scale)
        self.run_r = Auxiliar.getSurfaceFromJson(self.asset,"Run",flip=False,p_scale=self.p_scale)
        self.run_l = Auxiliar.getSurfaceFromJson(self.asset,"Run",flip=True,p_scale=self.p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromJson(self.asset,"Throw",flip=False,p_scale=self.p_scale)
        self.shoot_l = Auxiliar.getSurfaceFromJson(self.asset,"Throw",flip=True,p_scale=self.p_scale)
        self.walk_r = Auxiliar.getSurfaceFromJson(self.asset,"Walk",flip=False,p_scale=self.p_scale)
        self.walk_l = Auxiliar.getSurfaceFromJson(self.asset,"Walk",flip=True,p_scale=self.p_scale)    
        self.frame = 0
        
        self.hitpoints_max = self.asset["hitpoints"]
        self.hitpoints = self.asset["hitpoints"]
        self.attack_power = self.asset["attack_power"]
        self.is_alive = True
        self.is_hurt = False
        self.is_dying = False

        self.tiempo_transcurrido = 0
        self.tiempo_transcurrido_anim = 0
        self.tiempo_transcurrido_move = 0
        self.interval_time = interval_time
        self.tiempo_last_jump = 0
        self.interval_time_jump = self.interval_time * self.asset["interval_jump"]
        self.tiempo_last_attack = 0
        self.interval_time_attack = self.interval_time * self.asset["interval_attack"]
        self.tiempo_last_shoot = 0
        self.interval_time_shoot = self.interval_time * self.asset["interval_shoot"]
        self.tiempo_last_block = 0
        self.interval_time_block = self.interval_time * self.asset["interval_block"]
        
        self.frame_rate_ms = frame_rate_ms 
        self.move_rate_ms = move_rate_ms
        
        self.direction = direction_inicial
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = int((ANCHO_VENTANA / self.asset["speed_walk_modifier"]))
        self.speed_run = self.speed_walk * 2
        self.gravity = gravity
        self.jump_height = int((ALTO_VENTANA / self.asset["jump_height_modifier"]))
        self.jump_power = self.jump_height / 2
        self.y_start_jump = y
        self.is_jump = False
        self.is_fall = False

        self.is_shoot = False
        self.is_attack = False
        self.is_block = False
        
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.rect_collition = pygame.Rect(x+self.rect.width / 3,y,self.rect.width / 2,self.rect.height)
        self.rect_body_collition = pygame.Rect(x+10,y,self.rect.width/2,self.rect.height)
        
        self.rect_ground_collition = pygame.Rect(self.rect_collition)
        self.rect_ground_collition.height = GROUND_COLLIDE_H
        self.rect_ground_collition.y = y + self.rect.height - GROUND_COLLIDE_H
        
        self.sounds = sounds
        
        self.attack_sound = Auxiliar.getSoundFromJson(self.asset,"Attack")
        self.block_sound = Auxiliar.getSoundFromJson(self.asset,"Block")
        self.death_sound = Auxiliar.getSoundFromJson(self.asset,"Die")
        self.throw_sound = Auxiliar.getSoundFromJson(self.asset,"Throw")
                    
    def walk (self,direction_walk:int) -> None:
        """
        Inicia la animación de caminar (loop) y permite al personaje desplazarse en la dirección indicada.
        
        No aplica si el personaje está saltando o cayendo. 
        
        No retorna nada.
        
        ----------
        direction_walk : int
            dirección en la que se mueve el personaje
        """
              
        if(self.is_jump == False and self.is_fall == False):
            if (self.direction != direction_walk or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction_walk
                if (direction_walk == DIRECTION_R):
                    self.animation = self.walk_r
                    self.move_x = self.speed_walk
                else:
                    self.animation = self.walk_l
                    self.move_x = -self.speed_walk
                                            
    def jump (self, on_off:bool = True) -> None:
        """
        Si on_off es True, inicia la animación de salto y permite al personaje desplazarse en la dirección indicada.
        
        No aplica si on_off es False o el personaje ya está saltando o cayendo. 
        
        No retorna nada.
        
        ----------
        on_off : bool
            permite o impide iniciar el salto. Por defecto, True
        """
        
        if (on_off  and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            self.move_y = -self.jump_height
            if (self.direction == DIRECTION_R):
                self.animation = self.jump_r
                self.move_x = self.jump_power
            else:
                self.animation = self.jump_l
                self.move_x = -self.jump_power
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()
    
    def stay(self) -> None:
        """
        Inicia la animación de personaje ocioso (loop). No permite al personaje moverse.
        
        No retorna nada.
        """
        
        if not (self.animation == self.stay_r and not self.animation == self.stay_l):
            if (self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0 
      
    def attack(self,on_off:bool = True) -> None:
        """
        Si on_off es True, inicia la animación de ataque en la dirección actual y cambia el estado de acción a 'atacar'.
        
        No aplica si on_off es False o el personaje está saltando o cayendo. 
        
        No retorna nada.
        
        ----------
        on_off : bool
            permite o impide iniciar el ataque. Por defecto, True
        """
        
        self.is_attack = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.attack_r and self.animation != self.attack_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.attack_r
                else:
                    self.animation = self.attack_l
            
    def block(self,on_off:bool = True) -> None:
        """
        Si on_off es True, inicia la animación de bloqueo (mantenida) en la dirección actual y cambia el estado de acción a 'bloquear'.
        
        No aplica si on_off es False o el personaje está saltando o cayendo. 
        
        No retorna nada.
        
        ----------
        on_off : bool
            permite o impide iniciar el bloqueo. Por defecto, True
        """
        self.is_block = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.block_r and self.animation != self.block_l):
                if(self.direction == DIRECTION_R):
                    self.animation = self.block_r
                else:
                    self.animation = self.block_l
        else:
            self.frame = 0
            
    def shoot(self,lista_balas:list,on_off:bool = True) -> None:
        """
        Si on_off es True, inicia la animación de disparo en la dirección actual, cambia el estado de acción a 'disparar'
        y reproduce el sonido de disparo asignado.
        
        También crea un objeto Bullet en base a los atributos del personaje.
        
        No aplica si on_off es False o el personaje ya está disparando. 
        
        No retorna nada.
        
        ----------
        lista_balas : lista
            lista de los objetos Bullet activos en el nivel
        on_off : bool
            permite o impide iniciar el bloqueo. Por defecto, True
        """
        
        self.is_shoot = on_off
        if(on_off == True):
            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l
                    
                self.sounds.sound_effect(self.throw_sound)  
                  
            Ammo(asset=self.asset,lista_balas=lista_balas,x=self.rect.x,y=self.rect.y,frame_rate_ms=self.frame_rate_ms,move_rate_ms=self.move_rate_ms,direction=self.direction,p_scale=self.p_scale)
     
    def hurt (self) -> None:
        """
        Inicia la animación de personaje herido en la dirección actual.
        
        No retorna nada.
        """
        
        if(self.is_jump == False and self.is_fall == False):
            if(self.animation != self.hurt_r and self.animation != self.hurt_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.hurt_r
                else:
                    self.animation = self.hurt_l
            
    def death (self) -> None:
        """
        Inicia la animación de muerte en la dirección actual y reproduce el sonido de muerte asignado.
        
        No retorna nada.
        """
        
        if(self.animation != self.death_r and self.animation != self.death_l):
            if (self.direction == DIRECTION_R):
                self.animation = self.death_r
            else:
                self.animation = self.death_l
            self.move_x = 0
            self.move_y = 0
            
            self.sounds.sound_effect(self.death_sound)  
                                                                        
    def is_on_platform(self,lista_plataformas:list) -> bool:
        """
        Comprueba si el personaje se encuentra sobre el suelo o una de las plataformas del nivel.
        
        Si es el caso, retorna True.
        
        Si no es el caso, retorna False.
        
        ----------
        lista_plataformas : list
            lista de las plataformas activas en el nivel
        """
        
        retorno = False
        if(self.rect_ground_collition.bottom >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(plataforma.collition_enabled and self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno
            
    def add_x(self,delta_x:int) -> None:
        """
        Mueve al personaje en el eje X en base al valor recibido. También ajusta la posición de los rectángulos.
        
        No aplica si al desplazarse el personaje saldría de los límites de la pantalla.
        
        No retorna nada.
        
        ----------
        delta_x : int
            distancia de desplazamiento en eje X
        """
               
        if((self.rect_collition.x + delta_x) >= -self.rect_collition.w and (self.rect_collition.x + self.rect_collition.w + delta_x) <= ANCHO_VENTANA):
            self.rect.x += delta_x
            self.rect_collition.x += delta_x
            self.rect_ground_collition.x += delta_x
            self.rect_body_collition.x += delta_x
        
        if(self.direction == DIRECTION_R):
            self.rect_body_collition.x = self.rect.x + 5 + (self.rect_body_collition.width)
        else:
            self.rect_body_collition.x = self.rect.x - 5
                   
    def add_y(self,delta_y:int) -> None:
        """
        Mueve al personaje en el eje Y en base al valor recibido. También ajusta la posición de los rectángulos.

        No retorna nada.
        
        ----------
        delta_y : int
            distancia de desplazamiento en eje Y
        """
        
        self.rect.y += delta_y
        self.rect_collition.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.rect_body_collition.y += delta_y
                                 
    def do_movement(self,delta_ms:int,lista_plataformas:list) -> None:
        """
        Ajusta la posición del personaje en los ejes X e Y en base a los valores actuales de movimiento.
        
        Si el personaje está saltando y el salto lo sacaría de los límites de la pantalla, no hay cambio en el eje Y.
        
        Si el personaje no se encuentra sobre una plataforma o el suelo, activa el estado 'caída' y cambia su posición en el eje Y
        en base a la gravedad del nivel. Una vez que toca el suelo, desactiva el estado 'caída' y, si estaba saltando, la animación de
        salto.
        
        No aplica si el tiempo pasado desde la última ejecución del método es inferior al valor de velocidad de desplazamiento.
        
        No retorna nada.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_plataformas : list
            lista de las plataformas activas en el nivel
        """
        
        self.tiempo_transcurrido_move += delta_ms
        
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
                                  
            if(abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.add_x(self.move_x)
            self.add_y(self.move_y)
            
            if not(self.is_on_platform(lista_plataformas)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.add_y(self.gravity)          
            else:
                if(self.is_jump):
                    self.jump(False)
                self.is_fall = False
                
    def do_animation (self,delta_ms:int) -> None:
        """
        Avanza un frame de la animación actualmente indicada como activa hasta llegar al último frame.
        
        Si es la animación de bloqueo, permanece en el último frame. De otra forma, vuelve al primer frame.
        
        Si es la animación de muerte, desactiva los estados de personaje 'muriendo' y 'vivo'.
        
        Si es la animación de personaje herido, desactiva el estados de personaje 'herido'.
        
        No aplica si el tiempo pasado desde la última ejecución del método es inferior al valor de velocidad de animación.
        
        No retorna nada.
        
        ----------
        delta_ms : int
            valor de tiempo
        """
        
        self.tiempo_transcurrido_anim += delta_ms
        
        if(self.tiempo_transcurrido_anim >= self.frame_rate_ms):
            self.tiempo_transcurrido_anim = 0
           
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                if(self.is_block):
                    self.frame = -1
                else:
                    self.frame = 0
                    if (self.is_dying):
                        self.is_dying = False
                        self.is_alive = False
                    elif (self.is_hurt):
                        self.is_hurt = False
                                                      
    def update(self,delta_ms:int,lista_plataformas:list) -> None:
        """
        Ejecuta los métodos de animación y movimiento, actualizando los atributos de tiempo pasado y plataformas activas.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_plataformas : list
            lista de las plataformas activas en el nivel
        """
        
        self.do_animation(delta_ms)
        self.do_movement(delta_ms,lista_plataformas)
    
    def draw (self,screen) -> None:
        """
        Renderiza y actualiza el sprite del personaje en base a la animación y frames activos.
        
        No retorna nada.
        
        ----------
        screen
            superficie en la que se renderizan los sprites
        
        ----------
        DEBUG: Renderiza rectángulos de daños, colisiones con suelo/plataforma y, si el persona está atacando o bloqueando, ataque/bloqueo.
        """
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect_collition)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
            if(self.is_attack or self.is_block):
                pygame.draw.rect(screen,PURPLE,self.rect_body_collition)

        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

        