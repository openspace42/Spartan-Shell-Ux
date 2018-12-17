from .BackgroundInterface import BackgroundInterface
from Spartan.Shell import SRG


class BackgroundColor8bit(BackgroundInterface):
    def __init__(self, num):
        BackgroundInterface.__init__(self)
        if num < 0 or num > 255:
            raise Exception("BackgroundColor8bit can support color only between 0 and 255")
        self.__colorNumber = num
        self.RenderEngine = self.color_8bit_render_engine

    def color_8bit_render_engine(self):
        return SRG.Background_8bit(self.__colorNumber)

    @property
    def ColorNumber(self):
        return self.__colorNumber

    @ColorNumber.setter
    def ColorNumber(self, value):
        self.beforeOnChange(self, self.__colorNumber, value)
        t = self.__colorNumber
        self.__colorNumber = value
        self.Render()
        self.onChange(self, t, value)
