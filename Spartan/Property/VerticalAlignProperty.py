from enum import Enum
from Spartan.Common import Event


class VerticalAlignProperty(object):
    def __init__(self):
        self.__verticalAlign = VerticalAlignEnum.Center
        self.onVerticalAlignChange = Event()
        self.beforeOnVerticalAlignChange = Event()

    @property
    def VerticalAlign(self):
        return self.__verticalAlign

    @VerticalAlign.setter
    def VerticalAlign(self, value):
        if isinstance(value, VerticalAlignEnum):
            if self.__verticalAlign != value:
                # noinspection PyTypeChecker
                self.beforeOnVerticalAlignChange(self, self.__verticalAlign, value)
                t = self.__verticalAlign
                self.__verticalAlign = value
                # noinspection PyTypeChecker
                self.onVerticalAlignChange(self, t, value)


class VerticalAlignEnum(Enum):
    Top = 1
    Center = 2
    Bottom = 3
    Fill = 4
