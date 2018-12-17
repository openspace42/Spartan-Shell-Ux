import threading
import time
import os
from Spartan.Common import Event
from Spartan.Common import DocBuilder


class ShellSize(object):
    __doc__ = "run ShellSize.help() for see a help"
    __doc2__ = {
        'class name': 'ShellSize',
        'constructors': [
            {
                "params": [],
                "description": "new ShellSize Class"
             }
        ],
        'property': [
            {
                "name": "LastColumns",
                "type": "int",
                "description": "is a last column read, (x) size"
            },
            {
                "name": "LastRow",
                "type": "int",
                "description": "is a last row read, (y) size"
            },
            {
                "name": "is_running",
                "type": "property[get] bool",
                "description": "if true a demon is running"
            },
            {
                "name": "frequency",
                "type": "property[get,set] float",
                "description": "is the frequency with which\nit reads the size of the shell (1 = a second)"
            },
        ],
        "methods": [
            {
                "name": "start",
                "params": [],
                "description": "method, for start a demon",
                "return_type": "None"

            },
            {
                "name": "stop",
                "params": [],
                "description": "method, for stop a demon",
                "return_type": "None"
            }
        ],
        "events": [
            {
                "name": "OnChange",
                "params": [
                    {
                        "name": "sender",
                        "type": "ShellSize",
                        "description": "the ShellSize object that raised the event"
                    },
                    {
                        "name": "last_columns",
                        "type": "int",
                        "description": "last columns read"
                    },
                    {
                        "name": "last_row",
                        "type": "int",
                        "description": "last row read"
                    },
                    {
                        "name": "new_columns",
                        "type": "int",
                        "description": "new columns read"
                    },
                    {
                        "name": "new_row",
                        "type": "int",
                        "description": "new row read"
                    },
                ],
                "description": "invoke on shell change a size"
             }
        ]
    }

    def __init__(self, father):
        self.father=father
        self.LastColumns = 0
        self.LastRow = 0
        self.__running = False
        self.__frequency = 0.1
        self.__engine = None
        self.OnChange = None
        self.__engine = _ShellSizeThread(self)
        self.__engine.setDaemon(True)
        self.OnChange = Event()

    def start(self):
        if self.__running is True:
            raise Exception(str(self) + " ShellSize is already running")
        if self.__engine is not None:
            self.__running = True
            self.__engine.start()

    def stop(self):
        self.__running = False

    @staticmethod
    def help():
        return DocBuilder.analyzer_object(ShellSize.__doc2__)

    @property
    def is_running(self):
        return self.__running

    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, value):
        if isinstance(value, float):
            self.__frequency = value
        else:
            raise Exception(str(self) + 'The Frequency of ShellSize can only be a float')


class _ShellSizeThread(threading.Thread):
    def __init__(self, father):
        threading.Thread.__init__(self)
        self.__father = father
        self.LastColumns = 0
        self.LastRow = 0

    def run(self):
        self.LastColumns = 0
        self.LastRow = 0
        while self.__father.is_running:
            time.sleep(self.__father.frequency)
            tmp_rows = _ShellSizeThread.shell_lines()
            tmp_columns = _ShellSizeThread.shell_columns()
            if tmp_columns != self.LastColumns or tmp_rows != self.LastRow:
                self.__father.OnChange(self.__father, int(self.LastColumns), int( self.LastRow),
                                       int(tmp_columns), int(tmp_rows))
                self.LastColumns = tmp_columns
                self.LastRow = tmp_rows
                self.__father.LastColumns = tmp_columns
                self.__father.LastRow = tmp_rows

    @staticmethod
    def shell_lines():
        rows, columns = os.popen('stty size', 'r').read().split()
        return rows

    @staticmethod
    def shell_columns():
        rows, columns = os.popen('stty size', 'r').read().split()
        return columns
