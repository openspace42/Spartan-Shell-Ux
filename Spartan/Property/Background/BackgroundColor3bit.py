from .BackgroundInterface import  BackgroundInterface


class BackgroundColor3bit(BackgroundInterface):
    def __init__(self, num):
        super().__init__()
        if num < 0 or num > 7:
            raise Exception("BackgroundColor3bit can support color only between 0 and 7")
        self.__colorNumber = num
        self.RenderEngine = self.color_3bit_render_engine()

    def color_3bit_render_engine(self):
        return "\033["+str(self.__colorNumber) + "m"

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
