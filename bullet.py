import pygame
from constants import *
from auxiliar import Auxiliar

class Bullet:
    """Proyectiles disparados por los personajes del juego."""
    
    def __init__ (self,asset:dict,x:int,y:int,move_rate_ms:int,frame_rate_ms:int,move:int=100,direction_inicial:int=DIRECTION_R,p_scale:int=1,interval_bullet:int=FPS*2,distance:int=ANCHO_VENTANA) -> None:
        """
        Extrae información del diccionario para determinar nombre del personaje que dispara, nombre de la bala, sprite a animar, 
        puntos de ataque y sonido de impacto. Usa los parámetros pasados para determinar distancia y velocidad de movimiento.
        
        También genera un rectángulo de colisión con las mismas dimensiones que el sprite.
        
        No retorna nada.
        
        ----------
        asset : dict
            diccionario con toda la información del personaje que dispara la bala (contiene también la información de la bala)
        x : int
            coordenada X inicial de la bala
        y : int
            coordenada Y inicial de la bala   
        move_rate_ms : int
            velocidad de desplazamiento
        frame_rate_ms : int
            velocidad de las animaciones  
        move : int
            distancia a recorrer por cada frame. Por defecto, 100
        direction_inicial : int
            dirección en la que se dispara la bala. Por defecto, derecha
        p_scale : int
            escala del sprite. Por defecto, 1
        interval_bullet : int
            intervalo de tiempo para actualizar la posición de la bala. Por defecto, el doble de los FPS del nivel
        distance : int
            distancia máxima que puede recorrer la bala antes de desaparecer. Por defecto, el ancho de la ventana
        """
        
        self.p_scale = p_scale * GLOBAL_SCALE
        self.asset = asset
        self.asset_name = asset["name"]
        self.bullet_asset = asset["bullet"]
        self.bullet_asset_name = self.bullet_asset["name"]
        
        # Determina dirección de la bala y animación correspondiente:
        self.direction = direction_inicial
        if(self.direction == DIRECTION_L):
            self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + self.bullet_asset["path"] + "_{:03d}.png",self.bullet_asset["quantity"],flip=False,step=0,scale=self.p_scale,w=100,h=100)
        else:
            self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + self.bullet_asset["path"] + "_{:03d}.png",self.bullet_asset["quantity"],flip=True,step=0,scale=self.p_scale,w=100,h=100)
        
        # Variables de animación y rectángulo del sprite de la bala:
        self.frame = 0
        self.animation = self.image_list
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Puntos de ataque, sonido de impacto y estados de la bala (disparada y atacando):
        self.attack_power = self.bullet_asset["attack_power"]
        self.attack_sound = self.bullet_asset["sound_effect"]
        self.is_shoot = True
        self.is_attack = False
        
        # Estado de colisiones de la bala y rectángulo de colisión:
        self.collition_enabled = True
        self.rect_body_collition = pygame.Rect(self.rect)
        
        # Variavles de animaciones y desplazamiento:
        self.delta_x = move
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms * FPS
               
        self.distance = distance
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_anim = 0
        self.interval_bullet = interval_bullet
            
    def shooting (self,lista_personajes:list,lista_enemigos:list,lista_plataformas:list,lista_trampas:list,lista_balas:list) -> None:
        """
        Controla si la bala colisiona con alguno de los elementos activos del nivel (ignorando la propia bala).
        De ser el caso, la desactiva.
        
        No retorna nada.
        
        ----------
        lista_personajes : list
            lista de los jugadores activos en el nivel
        lista_enemigos : list
            lista de los enemigos activos en el nivel
        lista_plataformas : list
            lista de las plataformas activas en el nivel
        lista_trampas : list
            lista de las trampas activas en el nivel
        lista_balas : list
            lista de las balas activas en el nivel
        """
        
        self.lista_entidades = lista_personajes + lista_enemigos
        
        if(self.is_shoot):  
            for entidad in self.lista_entidades:
                if not(self.asset_name == entidad.asset_name or entidad.is_dying):
                    if(self.rect_body_collition.colliderect(entidad.rect_collition)):
                        self.is_shoot = False
                        break
            
            for plataforma in lista_plataformas:
                if(plataforma.collition_enabled and self.rect_body_collition.colliderect(plataforma.rect_collition)):
                    self.is_shoot = False
                    break                

            for trampa in lista_trampas:
                if(self.rect_body_collition.colliderect(trampa.rect_body_collition)):
                    self.is_shoot = False
                    break   
                
            for bala in lista_balas:
                if not(self.bullet_asset_name == bala.bullet_asset_name):
                    if(self.rect_body_collition.colliderect(bala.rect_body_collition)):
                        self.is_shoot = False
                        break      
    
    def do_movement(self) -> None:
        """
        Ajusta la posición de la bala en el eje X en base a los valores actuales de movimiento.
        
        No funciona si el tiempo pasado desde la última ejecución del método es inferior al valor de velocidad de desplazamiento.
        Si el movimiento de la bala la sacaría de los límites de la pantalla, la desactiva.
        
        No retorna nada.
        """
        
        self.tiempo_transcurrido_move += self.interval_bullet
                
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0         

            if((self.rect.x + self.rect.w + self.delta_x) >= 0 and (self.rect.x + self.rect.w + self.delta_x) <= self.distance):
                if(self.direction == DIRECTION_R):
                    self.rect.x += self.delta_x
                    self.rect_body_collition.x += self.delta_x
                else:
                    self.rect.x -= self.delta_x
                    self.rect_body_collition.x -= self.delta_x             
            else:
                self.is_shoot = False
                
    def do_animation (self,delta_ms:int) -> None:
        """
        Avanza un frame de la animación de la bala hasta llegar al último frame. Si pasa el último frame, vuelve al primero.
        
        No funciona si el tiempo pasado desde la última ejecución del método es inferior al valor de velocidad de animación.
        
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
                 self.frame = 0
                
    def update (self,delta_ms:int,lista_personajes:list,lista_enemigos:list,lista_plataformas:list,lista_trampas:list,lista_balas:list) -> None:
        """
        Ejecuta los métodos de animación, movimiento y control de colisiones, actualizando los atributos 
        de tiempo pasado y elementos activos.
        
        ----------
        delta_ms : int
            valor de tiempo
        lista_personajes : list
            lista de los jugadores activos en el nivel
        lista_enemigos : list
            lista de los enemigos activos en el nivel
        lista_plataformas : list
            lista de las plataformas activas en el nivel
        lista_trampas : list
            lista de las trampas activas en el nivel
        lista_balas : list
            lista de las balas activas en el nivel
        """
        
        self.shooting (lista_personajes,lista_enemigos,lista_plataformas,lista_trampas,lista_balas)
        self.do_movement()
        self.do_animation(delta_ms)
       
    def draw (self,screen): 
        """
        Renderiza la bala en la pantalla.
        
        ----------
        screen
            superficie en la que se renderizan los sprites
        
        ----------
        DEBUG: Renderiza el rectángulo de colisión.
        """
        
        if(self.is_shoot):
            if(DEBUG):
                if(self.collition_enabled):
                    pygame.draw.rect(screen,PURPLE,self.rect_body_collition)
                
            screen.blit(self.image,self.rect)
           
