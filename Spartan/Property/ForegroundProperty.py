from .Foreground import ForegroundColor24bit
from Spartan.Common import Event


class ForegroundProperty(object):
    def __init__(self):
        self.__foreground = ForegroundColor24bit()
        self.__foreground.onChange += self.baseChange
        self.__foreground.beforeOnChange += self.beforeBaseChange
        self.onForegroundChange = Event()
        self.beforeOnForegroundChange = Event()

    def baseChange(self, sender, last, new):
        self.onForegroundChange(sender, last, new)

    def beforeBaseChange(self, sender, last, new):
        self.beforeOnForegroundChange(sender, last, new)

    @property
    def Foreground(self):
        return self.__foreground

    @Foreground.setter
    def Foreground(self, value):
        if self.__foreground != value:
            # noinspection PyTypeChecker
            self.beforeOnForegroundChange(self, self.__foreground, value)
            t = self.__foreground
            self.__foreground = value
            self.__foreground.onChange = self.baseChange
            self.__foreground.beforeOnChange = self.beforeBaseChange
            # noinspection PyTypeChecker
            self.onForegroundChange(self, t, value)
