import pygame
from constants import *

class Damage_Control:
    """
    Controlador de daños entre elementos del nivel.
    """
    
    def __init__(self, lista_personajes:list, lista_enemigos:list, lista_balas:list, lista_trampas:list,sounds) -> None:
        """
        Carga las listas de elementos activos y el controlador de sonidos a las variables correspondientes.
        
        No retorna nada.
        
        ----------
        lista_personajes : list
            lista de los jugadores activos en el nivel
        lista_enemigos : list
            lista de los enemigos activos en el nivel
        lista_balas : list
            lista de las balas activas en el nivel
        lista_trampas : list
            lista de las trampas activas en el nivel
        sounds
            objeto controlador de sonidos
        """
        
        self.lista_personajes = lista_personajes
        self.lista_enemigos = lista_enemigos
        self.lista_balas = lista_balas
        self.lista_trampas = lista_trampas

        self.sounds = sounds

    def damage(self, lista_atacante:list, lista_atacado:list) -> None:
        """
        Controla las colisiones entre distintos elementos de dos listas para determinar si uno sufre daños. 
        También reproduce los sonidos de ataque/ bloqueo.
        
        No funciona si el elemento atacado no tiene el estado "vivo" o si el elemento atacante no está realizando la acción "atacar"/"disparar".
        
        No retorna nada.
        
        ----------
        lista_atacante : list
            lista de los elementos que causan el daño
        lista_atacado : list
            lista de los elementos que sufren el daño
            
        ----------
        DEBUG: En caso de daños, hace un print indicando el nombre del atacante y el atacado.
        """
        
        for atacante in lista_atacante:
            for atacado in lista_atacado:
                if (atacado.is_alive):
                    if not (atacado.is_dying or atacado.is_hurt) and (atacante.is_attack or atacante.is_shoot) and not (atacado.asset_name == atacante.asset_name): 
                        if((atacante.rect_body_collition.colliderect(atacado.rect_collition))):
                            # Si el atacado está realizando la acción "bloquear", no sufre daños pero se reproduce el sonido correspondiente:
                            if(atacado.is_block):
                                self.sounds.sound_effect(atacado.block_sound)
                            else:
                                atacado.hitpoints -= atacante.attack_power
                                self.sounds.sound_effect(atacante.attack_sound)
                                
                                if(DEBUG):
                                    print("{0} hit {1}".format(atacante.asset_name,atacado.asset_name))
                                
                                # Desplaza al atacado lejos del atacante:
                                if(atacante.rect.x <= atacado.rect.x):
                                    atacado.add_x(25)
                                else:
                                    atacado.add_x(-25)    
                                
                                # Si el ataque agotaría los puntos de vida del atacado, se activa la animación y estado de muerte.
                                # Si no, los de herida:
                                if(atacado.hitpoints - atacante.attack_power <= 0):
                                    atacado.is_dying = True
                                    atacado.death()
                                else:
                                    atacado.is_hurt = True
                                    atacado.hurt()
                            
    def update(self) -> None:
        """
        Actualiza las listas de elementos activos en el nivel y ejecuta el método de control de daños entre cada una de ellas.
        """
        
        self.lista_entidades = self.lista_personajes + self.lista_enemigos
        self.damage(self.lista_personajes, self.lista_enemigos)
        self.damage(self.lista_enemigos, self.lista_personajes)
        self.damage(self.lista_trampas, self.lista_entidades)
        self.damage(self.lista_balas, self.lista_entidades)
