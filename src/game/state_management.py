from src.configs import DOT_POINT

class GameState:
    def __init__(self):
        self.__level = 1
        self.__running = True
        self.__fps = 60
        self.__current_time = None
        self.__shannon_rect = None
        self.__is_loaded = False
        self.__is_shannon_powered = False
        self._mode_change_events = None
        self.__current_mode_index = 0
        self._custom_event = None
        self._shanon_direction = None
        self._power_up_event = None
        self._power_event_trigger_time = None
        self._is_shannon_dead = False
        self._highscore = 0
        self._mins_played = 0
        self._points = -DOT_POINT
        self._level_complete = False

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, value):
        self.__running = value
