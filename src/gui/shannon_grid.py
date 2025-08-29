import json

from src.configs import *
from src.sprites.shannon import Shannon
from src.utils.coord_utils import (place_elements_offset,)
from src.utils.draw_utils import (draw_circle, draw_debug_rects, draw_rect)

from src.log_handle import get_logger
logger = get_logger(__name__)

class ShannonGrid:
    def __init__(self, screen, game_state):
        logger.info("Initializing ShannonGrid")
        self.function_mapper = {
            "void": self.draw_void,
            "wall": self.draw_wall,
            "power": self.draw_power,
            "null": self.draw_void,
        }
        self._screen = screen
        self._game_state = game_state
        self._level_number = self._game_state.level
        self.load_level(self._level_number)
        logger.info("level loaded")
        self.shannon = Shannon(
            self._screen,
            self._game_state,
            self._matrix,
            self._shannon_pos,
            (self.start_x, self.start_y)
        )
        logger.info("shannon created")

    def get_json(self, path):
        with open(path) as fp:
            payload = json.load(fp)
        return payload
    
    def load_level(self, level_number):
        level_path = f"levels/level{level_number}.json"
        level_json = self.get_json(level_path)
        num_rows = level_json["num_rows"]
        num_cols = level_json["num_cols"]
        self._matrix = level_json["matrix"]
        self._shannon_pos = level_json["shannon_start"]
        self.start_x, self.start_y = place_elements_offset(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            CELL_SIZE[0] * num_cols,
            CELL_SIZE[0] * num_rows,
            0.5,
            0.5,
        )
        self._num_rows = num_rows
        self._num_cols = num_cols

    def draw_void(self, row, col): ...

    def draw_wall(self, **kwargs):
        draw_rect(
            kwargs["x"],
            kwargs["y"],
            kwargs["w"],
            kwargs["h"],
            self._screen,
            Colors.WALL_BLUE
        )

    def draw_power(self, **kwargs):
        circle_x = kwargs["x"] + kwargs["w"]
        circle_y = kwargs["y"] + kwargs["h"]
        draw_circle(circle_x, circle_y, 7, self._screen, Colors.YELLOW)
        