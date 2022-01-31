import os
import pygame
from states import state, main_game

BUTTON_SIZE = (300, 100)


class Title(state.State):
    def __init__(self, game):
        state.State.__init__(self, game)
        pygame.mixer.music.load(os.path.join(self.game.music_dir, "titlebg.mp3"))
        pygame.mixer.music.play(-1)
        self.background = pygame.image.load(os.path.join(self.game.sprite_dir, "background.png"))
        self.game_title = pygame.image.load(os.path.join(self.game.sprite_dir, "title.png"))
        self.instructions = pygame.image.load(os.path.join(self.game.sprite_dir, "titleinstructions.png"))

    def update(self):
        if self.game.actions["start"]:
            pygame.mixer.music.stop()
            new_state = main_game.MainGame(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, surface):
        surface.blit(self.background, (0, 0))
        surface.blit(self.game_title, (self.game.SCREEN_WIDTH * 0.04, self.game.SCREEN_HEIGHT * 0.3))
        surface.blit(self.instructions, (self.game.SCREEN_WIDTH * 0.038, self.game.SCREEN_HEIGHT * 0.65))
