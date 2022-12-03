import pygame
import re
from constants import *
from auxiliar import Auxiliar

class Entity:
    def __init__ (self,asset_folder,x,y,gravity,frame_rate_ms,move_rate_ms,direction_inicial=DIRECTION_R,p_scale=1,interval_time_jump=50) -> None:  
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_IDLE\\_IDLE_00{0}.png",1,flip=False,step = 0,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_IDLE\\_IDLE_00{0}.png",1,flip=True,step = 0,scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_JUMP\\_JUMP_00{0}.png",9,flip=False,step = 0,scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_JUMP\\_JUMP_00{0}.png",9,flip=True,step = 0,scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_RUN\\_RUN_00{0}.png",2,flip=False,step = 0,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_RUN\\_RUN_00{0}.png",2,flip=True,step = 0,scale=p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_ATTACK\\_ATTACK_00{0}.png",9,flip=False,step = 0,scale=p_scale,repeat_frame=1)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_ATTACK\\_ATTACK_00{0}.png",9,flip=True,step = 0,scale=p_scale,repeat_frame=1)
        self.knife_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_ATTACK\\_ATTACK_00{0}.png",9,flip=False,step = 0,scale=p_scale,repeat_frame=1)
        self.knife_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + "\\images\\caracters\\" + asset_folder + "\\_ATTACK\\_ATTACK_00{0}.png",9,flip=True,step = 0,scale=p_scale,repeat_frame=1)
        self.frame = 0
                
        self.tiempo_transcurrido = 0
        self.tiempo_transcurrido_anim = 0
        self.tiempo_transcurrido_move = 0
        self.tiempo_last_jump = 0
        self.interval_time_jump = interval_time_jump
        
        self.frame_rate_ms = frame_rate_ms 
        self.move_rate_ms = move_rate_ms
        
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = int((ANCHO_VENTANA / 50) * p_scale)
        self.speed_run = self.speed_walk * 2
        self.gravity = gravity
        self.jump_height = int((ALTO_VENTANA / 0.7) * p_scale)
        self.jump_power = self.jump_height / 4
        self.y_start_jump = y
        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False
        
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.direction = direction_inicial
                
        self.rect_collition = pygame.Rect(x+self.rect.width / 3,y,self.rect.width / 3,self.rect.height)
        self.rect_ground_collition = pygame.Rect(self.rect_collition)
        self.rect_ground_collition.height = GROUND_COLLIDE_H
        self.rect_ground_collition.y = y + self.rect.height - GROUND_COLLIDE_H
                
        self.rect_body_collition = pygame.Rect(x,y,self.rect.width/2,self.rect.height)
        self.rect_body_collition_front = pygame.Rect(self.rect_body_collition)
        self.rect_body_collition_back = pygame.Rect(self.rect_body_collition)
            
    def walk (self,direction_walk):        
        if(self.is_jump == False and self.is_fall == False):
            if self.direction != direction_walk or (self.animation != self.walk_r and self.animation != self.walk_l):
                self.frame = 0
                self.direction = direction_walk
                if (direction_walk == DIRECTION_R):
                    self.animation = self.walk_r
                    self.move_x = self.speed_walk
                else:
                    self.animation = self.walk_l
                    self.move_x = -self.speed_walk
                                            
    def jump (self, on_off = True):
        if (on_off  and self.is_jump == False):
            self.y_start_jump = self.rect.y
            if (self.direction == DIRECTION_R):
                self.animation = self.jump_r
                self.move_y = -self.jump_power
                self.move_x = self.jump_power
            else:
                self.animation = self.jump_l
                self.move_y = -self.jump_power
                self.move_x = -self.jump_power
                
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()
    
    def stay(self):  
        if not self.animation == self.stay_r and not self.animation == self.stay_l:
            if (self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0 
            
    def shoot(self,on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l   
                    
    def knife(self,on_off = True):
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                else:
                    self.animation = self.knife_l
                                                    
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
        if((self.rect.x + delta_x) >= 0 and (self.rect.x + self.rect.w + delta_x) <= ANCHO_VENTANA):
            self.rect.x += delta_x
            self.rect_collition.x += delta_x
            self.rect_ground_collition.x += delta_x
            self.rect_body_collition.x += delta_x
        
        if(self.direction == DIRECTION_R):
            self.rect_body_collition_front.x = self.rect_body_collition.x + (self.rect_body_collition.width)
            self.rect_body_collition_back.x = self.rect_body_collition.x
        else:
            self.rect_body_collition_front.x = self.rect_body_collition.x
            self.rect_body_collition_back.x = self.rect_body_collition.x + (self.rect_body_collition.width)
        
                
    def add_y(self,delta_y):
        self.rect.y += delta_y
        self.rect_collition.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.rect_body_collition_front.y += delta_y
        self.rect_body_collition_back.y += delta_y
        
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
                
    def do_animation (self,delta_ms,frame_rate_ms):
        self.tiempo_transcurrido_anim += delta_ms
        self.frame_rate_ms = frame_rate_ms
        
        if(self.tiempo_transcurrido_anim >= self.frame_rate_ms):
            self.tiempo_transcurrido_anim = 0
        
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                 self.frame = 0
                 
    def damage(self,lista_oponente):
        for oponente in lista_oponente:
            if(self.rect_body_collition_back.colliderect(oponente.rect_body_collition_front) or self.rect_body_collition_front.colliderect(oponente.rect_body_collition_front)):
                if(self.rect_body_collition_back.colliderect(oponente.rect_body_collition_front)):
                    self.lives -= 1
                              
                if(self.entity_type == PLAYER and oponente.lives > 0):
                    if(self.rect_body_collition_front.colliderect(oponente.rect_body_collition_front)):
                        self.lives -= 1
                        
                        if(self.rect.x <= oponente.rect.x):
                            self.add_x(-100)
                        else:
                            self.add_x(100)
                        self.jump(True)
                                    
                break
                                             
    def update(self,delta_ms,lista_plataformas,lista_oponente):
        if(DEBUG):
            if(self.lives > 0):
                    print(self.lives)
                    
        self.do_animation(delta_ms,self.frame_rate_ms)
        self.do_movement(delta_ms,lista_plataformas)
        self.damage(lista_oponente)
    
    def draw (self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,PURPLE,self.rect_body_collition_front)
            pygame.draw.rect(screen,ORANGE,self.rect_body_collition_back)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
    
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

        