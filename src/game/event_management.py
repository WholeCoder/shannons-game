

class EventHandler:
    def __init__(self, screen, game_state):
        self.screen = screen
        self._game_screen = game_state

    def pygame_quit(self):
        self._game_screen.running = False