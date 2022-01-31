import pygame
from states import state, main_game


class GameOver(state.State):
    def __init__(self, curr_game):
        state.State.__init__(self, curr_game)
        # play the game over screen music here
        # pygame.mixer.music.load(os.path.join(self.game.music_dir, ""))
        # pygame.mixer.music.play()
        self.background = pygame.surface

    def update(self):
        if self.game.actions['start']:
            self.game.state_stack[-2] = main_game.MainGame(self.game)
            self.game.state_stack[-1].exit_state()

    def render(self, display):
        font = pygame.font.SysFont('arial', 30)
        game_over_text = font.render(f"Game over :(", True, (0, 0, 0))
        display.blit(game_over_text, (200, 300))
        instruction_text = font.render("To play again press Enter. To exit press Escape.", True, (0, 0, 0))
        display.blit(instruction_text, (200, 350))
