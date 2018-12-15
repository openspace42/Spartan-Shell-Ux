from .Background import BackgroundColor24bit
from Spartan.Common import Event


class BackgroundProperty(object):
    def __init__(self):
        self.__background = BackgroundColor24bit()
        self.__background.onChange += self.baseChange
        self.__background.beforeOnChange += self.beforeBaseChange
        self.onBackgroundChange = Event()
        self.beforeOnBackgroundChange = Event()

    def baseChange(self, sender, last, new):
        self.onBackgroundChange(sender, last, new)

    def beforeBaseChange(self, sender, last, new):
        self.beforeOnBackgroundChange(sender, last, new)

    @property
    def Background(self):
        return self.__background

    @Background.setter
    def Background(self, value):
        if self.__background != value:
            # noinspection PyTypeChecker
            self.beforeOnBackgroundChange(self, self.__background, value)
            t = self.__background
            self.__background = value
            self.__background.onChange = self.baseChange
            self.__background.beforeOnChange = self.beforeBaseChange
            # noinspection PyTypeChecker
            self.onBackgroundChange(self, t, value)
