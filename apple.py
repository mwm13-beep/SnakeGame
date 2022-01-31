import os.path
import random
import pygame
import game


class Apple:
    def __init__(self, curr_game):
        self.image = pygame.image.load(os.path.join(curr_game.sprite_dir, "apple.png"))
        self.collect_sound_path = os.path.join(curr_game.music_dir, "eat.mp3")
        self.x = game.SIZE * 3
        self.y = game.SIZE * 3

    def render(self, display):
        display.blit(self.image, (self.x, self.y))

    def update(self):
        self.x = random.randint(0, 19) * game.SIZE
        self.y = random.randint(0, 14) * game.SIZE
        pygame.mixer.Sound.play(pygame.mixer.Sound(self.collect_sound_path))
