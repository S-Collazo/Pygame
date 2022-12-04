import pygame
from constants import *
from enemy import Enemy
from ammo import Ammo
from sounds import Sound
from auxiliar import Auxiliar

class Boss(Enemy):
    def __init__(self, asset, name, x, y, gravity, frame_rate_ms, move_rate_ms,difficulty,p_scale=1.2):
        self.asset = asset
        self.difficulty = difficulty
        super().__init__(self.asset, "Bosses", name, x, y, gravity,frame_rate_ms, move_rate_ms, p_scale)
        
        self.tiempo_last_attack_special = 0
        self.interval_time_attack_special = self.interval_time * self.asset["interval_attack_special"]
        
        self.direction = DIRECTION_L

        self.attack_special_r = Auxiliar.getSurfaceFromJson(self.asset,"Special Attack",flip=False,p_scale=self.p_scale)
        self.attack_special_l = Auxiliar.getSurfaceFromJson(self.asset,"Special Attack",flip=True,p_scale=self.p_scale)
        self.attack_special_value = self.asset["attack_special_value"][self.difficulty]
        
        self.attack_special_sound = Auxiliar.getSoundFromJson(self.asset,"Special Attack")

    def attack_special (self,lista_enemigos,spawner,on_off=False):
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.attack_special_r and self.animation != self.attack_special_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.attack_r
                else:
                    self.animation = self.attack_l
                    
                Sound.sound_effect(self.attack_special_sound)
                    
                spawner.boss_spawn(lista_enemigos,self.attack_special_value)
    
    def death (self):
        super().death()
        
    
    def update(self, delta_ms, lista_plataformas, lista_oponente, lista_balas, lista_items, item_asset, lista_enemigos, spawner):
        super().update(delta_ms, lista_plataformas, lista_items,item_asset)
        self.events(delta_ms,lista_oponente,lista_balas, lista_enemigos, spawner)

    def draw(self, screen):
        super().draw(screen)

    def events(self, delta_ms,lista_oponente,lista_balas,lista_enemigos,spawner):
        self.tiempo_transcurrido += delta_ms
        self.is_shooting = Ammo.is_shooting(lista_balas=lista_balas,asset=self.asset_type)

        for oponente in lista_oponente:
            self.player_position_x = oponente.rect_body_collition.x
            self.player_position_y = oponente.rect.y
            self.distance_difference_x = self.rect_body_collition.x - oponente.rect_body_collition.x
            self.distance_difference_y = self.rect.y - oponente.rect.y

            self.attack(False)
            self.block(False)
            self.shoot(lista_balas,False)

            if(abs(self.distance_difference_x) <= (ANCHO_VENTANA - 100)):
                if (abs(self.distance_difference_x) <= 300):
                    if((self.tiempo_transcurrido - self.tiempo_last_attack_special) > (self.interval_time_attack_special)):
                        self.attack_special(lista_enemigos,spawner,True)
                        self.tiempo_last_attack_special = self.tiempo_transcurrido
                    else:
                        if(self.is_shooting == False and ((self.tiempo_transcurrido - self.tiempo_last_shoot) > self.interval_time_shoot)):
                            self.shoot(lista_balas)
                            self.tiempo_last_shoot = self.tiempo_transcurrido
                
                elif(abs(self.distance_difference_x) <= 50):
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