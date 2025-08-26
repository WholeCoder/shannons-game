from src.log_handle import get_logger

logger = get_logger(__name__)

class ScreenManager:
    def __init__(self, screen, game_state, all_sprites):
        logger.info("Initializing ScreenManager")
        self.screen = screen
        self._game_state = game_state
        self.all_sprites = all_sprites

    def draw_screen(self):
        pass