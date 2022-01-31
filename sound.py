import pygame


def play_background_music(location):
    pygame.mixer.music.load(location)
    pygame.mixer.music.play()


def play_sound(self, location):
    pygame.mixer.Sound.play(pygame.mixer.Sound(location))
