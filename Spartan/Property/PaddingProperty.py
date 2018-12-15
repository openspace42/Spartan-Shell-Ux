from Spartan.Common import Event


class PaddingProperty(object):
    def __init__(self, top, bottom, right, left):
        self.__Padding = PaddingObject(self, top, bottom, right, left)
        self.onPaddingChange = Event()
        self.beforeOnPaddingChange = Event()

    @property
    def Padding(self):
        return self.__Padding

    @Padding.setter
    def Padding(self, value):
        # noinspection PyTypeChecker
        self.beforeOnPaddingChange(self, self.__Padding, value)
        t = self.__Padding
        self.__Padding = value
        # noinspection PyTypeChecker
        self.onPaddingChange(self, t, value)


class PaddingObject(object):
    def __init__(self, father, top, bottom, right, left):
        self.__father = father
        self.__Top = top
        self.__Bottom = bottom
        self.__Right = right
        self.__Left = left
        self.onTopChange = Event()
        self.beforeOnTopChange = Event()

        self.onBottomChange = Event()
        self.beforeOnBottomChange = Event()

        self.onRightChange = Event()
        self.beforeOnRightChange = Event()

        self.onLeftChange = Event()
        self.beforeOnLeftChange = Event()

    @property
    def Top(self):
        return self.__Top

    @Top.setter
    def Top(self, value):
        # noinspection PyTypeChecker
        self.beforeOnTopChange(self, self.__father, self.__Top, value)
        t = self.Top
        self.__Top = value
        # noinspection PyTypeChecker
        self.onTopChange(self, self.__father, t, value)

    @property
    def Bottom(self):
        return self.__Bottom

    @Bottom.setter
    def Bottom(self, value):
        # noinspection PyTypeChecker
        self.beforeOnBottomChange(self, self.__father, self.__Bottom, value)
        t = self.Bottom
        self.__Bottom = value
        # noinspection PyTypeChecker
        self.onBottomChange(self, self.__father, t, value)

    @property
    def Right(self):
        return self.__Right

    @Right.setter
    def Right(self, value):
        # noinspection PyTypeChecker
        self.beforeOnRightChange(self, self.__father, self.__Right, value)
        t = self.Right
        self.__Right = value
        # noinspection PyTypeChecker
        self.onRightChange(self, self.__father, t, value)

    @property
    def Left(self):
        return self.__Left

    @Left.setter
    def Left(self, value):
        # noinspection PyTypeChecker
        self.beforeOnLeftChange(self, self.__father, self.__Left, value)
        t = self.Left
        self.__Left = value
        # noinspection PyTypeChecker
        self.onLeftChange(self, self.__father, t, value)
