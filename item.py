import pygame
from constants import *
from auxiliar import Auxiliar

class Item:
    """Objetos recoletados por el jugador para obtener beneficios."""
    
    def __init__ (self,path:str,x:int,y:int,w:int,h:int,sounds,p_scale:float=1,used:bool=False) -> None:
        """
        Crea el objeto en base a la carpeta de imagenes indicada.
        
        También genera un rectángulo con las mismas dimensiones que el sprite.
        
        No retorna nada.
        
        ----------
        path : str
            ubicación de las imagenes del tipo de objeto
        x : int
            coordenada X en la que se genera el objeto en el nivel
        y : int
            coordenada Y en la que se genera el objeto en el nivel
        w : int
            ancho del sprite
        h : int
            alto del sprite
        sounds
            objeto controlador de sonidos
        p_scale : float
            escala del sprite. Por defecto, 1
        used : bool
            indica si el objeto fue obtenido por el jugador o no
        """
        
        self.p_scale = p_scale * GLOBAL_SCALE
        
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles(PATH_RECURSOS + path + "_{:03d}.png",1,step=0,flip=False,scale=self.p_scale,w=w,h=h)
        self.image = self.image_list[0]
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.rect_collition = pygame.Rect(self.rect)
        
        self.used = used
        
        self.sounds = sounds
                    
    def update (self,lista_personajes:list) -> None:
        """
        No cumple ninguna función en el objeto base.
        Ejecuta el método especial de un objeto.
        
        No retorna nada.
        
        ----------
        lista_personajes : list
            lista de los jugadores activos en el nivel
        """
        pass
    
    def draw (self,screen) -> None:
        """
        Renderiza el sprite del objeto.
        
        No retorna nada.
        
        ----------
        screen
            superficie en la que se renderizan los sprites
        
        ----------
        DEBUG: Renderiza el rectángulo de colisión.
        """
              
        if(DEBUG):
            pygame.draw.rect(screen,ORANGE,self.rect_collition)
            
        screen.blit(self.image,self.rect)
        
class Health_Potion (Item):
    """Objeto de curación."""
    
    def __init__ (self,asset:dict,name:str,x:int,y:int,sounds,p_scale:float=1.5,used:bool=False) -> None:
        """
        Extrae información del diccionario para generar un objeto (base en clase Item).
        
        También obtiene el valor de curación del objeto.
        
        No retorna nada.
        
        ----------
        asset : dict
            diccionario con toda la información del objeto
        name : str
            tipo de objeto
        x : int
            coordenada X inicial del objeto
        y : int
            coordenada Y inicial del objeto
        sounds
            objeto controlador de sonidos
        p_scale : float
            escala del sprite. Por defecto, 1.5
        used : bool
            indica si el objeto fue obtenido por el jugador o no
        """
        
        self.asset = asset["Healing Item"][name]
        self.path= self.asset["asset_folder"]
        item_dimensions = Auxiliar.splitIntoInt(self.asset["asset_dimensions"],",")
        self.w = item_dimensions[0]
        self.h = item_dimensions[1]
        super().__init__ (path=self.path,x=x,y=y,w=self.w,h=self.h,sounds=sounds,p_scale=p_scale,used=used)
        self.healing_power = self.asset["healing_power"]
        self.healing_sound = self.asset["sound_effect"]
    
    def healing (self,lista_personajes:list) -> None:    
        """
        Comprueba si ocurrió una colisión entre el objeto y un jugador.
        
        Si es el caso, restaura los puntos de vida indicados, 
        reproduce el efecto de sonido apropiado y cambia el estado 
        del objeto a "usado".
        
        En caso de que los puntos de vida restaurados superen la vida máxima del jugador, 
        restaura la vida máxima.
        
        No retorna nada.
        
        ----------
        lista_personajes : list
            lista de los jugadores activos en el nivel
        """
         
        for personaje in lista_personajes:
            if(self.rect_collition.colliderect(personaje.rect_collition)):
                        if ((personaje.hitpoints + self.healing_power) <= personaje.hitpoints_max):
                            personaje.hitpoints += self.healing_power
                        else:
                            personaje.hitpoints = personaje.hitpoints_max
                        self.sounds.sound_effect(self.healing_sound)
                        self.used = True
            break
      
    def update (self,lista_personajes:list) -> None:
        """
        Ejecuta el método de curación.
        
        No retorna nada.
        
        ----------
        lista_personajes : list
            lista de los jugadores activos en el nivel
        """
        
        self.healing(lista_personajes)
    
    def draw (self,screen) -> None:
        """
        Renderiza el sprite del objeto.
        
        No retorna nada.
        
        ----------
        screen
            superficie en la que se renderizan los sprites
        
        ----------
        DEBUG: Renderiza el rectángulo de colisión.
        """
        
        super().draw(screen)
            
