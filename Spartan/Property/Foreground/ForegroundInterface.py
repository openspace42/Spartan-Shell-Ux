from Spartan.Common import Event


class ForegroundInterface(object):
    def __init__(self):
        self.__renderBuffer = ""
        self.RenderEngine = None
        self.onChange = Event()
        self.beforeOnChange = Event()

    def Render(self):
        if self.RenderEngine is not None:
            self.__renderBuffer = self.RenderEngine()

    @property
    def renderBuffer(self):
        return self.__renderBuffer

