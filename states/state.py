class State:
    def __init__(self, game):
        self.game = game
        self.prev_state = None
        self.clickable = []

    def update(self):
        pass

    def render(self, display):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()
        self.clickable.clear()

    def reset(self):
        pass

    def check_clickable(self, pos):
        in_bounds = False
        count = 0

        while count < len(self.clickable) and not in_bounds:
            in_bounds = self.clickable[count].is_over(pos)

        return in_bounds

