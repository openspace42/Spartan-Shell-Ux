from Spartan.Common import Event


class HeightProperty:
    __doc__ = "run HeightProperty.help() for see a help"
    __doc2__ = {
        'class name': 'HeightProperty',
        'constructors': [
            {
                "params": [],
                "description": "new HeightProperty Class"
             }
        ],
        'property': [
            {
                "name": "ActualHeight",
                "type": "property[get] int",
                "description": "is a real height"
            },
            {
                "name": "Height",
                "type": "property[get,set] int, (str)'auto'",
                "description": "is a height set"
            },
        ],
        "methods": [
        ],
        "events": [
            {
                "name": "onHeightChange",
                "params": [
                    {
                        "name": "sender",
                        "type": "Control",
                        "description": "the control that has the height property or a HeightProperty instance"
                    },
                    {
                        "name": "last_height",
                        "type": "int, (str)'auto'",
                        "description": "last value for height"
                    },
                    {
                        "name": "new_height",
                        "type": "int, (str)'auto'",
                        "description": "new value for height"
                    },
                ],
                "description": "invoke on Height Property change"
             },
            {
                "name": "beforeOnHeightChange",
                "params": [
                    {
                        "name": "sender",
                        "type": "Control",
                        "description": "the control that has the height property or a HeightProperty instance"
                    },
                    {
                        "name": "last_height",
                        "type": "int, (str)'auto'",
                        "description": "last value for height"
                    },
                    {
                        "name": "new_height",
                        "type": "int, (str)'auto'",
                        "description": "new value for height"
                    },
                ],
                "description": "invoke before Height Property change"
            }
        ],
    }

    def __init__(self):
        self.__height = "auto"
        self.__actualHeight = 0
        self.onHeightChange = Event()
        self.beforeOnHeightChange = Event()

    def __calculate_real_Height(self):
        """
        future implementation
        :return: actual height
        :rtype:int
        """
        if isinstance(self, Screen):
            return self.__height
        return 0

    @property
    def ActualHeight(self):
        if self.__height is "auto":
            return self.__calculate_real_Height
        else:
            return self.__height

    @property
    def Height(self):
        return self.__height

    @Height.setter
    def Height(self, value):
        if value is "auto" or isinstance(value, int):
            # noinspection PyTypeChecker
            self.beforeOnHeightChange(self, self.__height, value)
            t = self.__height
            self.__height = value
            # noinspection PyTypeChecker
            self.onHeightChange(self, t, self.__height)
        else:
            raise Exception("The Height can be only int or (str)'auto'")

