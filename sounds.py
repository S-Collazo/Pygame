import pygame
from constants import *

class Sound:
    def a(self):
        self.test_sound = pygame.mixer.Sound(PATH_RECURSOS + "\\sounds\\effects\\heal.mp3")

    def soundtrack (music):
        pygame.mixer.music.load(PATH_RECURSOS + music)
        pygame.mixer.music.play(-1)

    def sound_effect (self):
        pygame.mixer.Sound.play(self.test_sound)
        pygame.mixer.Sound.stop()
        
    def music_pause (pause=True):
        if (pause):
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
