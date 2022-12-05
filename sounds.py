import pygame
from constants import *

class Sounds:
    def __init__ (self,sound_volume=1.0,music_volume=0.25):
        self.sound_volume = sound_volume
        self.sound_volume_standard = sound_volume
        self.music_volume = music_volume

    def set_sound_volume(self,volume):
        self.sound_volume = volume
        if (self.sound_volume > 0):
            self.sound_volume_standard = self.sound_volume
        if(DEBUG):
            if(self.sound_volume > 0):
                print("Sound: {0}".format(self.sound_volume))
        
    def set_music_volume(self,volume):
        self.music_volume = volume
        if(DEBUG):
            print("Music: {0}".format(self.music_volume))
        
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
        
    def music_pause (self,pause=True):
        if (pause):
            pygame.mixer.pause()
            pygame.mixer.music.pause()
            self.set_sound_volume(0)
        else:
            pygame.mixer.unpause()
            pygame.mixer.music.unpause()
            self.set_sound_volume(self.sound_volume_standard)
