from .BackgroundInterface import BackgroundInterface


class BackgroundColor24bit(BackgroundInterface):
    def __init__(self, r=0,g=0,b=0):
        super().__init__()
        if r < 0 or r > 255:
            raise Exception("BackgroundColor24bit can support color only between 0 and 255 for red")
        if g < 0 or g > 255:
            raise Exception("BackgroundColor24bit can support color only between 0 and 255 for green")
        if b < 0 or b > 255:
            raise Exception("BackgroundColor24bit can support color only between 0 and 255 for blu")
        self.__red = r
        self.__green = g
        self.__blu = b
        self.RenderEngine = self.color_24bit_render_engine()

    def color_24bit_render_engine(self):
        return "\033[48;2;"+str(self.__red)+";"+str(self.__green)+";"+str(self.__blu)+"m"

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
    def G(self,value):
        self.beforeOnChange(self, self.__green, value)
        t = self.__green
        self.__green = value
        self.Render()
        self.onChange(self, t, value)

    @property
    def B(self):
        return self.__red

    @B.setter
    def B(self,value):
        self.beforeOnChange(self, self.__blu, value)
        t = self.__blu
        self.__blu = value
        self.Render()
        self.onChange(self, t, value)
