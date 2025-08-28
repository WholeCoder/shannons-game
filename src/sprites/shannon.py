from pygame.sprite import Sprite
from pygame import Surface

from src.game.state_management import GameState
from src.log_handle import get_logger
logger = get_logger(__name__)

class Shannon(Sprite):
    def __init__(self,
                 screen: Surface,
                 game_state: GameState,
                 matrix: list[list[str]],
                 shannon_pos: tuple,
                 start_pos: tuple):
        super().__init__()
        self.screen = screen
        self.game_state = game_state
        self.shannon_pos = shannon_pos
        self.matrix = matrix
        self.start_pos = start_pos