import os
import pygame
import apple
import snake
import game
from states import state
from states import gameover


class MainGame(state.State):
    def __init__(self, curr_game):
        state.State.__init__(self, curr_game)
        pygame.mixer.music.load(os.path.join(self.game.music_dir, "maingamebg.mp3"))
        pygame.mixer.music.play(-1)
        self.game_over_sound_path = os.path.join(curr_game.music_dir, "lose.mp3")
        self.background = pygame.image.load(os.path.join(self.game.sprite_dir, "background.png"))
        self.snake = snake.Snake(curr_game)
        self.apple = apple.Apple(curr_game)

    def update(self):
        # check to see if the snake collides with the mushroom after movement
        if game.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.apple.update()
            self.snake.increase_length()

        self.snake.update()

        # check to see if the snake has collided with itself
        curr = 3
        game_over = False
        while curr < self.snake.length and not game_over:
            if game.is_collision(self.snake.x[curr], self.snake.y[curr], self.snake.x[0], self.snake.y[0]):
                game_over = True
            curr = curr + 1

        # check to see if the snake has exited with the boundaries
        if self.snake.x[0] < 0 or self.snake.x[0] >= self.game.SCREEN_WIDTH or 0 > self.snake.y[0] or self.snake.y[0] >= self.game.SCREEN_HEIGHT:
            game_over = True

        # in this case we enter the game over state
        if game_over:
            self.game.reset_keys()
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(pygame.mixer.Sound(self.game_over_sound_path))
            new_state = gameover.GameOver(self.game)
            new_state.enter_state()

    def render(self, display):
        display.blit(self.background, (0, 0))
        self.apple.render(display)
        self.snake.render(display)