class Gem (Item):
    """Objeto moneda."""
    
    def __init__ (self,asset:dict,name:str,x:int,y:int,sounds,p_scale:float=0.8,enemy_drop:bool=False,boss_drop:bool=False,used:bool=False) -> None:
        """
        Extrae información del diccionario para generar un objeto (base en clase Item).
        
        Determina el sprite y el valor de moneda en base a las variables "enemy_drop" y "boss_drop".
        
        No retorna nada.
        
        ----------
        asset : dict
            diccionario con toda la información del objeto
        name : str
            tipo de objeto
        x : int
            coordenada X inicial del objeto
        y : int
            coordenada Y inicial del objeto
        sounds
            objeto controlador de sonidos
        p_scale : float
            escala del sprite. Por defecto, 1
        enemy_drop : bool
            indica si el objeto proviene de un enemigo muerto o se genera por su cuenta
        boss_drop : bool
            indica si el objeto proviene de un enemigo tipo jefe muerto
        used : bool
            indicado si el objeto fue obtenido por el jugador o no
        """
        
        self.asset = asset["Currency"][name]
        if (enemy_drop):
            if (boss_drop):
                self.path= self.asset["asset_folder"][2]
                self.currency_value = self.asset["currency_value"][2]
            else:
                self.path= self.asset["asset_folder"][0]
                self.currency_value = self.asset["currency_value"][0]
        else:
            self.path= self.asset["asset_folder"][1]
            self.currency_value = self.asset["currency_value"][1]
        item_dimensions = Auxiliar.splitIntoInt(self.asset["asset_dimensions"],",")
        self.w = item_dimensions[0]
        self.h = item_dimensions[1]
        super().__init__ (path=self.path,x=x,y=y,w=self.w,h=self.h,sounds=sounds,p_scale=p_scale,used=used)
        self.currency_sound = self.asset["sound_effect"]
    
    def earning (self,lista_personajes:list) -> None:
        """
        Comprueba si ocurrió una colisión entre el objeto y un jugador.
        
        Si es el caso, agrega el valor de moneda a la puntuación del jugador, 
        reproduce el efecto de sonido apropiado y cambia el estado 
        del objeto a "usado".
        
        No retorna nada.
        
        ----------
        lista_personajes : list
            lista de los jugadores activos en el nivel
        """
               
        for personaje in lista_personajes:
            if(self.rect_collition.colliderect(personaje.rect_collition)):
                        personaje.currency += self.currency_value
                        self.sounds.sound_effect(self.currency_sound)
                        self.used = True
            break
      
    def update (self,lista_personajes:list) -> None:
        """
        Ejecuta el método de añadir puntuación.
        
        No retorna nada.
        
        ----------
        lista_personajes : list
            lista de los jugadores activos en el nivel
        """
        
        self.earning (lista_personajes)
    
    def draw (self,screen) -> None:
        """
        Renderiza el sprite del objeto.
        
        No retorna nada.
        
        ----------
        screen
            superficie en la que se renderizan los sprites
        
        ----------
        DEBUG: Renderiza el rectángulo de colisión.
        """
        
        super().draw(screen)