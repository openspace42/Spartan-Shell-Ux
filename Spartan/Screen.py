from Spartan.Property import *
from Spartan.Shell.Demons import *
from Spartan.Shell import CSI
import time
import sys


class Screen(HeightProperty, WidthProperty,
             VerticalAlignProperty, HorizontalAlignProperty,
             BackgroundProperty, ForegroundProperty,
             MarginProperty, RenderableProperty):
    # noinspection PyCallByClass
    def __init__(self):
        HeightProperty.__init__(self)
        WidthProperty.__init__(self)
        VerticalAlignProperty.__init__(self)
        HorizontalAlignProperty.__init__(self)
        BackgroundProperty.__init__(self)
        ForegroundProperty.__init__(self)
        RenderableProperty.__init__(self)
        MarginProperty.__init__(self, 0, 0, 0, 0)

        self.Height=0
        self.Width=0

        self.__FPSStart_time = time.time()
        self.__FPS = False
        self.DisplayFps = False

        self.io_engine = None
        self.s_engine = None
        self.quit = False

    @staticmethod
    def ScreennSizeChange(sender, last_columns, last_row, new_columns, new_row):
        sender.father.Height = new_row
        sender.father.Width = new_columns
        sender.father.render_update()

    def end(self):
        self.quit = True

    @staticmethod
    def ScreenKeyRelease(sender, father, input, key_alias, printable):
        if key_alias == "CTRL+ALT+C":
            father.father.end()

    def start(self):
        self.io_engine = ShellIO(self)
        self.io_engine.start()
        self.s_engine = ShellSize(self)
        self.s_engine.start()
        self.__GUI__init__()

    def __GUI__init__(self):
        self.s_engine.OnChange += Screen.ScreennSizeChange
        self.io_engine.onKeyRelease += Screen.ScreenKeyRelease
        self.RenderEngine = self.ScreenRenderEngine

        while not self.quit:
            time.sleep(0.015)
            self.draw()
            if self.DisplayFps:
                self.__FPS = 1.0 / (time.time() - self.__FPSStart_time)
                self.__FPSStart_time = time.time()
                sys.stdout.write(CSI.CUP(2, 2))
                sys.stdout.write("FPS: " + str(self.__FPS) + "\t--\t" + str(self.Width) + "x" + str(self.Height))
                sys.stdout.flush()

        self.s_engine.stop()
        self.io_engine.stop()

    def ScreenRenderEngine(self):
        h = int(self.ActualHeight)
        w = int(self.ActualWidth)
        t = self.Background.renderBuffer + self.Foreground.renderBuffer
        for i in range(0, h +1):
            t += " " * w
            if i!= h+1:
                t += "\n"
        t += self.Background.renderBuffer + self.Foreground.renderBuffer
        return t
