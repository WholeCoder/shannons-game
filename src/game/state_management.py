
class GameState:
    def __init__(self):
        self.__running = True

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, value):
        self.__running = value
