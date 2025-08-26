import sys

import pygame

from src.configs import *
from src.game.event_management import EventHandler
from src.game.state_management import GameState
from src.gui.screen_management import ScreenManager
from src.log_handle import get_logger
logger = get_logger(__name__)

class GameRun:
    def __init__(self):
        logger.info("About to initialize pygame")
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Shannon's Game")
        logger.info("pygame initialized successfully")
        self.game_state = GameState()
        logger.info("game state object created")
        self.events = EventHandler(self.screen, self.game_state)
        logger.info("event handler object created")
        self.all_sprites = pygame.sprite.Group()
        self.gui = ScreenManager(self.screen, self.game_state, self.all_sprites)
        logger.info("screen manager object created")

    def main(self):
        clock = pygame.time.Clock()
        while self.game_state.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.events.pygame_quit()
            self.all_sprites.update()
            self.gui.draw_screen()
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
        sys.exit()