from enum import Enum
from Spartan.Common import Event


class HorizontalAlignProperty(object):
    def __init__(self):
        self.__horizontalAlign = HorizontalAlignEnum.Center
        self.onHorizontalAlignChange = Event()
        self.beforeOnHorizontalAlignChange = Event()

    @property
    def HorizontalAlign(self):
        return self.__horizontalAlign

    @HorizontalAlign.setter
    def HorizontalAlign(self, value):
        if isinstance(value, HorizontalAlignEnum):
            if self.__horizontalAlign != value:
                # noinspection PyTypeChecker
                self.beforeOnHorizontalAlignChange(self, self.__horizontalAlign, value)
                t = self.__horizontalAlign
                self.__horizontalAlign = value
                # noinspection PyTypeChecker
                self.onHorizontalAlignChange(self, t, value)


class HorizontalAlignEnum(Enum):
    Top = 1
    Center = 2
    Bottom = 3
    Fill = 4
