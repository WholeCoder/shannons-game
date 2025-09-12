from src.gui.shannon_grid import Block, ShannonGrid

from src.log_handle import get_logger

logger = get_logger(__name__)

class  ScreenManager:
    def __init__(self, screen, game_state, all_sprites):
        logger.info("Initializing ScreenManager")
        self.screen = screen
        self._game_state = game_state
        self.all_sprites = all_sprites
        self.shannon = ShannonGrid(screen, game_state)
        logger.info("shannon grid created")
        self.all_sprites.add(self.shannon.shannon)
        for row in self.shannon.sprite_matrix:
            for block_sprite in row:
                if block_sprite is not None:
                    self.all_sprites.add(block_sprite)
        logger.info("all sprites added to group")

    def draw_screens(self):
        pass#self.shannon.draw_level()