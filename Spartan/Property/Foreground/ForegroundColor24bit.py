from .ForegroundInterface import ForegroundInterface
from Spartan.Shell import SRG

class ForegroundColor24bit(ForegroundInterface):
    def __init__(self, r=255, g=255, b=255):
        ForegroundInterface.__init__(self)
        if r < 0 or r > 255:
            raise Exception("ForegroundColor24bit can support color only between 0 and 255 for red")
        if g < 0 or g > 255:
            raise Exception("ForegroundColor24bit can support color only between 0 and 255 for green")
        if b < 0 or b > 255:
            raise Exception("ForegroundColor24bit can support color only between 0 and 255 for blu")
        self.__red = r
        self.__green = g
        self.__blu = b
        self.RenderEngine = self.color_24bit_render_engine

    def color_24bit_render_engine(self):
        return SRG.Foreground_24bit(self.__red, self.__green, self.__blu)

    @property
    def R(self):
        return self.__red

    @R.setter
    def R(self, value):
        self.beforeOnChange(self, self.__red, value)
        t = self.__red
        self.__red = value
        self.Render()
        self.onChange(self, t, value)

    @property
    def G(self):
        return self.__green

    @G.setter
    def G(self, value):
        self.beforeOnChange(self, self.__green, value)
        t = self.__green
        self.__green = value
        self.Render()
        self.onChange(self, t, value)

    @property
    def B(self):
        return self.__red

    @B.setter
    def B(self, value):
        self.beforeOnChange(self, self.__blu, value)
        t = self.__blu
        self.__blu = value
        self.Render()
        self.onChange(self, t, value)
