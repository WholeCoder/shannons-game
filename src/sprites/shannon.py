
from pygame import image, transform
from pygame.sprite import Sprite
from pygame import Surface

from src.configs import SHANNON, SHANNON_SPEED, CELL_SIZE
from src.game.state_management import GameState
from src.utils.coord_utils import get_tiny_matrix, precompute_matrix_coords
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
        self.load_all_frames()
        self.calculate_shannon_coords()
        self.log_image()
        self.calculate_tiny_matrix()
        self.calculate_coord_matrix()
        self.frame_delay = 5

    def load_all_frames(self):
        def frame_helper(direction):
            width, height = SHANNON

    def calculate_shannon_coords(self):
        pass

    def log_image(self):
        self.image = self.frames[self.curr_frame_idx]
        self.rect_x = self.shannon_x_coord
        self.rect_y = self.shannon_y_coord
        self.rect = self.image.get_rect(topleft=(self.shannon_x_coord, self.shannon_y_coord))

    def calculate_tiny_matrix(self):
        self.tiny_matrix = get_tiny_matrix(self.matrix,
                                            CELL_SIZE[0],
                                            SHANNON_SPEED)
        self.subdiv = CELL_SIZE[0] // SHANNON_SPEED
        self.tiny_start_x = self.shannon_pos[0] * self.subdiv
        self.tiny_start_y = self.shannon_pos[1] * self.subdiv
        

    def calculate_coord_matrix(self):
        self.coord_matrix = precompute_matrix_coords(*self.start_pos,
                                                     SHANNON_SPEED,
                                                     len(self.tiny_matrix),
                                                     len(self.tiny_matrix[0]))