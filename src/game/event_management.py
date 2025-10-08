from pygame import (K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, KEYUP,
                    QUIT, K_q)
from pygame import USEREVENT
from pygame.time import set_timer

class EventHandler:
    def __init__(self, screen, game_state):
        self._screen = screen
        self._game_screen = game_state

    def pygame_quit(self):
        self._game_screen.running = False

    def key_bindings_down(self, key):
        if key == K_LEFT:
            self._game_screen.direction = "l"
        elif key == K_RIGHT:
            self._game_screen.direction = "r"
        elif key == K_SPACE:
            if not self._game_screen.shannon_is_jump_direction == "not jumping":
                self._game_screen.shannon_is_jump_direction = "start jumping"
                self._game_screen.jump_step = 0

    def key_bindings_up(self, key):
        if key == K_LEFT:
            self._game_screen.direction = ""
        elif key == K_RIGHT:
            self._game_screen.direction = ""
        elif key == K_SPACE:
            self._game_screen.direction = ""

    def handle_events(self, event):
        if event.type == QUIT:
            self.pygame_quit()

        if event.type == KEYDOWN:
            self.key_bindings_down(event.key)

        if event.type == KEYUP:
            self.key_bindings_up(event.key)
        
