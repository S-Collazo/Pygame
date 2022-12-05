import pygame
from constants import *
from auxiliar import Auxiliar
from ammo import Ammo
from sounds import Sounds

class Entity:
    def __init__ (self,asset,x,y,gravity,frame_rate_ms,move_rate_ms,sounds,direction_inicial=DIRECTION_R,p_scale=1,interval_time=FPS) -> None:  
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
            
        self.direction = direction_inicial
                        
        self.rect_collition = pygame.Rect(x+self.rect.width / 3,y,self.rect.width / 2,self.rect.height)
        self.rect_ground_collition = pygame.Rect(self.rect_collition)
        self.rect_ground_collition.height = GROUND_COLLIDE_H
        self.rect_ground_collition.y = y + self.rect.height - GROUND_COLLIDE_H
                
        self.rect_body_collition = pygame.Rect(x+10,y,self.rect.width/2,self.rect.height)
        
        self.sounds = sounds
        
        self.attack_sound = Auxiliar.getSoundFromJson(self.asset,"Attack")
        self.block_sound = Auxiliar.getSoundFromJson(self.asset,"Block")
        self.death_sound = Auxiliar.getSoundFromJson(self.asset,"Die")
        self.throw_sound = Auxiliar.getSoundFromJson(self.asset,"Throw")
                    
    def walk (self,direction_walk):        
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
                                            
    def jump (self, on_off = True):
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
    
    def stay(self):  
        if not (self.animation == self.stay_r and not self.animation == self.stay_l):
            if (self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0 
      
    def attack(self,on_off = True):
        self.is_attack = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.attack_r and self.animation != self.attack_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.attack_r
                else:
                    self.animation = self.attack_l
            
    def block(self,on_off = True):
        self.is_block = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.block_r and self.animation != self.block_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.block_r
                else:
                    self.animation = self.block_l
            
    def shoot(self,lista_balas,on_off = True):
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
     
    def hurt (self):
        if(self.is_jump == False and self.is_fall == False):
            if(self.animation != self.hurt_r and self.animation != self.hurt_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.hurt_r
                else:
                    self.animation = self.hurt_l
            
    def death (self):
        if(self.animation != self.death_r and self.animation != self.death_l):
            if (self.direction == DIRECTION_R):
                self.animation = self.death_r
            else:
                self.animation = self.death_l
            self.move_x = 0
            self.move_y = 0
            
            self.sounds.sound_effect(self.death_sound)  
                                                                        
    def is_on_platform(self,lista_plataformas):
        retorno = False
        if(self.rect_ground_collition.bottom >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(plataforma.collition_enabled and self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno
            
    def add_x(self,delta_x):        
        if((self.rect_collition.x + delta_x) >= -self.rect_collition.w and (self.rect_collition.x + self.rect_collition.w + delta_x) <= ANCHO_VENTANA):
            self.rect.x += delta_x
            self.rect_collition.x += delta_x
            self.rect_ground_collition.x += delta_x
            self.rect_body_collition.x += delta_x
        
        if(self.direction == DIRECTION_R):
            self.rect_body_collition.x = self.rect.x + 5 + (self.rect_body_collition.width)
        else:
            self.rect_body_collition.x = self.rect.x - 5
                   
    def add_y(self,delta_y):
        self.rect.y += delta_y
        self.rect_collition.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.rect_body_collition.y += delta_y
                                 
    def do_movement(self,delta_ms,lista_plataformas):
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
                
    def do_animation (self,delta_ms):
        self.tiempo_transcurrido_anim += delta_ms
        
        if(self.tiempo_transcurrido_anim >= self.frame_rate_ms):
            self.tiempo_transcurrido_anim = 0
            
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                if (self.is_dying):
                    self.is_dying = False
                    self.is_alive = False
                else:
                    self.frame = 0
                    if (self.is_hurt):
                        self.is_hurt = False
                                                      
    def update(self,delta_ms,lista_plataformas):
            self.do_animation(delta_ms)
            self.do_movement(delta_ms,lista_plataformas)
    
    def draw (self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect_collition)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
            if(self.is_attack or self.is_block):
                pygame.draw.rect(screen,PURPLE,self.rect_body_collition)

        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

        