from Spartan.Common import Event


class WidthProperty:
    __doc__ = "run WidthProperty.help() for see a help"
    __doc2__ = {
        'class name': 'WidthProperty',
        'constructors': [
            {
                "params": [],
                "description": "new WidthProperty Class"
             }
        ],
        'property': [
            {
                "name": "ActualWidth",
                "type": "property[get] int",
                "description": "is a real width"
            },
            {
                "name": "Width",
                "type": "property[get,set] int, (str)'auto'",
                "description": "is a width set"
            },
        ],
        "methods": [
        ],
        "events": [
            {
                "name": "onWidthChange",
                "params": [
                    {
                        "name": "sender",
                        "type": "Control",
                        "description": "the control that has the height property or a WidthProperty instance"
                    },
                    {
                        "name": "last_width",
                        "type": "int, (str)'auto'",
                        "description": "last value for width"
                    },
                    {
                        "name": "new_width",
                        "type": "int, (str)'auto'",
                        "description": "new value for width"
                    },
                ],
                "description": "invoke on Width Property change"
             },
            {
                "name": "beforeOnWidthChange",
                "params": [
                    {
                        "name": "sender",
                        "type": "Control",
                        "description": "the control that has the height property or a WidthProperty instance"
                    },
                    {
                        "name": "last_width",
                        "type": "int, (str)'auto'",
                        "description": "last value for width"
                    },
                    {
                        "name": "new_width",
                        "type": "int, (str)'auto'",
                        "description": "new value for width"
                    },
                ],
                "description": "invoke before Width Property change"
            }
        ],
    }

    def __init__(self):
        self.__width = "auto"
        self.__actualWidth = 0
        self.onWidthChange = Event()
        self.beforeOnWidthChange = Event()

    @classmethod
    def __calculate_real_Width(cls):
        """
        future implementation
        :return: actual width
        :rtype:int
        """
        return 0

    @property
    def ActualWidth(self):
        if self.__width is "auto":
            return self.__calculate_real_Width
        else:
            return self.__width

    @property
    def Width(self):
        return self.__width

    @Width.setter
    def Width(self, value):
        if value is "auto" or isinstance(value, int):
            # noinspection PyTypeChecker
            self.beforeOnWidthChange(self, self.__width, value)
            t = self.__width
            self.__width = value
            # noinspection PyTypeChecker
            self.onWidthChange(self, t, self.__width)
        else:
            raise Exception("The Height can be only int or (str)'auto'")

