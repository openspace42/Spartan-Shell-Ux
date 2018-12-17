from Spartan.Common import Event
from Spartan.Shell import CSI
from . import HeightProperty, WidthProperty
import sys


class RenderableProperty(object):
    def __init__(self):
        self.__drawn = True
        self.__RenderBuffer = ""
        self.RenderEngine = None
        self.onRendered = Event()
        self.beforeRender = Event()

    def __render(self):
        # noinspection PyTypeChecker
        self.beforeRender()
        self.__RenderBuffer = self.RenderEngine()
        # noinspection PyTypeChecker
        self.onRendered()

    def get_absolute_position(self):
        #if isinstance(self, Screen):
            #return 0, 0
        return 0, 0

    def print_buffer(self, x, y, height, width):
        print_buffer = ""
        rb = self.__RenderBuffer.split("\n")
        i = 0
        while i != len(rb) and i!= height+1 :
            print_buffer += CSI.CUP(x, y+i)
            print_buffer += rb[i]
            i += 1
        return print_buffer

    def render_update(self):
        self.__render()
        self.__drawn = False

    def draw(self):
        if not self.__drawn:
            x, y = self.get_absolute_position()
            height = 0
            width = 0
            if isinstance(self, HeightProperty):
                height = self.ActualHeight
            if isinstance(self, WidthProperty):
                width = self.ActualWidth
            sys.stdout.write(self.print_buffer(x, y, height, width))
            sys.stdout.flush()
            self.__drawn = True
