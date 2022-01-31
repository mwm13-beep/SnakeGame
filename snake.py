import os.path
import pygame
import game

INITIAL_SNAKE_LENGTH = 1
SNAKE_SPEED = 48


class Snake:
    def __init__(self, curr_game):
        self.game = curr_game
        self.length = INITIAL_SNAKE_LENGTH
        self.sprite_body = pygame.image.load(os.path.join(self.game.sprite_dir, "snakebody.png"))
        self.sprite_head_up = pygame.image.load(os.path.join(self.game.sprite_dir, "snakeheadup.png"))
        self.sprite_head_down = pygame.image.load(os.path.join(self.game.sprite_dir, "snakeheaddown.png"))
        self.sprite_head_left = pygame.image.load(os.path.join(self.game.sprite_dir, "snakeheadleft.png"))
        self.sprite_head_right = pygame.image.load(os.path.join(self.game.sprite_dir, "snakeheadright.png"))
        self.x = [game.SIZE]
        self.y = [game.SIZE]
        self.direction = 'down'
        self.time = 0

    def update(self):
        # starting at the back update each block in the body
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # check to see if the snake's direction needs to change
        self.change_direction()

        # move the snake in the appropriate direction
        if self.direction == 'up':
            self.y[0] -= SNAKE_SPEED
        elif self.direction == 'down':
            self.y[0] += SNAKE_SPEED
        elif self.direction == 'left':
            self.x[0] -= SNAKE_SPEED
        elif self.direction == 'right':
            self.x[0] += SNAKE_SPEED

    def change_direction(self):
        if self.game.actions['up'] and self.direction != 'down':
            self.direction = 'up'
        elif self.game.actions['down'] and self.direction != 'up':
            self.direction = 'down'
        elif self.game.actions['left'] and self.direction != 'right':
            self.direction = 'left'
        elif self.game.actions['right'] and self.direction != 'left':
            self.direction = 'right'
        self.game.reset_keys()

    def render(self, display):
        # render the head
        if self.direction == 'up':
            display.blit(self.sprite_head_up, (self.x[0], self.y[0]))
        elif self.direction == 'down':
            display.blit(self.sprite_head_down, (self.x[0], self.y[0]))
        elif self.direction == 'left':
            display.blit(self.sprite_head_left, (self.x[0], self.y[0]))
        elif self.direction == 'right':
            display.blit(self.sprite_head_right, (self.x[0], self.y[0]))

        # render the body
        for i in range(1, self.length):
            display.blit(self.sprite_body, (self.x[i], self.y[i]))

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
