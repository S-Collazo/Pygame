import pygame
from constants import *

class Sounds:
    """Controlador de música y efectos de sonido."""
    
    def __init__ (self,sound_volume:float=1.0,music_volume:float=0.25) -> None:
        """
        Asigna los valores recibidos a las variables de volúmen de música y 
        volúmen de efectos de sonido. También establece el volúmen de efectos de
        sonido por defecto (en caso de que sea necesario desilenciarlos).
        
        No retorna nada. 
              
        ----------
        sound_volume : float
            volúmen de los efectos de sonidos
        music_volume : float
            volúmen de música
        """
        
        self.sound_volume = sound_volume
        self.sound_volume_standard = sound_volume
        self.music_volume = music_volume

    def set_sound_volume(self,volume:float) -> None:
        """
        Asigna el valor recibido al volúmen de efectos de sonido.
        
        Si el valor es mayor a 0, lo establece como el volúmen a usar 
        en caso de restaurar los sonidos.
        
        No retorna nada. 
              
        ----------
        volume : float
            volúmen de los efectos de sonidos
            
        ----------
        DEBUG: Imprime el volúmen de sonido asignado.
        """
        
        self.sound_volume = volume
        if (self.sound_volume > 0):
            self.sound_volume_standard = self.sound_volume
        if(DEBUG):
            if(self.sound_volume > 0):
                print("Sound: {0}".format(self.sound_volume))
        
    def set_music_volume(self,volume:float) -> None:
        """
        Asigna el valor recibido al volúmen de música.
        
        No retorna nada. 
              
        ----------
        volume : float
            volúmen de música
            
        ----------
        DEBUG: Imprime el volúmen de música.
        """
        
        self.music_volume = volume
        if(DEBUG):
            print("Music: {0}".format(self.music_volume))
        
    def soundtrack (self,music:str) -> None:
        """
        Reproduce al dirección de archivo recibida como música de nivel.
        
        Se reproduce de forma indefinida.
        
        No retorna nada.
              
        ----------
        music : str
            ubicación del archivo de música
            
        ----------
        DEBUG: Imprime el volúmen de música.
        """
        
        pygame.mixer.music.load(PATH_RECURSOS + music)
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1)

    def sound_effect (self,sound:str) -> None:
        """
        Reproduce al dirección de archivo recibida como efecto de sonido.
        
        Se reproduce una vez,
        
        No retorna nada.
              
        ----------
        sound : str
            ubicación del archivo de efecto de sonido
        """
        
        effect = pygame.mixer.Sound(PATH_RECURSOS + sound)
        pygame.mixer.Sound.set_volume(effect,self.sound_volume)
        pygame.mixer.Sound.play(effect)
    
    def sound_stop(self) -> None:
        """
        Detiene la reproducción de todos los efectos de sonido y música.

        No retorna nada.
        """
        
        pygame.mixer.stop()
        pygame.mixer.music.stop()
        
    def music_pause (self,pause:bool=True) -> None:
        """
        Si pause es True, pausa la reproducción de efectos de sonida y 
        música en el nivel. También silencia cualquier efecto de sonido 
        nuevo.
        
        Si es pause es False, despause la reproducción de efectos de sonida y 
        música en el nivel. También restora el volúmen de los efectos de sonido 
        al valor guardado como volúmen por defecto.
        
        ----------
        pause : bool
            indica si los efectos de sonido y la música deben pausarse o despausarse
        """
        
        if (pause):
            pygame.mixer.pause()
            pygame.mixer.music.pause()
            self.set_sound_volume(0)
        else:
            pygame.mixer.unpause()
            pygame.mixer.music.unpause()
            self.set_sound_volume(self.sound_volume_standard)
