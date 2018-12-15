from .ForegroundInterface import  ForegroundInterface


class ForegroundColor8bit(ForegroundInterface):
    def __init__(self, num):
        super().__init__()
        if num < 0 or num > 255:
            raise Exception("ForegroundColor8bit can support color only between 0 and 255")
        self.__colorNumber = num
        self.RenderEngine = self.color_8bit_render_engine()

    def color_8bit_render_engine(self):
        return "\033[48;5;"+str(self.__colorNumber) + "m"

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
