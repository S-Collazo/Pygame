import pygame
from constants import *

class Sound:
    def soundtrack (music):
        pygame.mixer.music.load(PATH_RECURSOS + music)
        pygame.mixer.music.play(-1)

    def sound_effect (sound):
        effect = pygame.mixer.Sound(PATH_RECURSOS + sound)
        pygame.mixer.Sound.play(effect)
        
    def music_pause (pause=True):
        if (pause):
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
