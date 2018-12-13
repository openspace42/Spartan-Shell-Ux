from Spartan.Common import Event
from Spartan.Common import DocBuilder
from Spartan.Shell.Demons.StandardKeyEngine import StandardKeyEngine
import threading
import sys
import os
import termios
import tty


class ShellIO(object):
    __doc__ = "run ShellIO.help() for see a help"
    __doc2__ = {
        'class name': 'ShellIO',
        'constructors': [
            {
                "params": [],
                "description": "new ShellIO Class"
             }
        ],
        'property': [

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
                "name": "onKeyPress",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "input",
                        "type": "[chr,str]",
                        "description": "decoded buffer"
                    },
                    {
                        "name": "key_alias",
                        "type": "str",
                        "description": "the alias of input "
                    },
                    {
                        "name": "printable",
                        "type": "bool",
                        "description": "nif true a char is printable"
                    }
                ],
                "description": "invoke on on key is press"
            },
            {
                "name": "onKeyRelease",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "input",
                        "type": "[chr,str]",
                        "description": "decoded buffer"
                    },
                    {
                        "name": "key_alias",
                        "type": "str",
                        "description": "the alias of input "
                    },
                    {
                        "name": "printable",
                        "type": "bool",
                        "description": "nif true a char is printable"
                    }
                ],
                "description": "invoke on on key is released"
            },
            {
                "name": "onKeyContinuingPress",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "input",
                        "type": "[chr,str]",
                        "description": "decoded buffer"
                    },
                    {
                        "name": "key_alias",
                        "type": "str",
                        "description": "the alias of input "
                    },
                    {
                        "name": "printable",
                        "type": "bool",
                        "description": "nif true a char is printable"
                    }
                ],
                "description": "invoke on on key is press for more time"
            },
            {
                "name": "onMouseLeftPress",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "x_location",
                        "type": "int",
                        "description": "a x position on shell"
                    },
                    {
                        "name": "y_location",
                        "type": "int",
                        "description": "a y position on shell "
                    },
                ],
                "description": "invoke on left button of mouse is pushed"
            },
            {
                "name": "onMouseLeftRelease",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "x_location",
                        "type": "int",
                        "description": "a x position on shell"
                    },
                    {
                        "name": "y_location",
                        "type": "int",
                        "description": "a y position on shell "
                    },
                ],
                "description": "invoke on left button of mouse is released"
            },
            {
                "name": "onMouseLeftPressMove",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "last_x_location",
                        "type": "int",
                        "description": "a last  x position on shell"
                    },
                    {
                        "name": "last_y_location",
                        "type": "int",
                        "description": "a last y position on shell "
                    },
                    {
                        "name": "x_location",
                        "type": "int",
                        "description": "a x position on shell"
                    },
                    {
                        "name": "y_location",
                        "type": "int",
                        "description": "a y position on shell "
                    }
                ],
                "description": "invoke on left button of mouse is in dragging"
            },
            {
                "name": "onMouseRightPress",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "x_location",
                        "type": "int",
                        "description": "a x position on shell"
                    },
                    {
                        "name": "y_location",
                        "type": "int",
                        "description": "a y position on shell "
                    },
                ],
                "description": "invoke on right button of mouse is pushed"
            },
            {
                "name": "onMouseRightRelease",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "x_location",
                        "type": "int",
                        "description": "a x position on shell"
                    },
                    {
                        "name": "y_location",
                        "type": "int",
                        "description": "a y position on shell "
                    },
                ],
                "description": "invoke on right button of mouse is released"
            },
            {
                "name": "onMouseRightPressMove",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "last_x_location",
                        "type": "int",
                        "description": "a last  x position on shell"
                    },
                    {
                        "name": "last_y_location",
                        "type": "int",
                        "description": "a last y position on shell "
                    },
                    {
                        "name": "x_location",
                        "type": "int",
                        "description": "a x position on shell"
                    },
                    {
                        "name": "y_location",
                        "type": "int",
                        "description": "a y position on shell "
                    }
                ],
                "description": "invoke on right button of mouse is in dragging"
            },
            {
                "name": "onMouseMiddlePress",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "x_location",
                        "type": "int",
                        "description": "a x position on shell"
                    },
                    {
                        "name": "y_location",
                        "type": "int",
                        "description": "a y position on shell "
                    },
                ],
                "description": "invoke on middle button of mouse is pushed"
            },
            {
                "name": "onMouseMiddleRelease",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "x_location",
                        "type": "int",
                        "description": "a x position on shell"
                    },
                    {
                        "name": "y_location",
                        "type": "int",
                        "description": "a y position on shell "
                    },
                ],
                "description": "invoke on middle button of mouse is released"
            },
            {
                "name": "onMouseMiddlePressMove",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "last_x_location",
                        "type": "int",
                        "description": "a last  x position on shell"
                    },
                    {
                        "name": "last_y_location",
                        "type": "int",
                        "description": "a last y position on shell "
                    },
                    {
                        "name": "x_location",
                        "type": "int",
                        "description": "a x position on shell"
                    },
                    {
                        "name": "y_location",
                        "type": "int",
                        "description": "a y position on shell "
                    }
                ],
                "description": "invoke on middle button of mouse is in dragging"
            },
            {
                "name": "onMouseMiddleUp",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "x_location",
                        "type": "int",
                        "description": "a x position on shell"
                    },
                    {
                        "name": "y_location",
                        "type": "int",
                        "description": "a y position on shell "
                    },
                ],
                "description": "invoke on middle button move up"
            },
            {
                "name": "onMouseMiddleDown",
                "params": [
                    {
                        "name": "sender",
                        "type": "KeyEngine",
                        "description": "the KeyEngine object that raised the event"
                    },
                    {
                        "name": "father",
                        "type": "ShellIO",
                        "description": "the ShellIO object that raised the event"
                    },
                    {
                        "name": "x_location",
                        "type": "int",
                        "description": "a x position on shell"
                    },
                    {
                        "name": "y_location",
                        "type": "int",
                        "description": "a y position on shell "
                    },
                ],
                "description": "invoke on middle button move down"
            }
        ]
    }

    def __init__(self):
        self.onKeyPress = Event()
        self.onKeyRelease = Event()
        self.onKeyContinuingPress = Event()

        self.onMouseLeftPress = Event()
        self.onMouseLeftRelease = Event()
        self.onMouseLeftPressMove = Event()

        self.onMouseMiddlePress = Event()
        self.onMouseMiddleRelease = Event()
        self.onMouseMiddlePressMove = Event()

        self.onMouseMiddleUp = Event()
        self.onMouseMiddleDown = Event()

        self.onMouseRightPress = Event()
        self.onMouseRightRelease = Event()
        self.onMouseRightPressMove = Event()

        self.buffer = ""

        self.__IOListener = ShellIOListenerThread(self)
        self.__IOListener.setDaemon(True)
        self.__fd = None

        self.__KeyEngine = StandardKeyEngine(self)
        self.__KeyEngine.setDaemon(True)

        self.__shellOldSettings = None

    def start(self):
        os.system('echo -e "\0337\033[?47h\033[r\033[m\033[2J\033[H\033[?7h\033[?1;3;4;6l\033[?1h\033=\033[?1000h";')
        os.system("tput civis")
        os.system("stty -echo")
        self.__IOListener.start()
        self.__fd = sys.stdin.fileno()
        self.__shellOldSettings = termios.tcgetattr(self.__fd)
        tty.setraw(self.__fd)
        self.buffer = ""
        self.__KeyEngine.start()

    def stop(self):
        self.__IOListener.stop()
        self.__KeyEngine.stop()
        termios.tcsetattr(self.__fd, termios.TCSADRAIN, self.__shellOldSettings)
        os.system("stty echo")
        os.system("tput cnorm")
        os.system('echo -e "\033[2J\033[?47l\0338\033[?1000l"')

    @staticmethod
    def help():
        return DocBuilder.analyzer_object(ShellIO.__doc2__)

    @property
    def is_running(self):
        return self.__IOListener.is_running or self.__KeyEngine.is_running


class ShellIOListenerThread(threading.Thread):
    def __init__(self, father):
        threading.Thread.__init__(self)
        self.__father = father
        self.__run = True
        return

    def run(self):
        try:
            while self.__run:
                ch = sys.stdin.read(1)
                self.__father.buffer += ch
        except (KeyboardInterrupt, EOFError):
            pass
        return

    def stop(self):
        self.__run = False

    @property
    def is_running(self):
        return self.__run
