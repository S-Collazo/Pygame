import pygame
from constants import *

class Sounds:
    def __init__ (self,sound_volume=1.0,music_volume=1.0):
        self.sound_volume = sound_volume
        self.music_volume = music_volume
        
    def set_music_volume(self,volume):
        self.music_volume = volume
    
    def soundtrack (self,music):
        pygame.mixer.music.load(PATH_RECURSOS + music)
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1)

    def sound_effect (self,sound):
        effect = pygame.mixer.Sound(PATH_RECURSOS + sound)
        pygame.mixer.Sound.set_volume(effect,self.sound_volume)
        pygame.mixer.Sound.play(effect)
    
    def sound_stop(self):
        pygame.mixer.stop()
        pygame.mixer.music.stop()
        
    def music_pause (pause=True):
        if (pause):
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
