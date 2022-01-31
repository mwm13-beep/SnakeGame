import os
import pygame


class Button:
    def __init__(self, game, image_name, x, y, width, height):
        self.text = pygame.image.load(os.path.join(game.sprite_dir, image_name))
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def is_over(self, pos):
        if self.x <= pos[0] < self.x + self.width and self.y <= pos[1] < self.y + self.height:
            return True
        else:
            return False
