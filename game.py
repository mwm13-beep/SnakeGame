import os
import time

import pygame
from pygame.locals import *

from states.title import Title

SIZE = 48
INITIAL_SNAKE_LENGTH = 1


def is_collision(x1, y1, x2, y2):
    if x1 <= x2 < x1 + SIZE and y1 <= y2 < y1 + SIZE:
        return True
    else:
        return False


class Game:
    def __init__(self):
        # set up pygame and pygame music
        pygame.init()
        pygame.mixer.init()

        # variables for gameplay area and game state
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 800
        self.running = True
        self.playing = False
        self.actions = {"left": False, "right": False, "up": False, "down": False, "action1": False, "action2": False, "start": False}
        self.dt = 0
        self.prev_time = 0
        self.state_stack = []

        # setting up the screen
        self.game_canvas = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Feed the Snake!")

        # Paths and variables that will be set by the following method calls
        self.sprite_dir = None
        self.assets_dir = None
        self.music_dir = None
        self.font = None
        self.load_assets()
        self.load_states()

    def game_loop(self):
        while self.running:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()
            time.sleep(0.20)

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def get_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == K_UP:
                    self.actions['up'] = True
                if event.key == K_DOWN:
                    self.actions['down'] = True
                if event.key == K_LEFT:
                    self.actions['left'] = True
                if event.key == K_RIGHT:
                    self.actions['right'] = True
                if event.key == K_RETURN:
                    self.actions['start'] = True

            if event.type == MOUSEBUTTONDOWN:
                if self.state_stack[-1].check_clickable(pygame.mouse.get_pos()):
                    self.actions['start'] = True

    def update(self):
        self.state_stack[-1].update()

    def load_assets(self):
        # Set pointers to our resource directories
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.music_dir = os.path.join(self.assets_dir, "music")
        self.font = pygame.font.SysFont('arial', 30)

    def load_states(self):
        self.state_stack.append(Title(self))

    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        pygame.display.flip()

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        # text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False
