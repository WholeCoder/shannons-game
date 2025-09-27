
from pygame import image, transform
from pygame.sprite import Sprite
from pygame.rect import Rect
from pygame import Surface

from src.configs import SHANNON, SHANNON_FALL_SPEED, SHANNON_SPEED, CELL_SIZE
from src.game.state_management import GameState
from src.utils.coord_utils import get_tiny_matrix, precompute_matrix_coords
from src.sprites.sprite_configs import *
from src.utils.coord_utils import (get_coords_from_idx)
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
        self.sprite_matrix = self.game_state.sprite_matrix
        self.load_all_frames()
        self.calculate_shannon_coords()
        self.load_image()
        # self.calculate_tiny_matrix()
        # self.calculate_coord_matrix()
        self.frame_delay = 5

    def load_all_frames(self):
        def frame_helper(direction):
            width, height = SHANNON
            return [
                transform.scale(image.load(path).convert_alpha(), (width, height))
                for path in SHANNON_PATHS[direction]
            ]
        self.curr_frame_idx = 0
        self.left_frames = frame_helper("left")
        self.right_frames = frame_helper("right")
        self.direction_mapper = {
            "l": self.left_frames,
            "r": self.right_frames
        }
        self.frames = self.right_frames
        self.move_direction = self.game_state.direction

    def calculate_shannon_coords(self):
        x, y = get_coords_from_idx(
            self.shannon_pos,
            self.start_pos[0],
            self.start_pos[1],
            CELL_SIZE[0],
            CELL_SIZE[1],
            len(self.matrix),
            len(self.matrix[0]))
        self.shannon_x_coord = x
        self.shannon_y_coord = y

    def load_image(self):
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
        
    def update(self, dt):
        self.frame_update()
        self.build_bounding_boxes(self.rect_x, self.rect_y)
        self.movement_bind()
        self.move_shannon(dt)
        # self.boundary_check()
        self.frame_direction_update()

    def frame_direction_update(self):
        if self.move_direction != "":
            self.frames = self.direction_mapper[self.move_direction]


    def boundary_check(self):
        if (self.tiny_start_y + self.subdiv * 2) >= len(self.tiny_matrix[0]) - 1:
            self.tiny_start_y = 0
            self.rect_x = self.coord_matrix[self.tiny_start_x][0][0]

        elif (self.tiny_start_y - 1) < 0:
            self.tiny_start_y = len(self.tiny_matrix[0]) - (self.subdiv * 3)
            self.rect_x = self.coord_matrix[self.tiny_start_x][-self.subdiv*2 - 4][0]

    def frame_update(self):
        self.frame_delay -= 1
        if self.frame_delay <= 0:
            self.frame_delay = 5
            self.curr_frame_idx = (self.curr_frame_idx + 1) % len(self.frames)
            self.image = self.frames[self.curr_frame_idx]

    def build_bounding_boxes(self, x: int | float, y: int | float):
        self.rect.x = x + (CELL_SIZE[0] * 2 - self.rect.width) // 2
        self.rect.y = y + (CELL_SIZE[1] * 2 - self.rect.height) // 2

    def movement_bind(self):
        match self.game_state.direction:
            case 'l':
                # if self.edges_helper_vertical(self.tiny_start_x, self.tiny_start_y, -1):
                self.move_direction = "l"
                self.game_state.shannon_direction = 'l'
            
            case 'r':
                # if self.edges_helper_vertical(
                #     self.tiny_start_x, self.tiny_start_y, self.subdiv * 2
                # ):
                self.move_direction = "r"
                self.game_state.shannon_direction = 'r'
            case _:
                self.move_direction = ""
                self.game_state.shannon_direction = ""

    def move_shannon(self, dt: float):

        if not self.touches_wall_below():
            self.rect_y += SHANNON_FALL_SPEED
            self.game_state.shannon_rect = (self.rect_x, self.rect_y, 
                                       CELL_SIZE[0]*2, CELL_SIZE[0]*2)
        match self.move_direction:
            case "l":
                if self.doesnt_run_into_wall("left"): #self.edges_helper_vertical(self.tiny_start_x, self.tiny_start_y, -1):
                    self.rect_x -= SHANNON_SPEED
                    # self.tiny_start_y -= 1
            case "r":
                if self.doesnt_run_into_wall("right"): 
                    #self.edges_helper_vertical(
            #     self.tiny_start_x, self.tiny_start_y, self.subdiv * 2
            # ):
                    self.rect_x += SHANNON_SPEED
                    # self.tiny_start_y += 1
        
        # self.move_direction = self.game_state.direction = ""

        self.game_state.shannon_rect = (self.rect_x, self.rect_y, 
                                       CELL_SIZE[0]*2, CELL_SIZE[0]*2)
        
    
    def touches_wall_below(self):
        for row in self.sprite_matrix:
            for sp in row:
                if sp is not None:
                    next_position = Rect(self.rect)
                    # if sp.rect.colliderect(self.rect):
                    next_position.y += SHANNON_SPEED
                    if sp.rect.colliderect(next_position):
                        return True
        return False

    def doesnt_run_into_wall(self, direction: str):
        for row in self.sprite_matrix:
            for sp in row:
                if sp is not None:
                    # if sp.rect.colliderect(self.rect):
                    shanny_x = self.rect.x
                    if direction == "left" and self.move_direction == "l":
                        shanny_x -= SHANNON_SPEED
                    if direction == "right" and self.move_direction == "r":
                        shanny_x += SHANNON_SPEED

                    next_position = Rect(shanny_x, self.rect.y, self.rect.width, self.rect.height)
                    if sp.rect.colliderect(next_position):
                        return False
        return True


    def edges_helper_vertical(self, row: int, 
                              col: int, 
                              additive: int):
        for r in range(self.subdiv * 2):
            if self.tiny_matrix[row + r][col + additive] == "wall":
                return False
        return True
