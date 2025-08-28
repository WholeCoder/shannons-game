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
    def level_complete(self):
        return self._level_complete
    
    @level_complete.setter
    def level_complete(self, val):
        self._level_complete = val

    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self, val):
        self._points = val

    @property
    def highscore(self):
        return self._highscore

    @highscore.setter
    def highscore(self, value):
        self._highscore = value

    @property
    def mins_played(self):
        return self._mins_played
    
    @mins_played.setter
    def mins_played(self, val):
        self._mins_played = val

    @property
    def is_shannon_dead(self):
        return self._is_shannon_dead
    
    @is_shannon_dead.setter
    def is_shannon_dead(self, val):
        self._is_shannon_dead = val

    @property
    def power_event_trigger_time(self):
        return self._power_event_trigger_time

    @power_event_trigger_time.setter
    def power_event_trigger_time(self, val):
        self._power_event_trigger_time = val

    @property
    def power_up_event(self):
        return self._power_up_event

    @power_up_event.setter
    def power_up_event(self, val):
        self._power_up_event = val

    @property
    def shanon_direction(self):
        return self._shanon_direction

    @shanon_direction.setter
    def shanon_direction(self, val):
        self._shanon_direction = val

    @property
    def custom_event(self):
        return self._custom_event

    @custom_event.setter
    def custom_event(self, val):
        self._custom_event = val

    @property
    def mode_change_events(self):
        if self.__current_mode_index >= len(self._mode_change_events):
            curr_event = self._mode_change_events[-1]
        else:
            curr_event = self._mode_change_events[self.__current_mode_index]
            self.__current_mode_index += 1
        return curr_event
    
    @mode_change_events.setter
    def mode_change_events(self, val):
        self._mode_change_events = val

    @property
    def is_shannon_powered(self):
        return self.__is_shannon_powered
    
    @is_shannon_powered.setter
    def is_shannon_powered(self, val):
        self.__is_shannon_powered = val

    @property
    def is_loaded(self):
        return self.__is_loaded
    
    @property
    def shannon_rect(self):
        return self.__shannon_rect

    @shannon_rect.setter
    def shannon_rect(self, value):
        self.__shannon_rect = value

    @property
    def current_time(self):
        return self.__current_time

    @current_time.setter
    def current_time(self, value):
        self.__current_time = value

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    @property
    def fps(self):
        return self.__fps
    
    @fps.setter
    def fps(self, value):
        self.__fps = value

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, value):
        self.__running = value
