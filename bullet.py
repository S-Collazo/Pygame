import pygame
from constants import *
from auxiliar import Auxiliar

class Bullet:
    def __init__ (self,asset,x,y,move_rate_ms,frame_rate_ms,move=100,direction_inicial=DIRECTION_R,p_scale=1,interval_bullet=FPS*2,distance=ANCHO_VENTANA,type=0):
        self.p_scale = p_scale * GLOBAL_SCALE
        self.asset = asset
        self.asset_name = asset["name"]
        self.bullet_asset = asset["bullet"]
        self.bullet_asset_name = self.bullet_asset["name"]
        
        self.direction = direction_inicial
        
        if(self.direction == DIRECTION_L):
            self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + self.bullet_asset["path"] + "_{:03d}.png",self.bullet_asset["quantity"],flip=False,step=0,scale=self.p_scale,w=100,h=100)
        else:
            self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + self.bullet_asset["path"] + "_{:03d}.png",self.bullet_asset["quantity"],flip=True,step=0,scale=self.p_scale,w=100,h=100)
        
        self.frame = 0
        self.animation = self.image_list
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.attack_power = self.bullet_asset["attack_power"]
        
        self.rect_body_collition = pygame.Rect(self.rect)
        
        self.delta_x = move
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms * FPS
               
        self.distance = distance
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_anim = 0
        self.interval_bullet = interval_bullet
        
        self.is_shoot = True
        self.is_attack = False
        self.collition_enabled = True
    
    def shooting (self,lista_personajes,lista_enemigos,lista_plataformas,lista_trampas,lista_balas):
        self.lista_entidades = lista_personajes + lista_enemigos
        if(self.is_shoot):  
            for entidad in self.lista_entidades:
                if not(self.asset_name == entidad.asset_name or entidad.is_dying):
                    if(self.rect_body_collition.colliderect(entidad.rect_collition)):
                        print("A")
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
    
    def do_movement(self):
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
                
    def do_animation (self,delta_ms):
        self.tiempo_transcurrido_anim += delta_ms
        
        if(self.tiempo_transcurrido_anim >= self.frame_rate_ms):
            self.tiempo_transcurrido_anim = 0
        
            if(self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                 self.frame = 0
                
    def update (self,delta_ms,lista_personajes,lista_enemigos,lista_plataformas,lista_trampas,lista_balas):
        self.shooting (lista_personajes,lista_enemigos,lista_plataformas,lista_trampas,lista_balas)
        self.do_movement()
        self.do_animation(delta_ms)
       
    def draw (self,screen):        
        if(self.is_shoot):
            if(DEBUG):
                if(self.collition_enabled):
                    pygame.draw.rect(screen,PURPLE,self.rect_body_collition)
                
            screen.blit(self.image,self.rect)
           