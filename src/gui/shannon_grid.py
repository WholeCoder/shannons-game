import json

from src.configs import *

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

    def get_json(self, path):
        with open(path) as fp:
            payload = json.load(fp)
        return payload
    
    def load_level(self, level_number):
        level_path = f"levels/level_{level_number}.json"
        level_json = self.get_json(level_path)
        num_rows = level_json["num_rows"]
        num_cols = level_json["num_cols"]
        self._matrix = level_json["matrix"]
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
        