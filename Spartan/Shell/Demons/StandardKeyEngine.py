import threading
import time


class StandardKeyEngine(threading.Thread):

    __KeyDict__ = [
        {"val": "\x03", "alias": "CTRL+C", "printable": False},
        {"val": "\x1b\x03", "alias": "CTRL+ALT+C", "printable": False},

        {"val": "\x1b\x4f\x41", "alias": "KEY-UP", "printable": False},
        {"val": "\x1b\x4f\x42", "alias": "KEY-DOWN", "printable": False},
        {"val": "\x1b\x4f\x43", "alias": "KEY-RIGHT", "printable": False},
        {"val": "\x1b\x4f\x44", "alias": "KEY-LEFT", "printable": False},

        {"val": "\x1b\x5b\x35\x7e", "alias": "PAG-UP", "printable": False},
        {"val": "\x1b\x5b\x35\x7e", "alias": "PAG-DOWN", "printable": False},

        {"val": "\x0d", "alias": "NEW-LINE", "printable": True},
        {"val": "\x09", "alias": "TAB", "printable": True},
        {"val": "\x1b", "alias": "ESC", "printable": False},
        {"val": "\x7f", "alias": "DELETE", "printable": False},

        {"val": "\x1b\x5b\x34\x7e", "alias": "END", "printable": False},
        {"val": "\x1b\x5b\x31\x7e", "alias": "START", "printable": False},
        {"val": "\x1b\x5b\x32\x7e", "alias": "INSERT", "printable": False},
        {"val": "\x1b\x5b\x33\x7e", "alias": "CANC", "printable": False},

        {"val": "\x1b\x5b\x31\x31\x7e", "alias": "KEY-F1", "printable": False},
        {"val": "\x1b\x5b\x31\x32\x7e", "alias": "KEY-F2", "printable": False},
        {"val": "\x1b\x5b\x31\x33\x7e", "alias": "KEY-F3", "printable": False},
        {"val": "\x1b\x5b\x31\x34\x7e", "alias": "KEY-F4", "printable": False},
        {"val": "\x1b\x5b\x31\x35\x7e", "alias": "KEY-F5", "printable": False},
        {"val": "\x1b\x5b\x31\x37\x7e", "alias": "KEY-F6", "printable": False},
        {"val": "\x1b\x5b\x31\x38\x7e", "alias": "KEY-F7", "printable": False},
        {"val": "\x1b\x5b\x31\x39\x7e", "alias": "KEY-F8", "printable": False},
        {"val": "\x1b\x5b\x32\x30\x7e", "alias": "KEY-F9", "printable": False},
        {"val": "\x1b\x5b\x32\x31\x7e", "alias": "KEY-F10", "printable": False},
        {"val": "\x1b\x5b\x32\x33\x7e", "alias": "KEY-F11", "printable": False},
        {"val": "\x1b\x5b\x32\x34\x7e", "alias": "KEY-F12", "printable": False},

        {"val": "\x20", "alias": "SPACE", "printable": True},
        {"val": "\x21", "alias": "EXCLAMATION-MARK", "printable": True},
        {"val": "\x22", "alias": "DOUBLE-QUOTES", "printable": True},
        {"val": "\x23", "alias": "NUMBER", "printable": True},
        {"val": "\x24", "alias": "DOLLAR", "printable": True},
        {"val": "\x25", "alias": "PER-CENT-SIGN", "printable": True},
        {"val": "\x26", "alias": "AMPERSAND", "printable": True},
        {"val": "\x27", "alias": "SINGLE-QUOTES", "printable": True},
        {"val": "\x28", "alias": "OPEN-PARENTHESIS", "printable": True},
        {"val": "\x29", "alias": "CLOSE-PARENTHESIS", "printable": True},
        {"val": "\x2a", "alias": "ASTERISK", "printable": True},
        {"val": "\x2b", "alias": "PLUS", "printable": True},
        {"val": "\x2c", "alias": "COMMA", "printable": True},
        {"val": "\x2d", "alias": "HYPHEN", "printable": True},
        {"val": "\x2e", "alias": "DOT", "printable": True},
        {"val": "\x2f", "alias": "SLASH", "printable": True},

        {"val": "\x30", "alias": "NUMBER-ZERO", "printable": True},
        {"val": "\x31", "alias": "NUMBER-ONE", "printable": True},
        {"val": "\x32", "alias": "NUMBER-TWO", "printable": True},
        {"val": "\x33", "alias": "NUMBER-THREE", "printable": True},
        {"val": "\x34", "alias": "NUMBER-FOUR", "printable": True},
        {"val": "\x35", "alias": "NUMBER-FIVE", "printable": True},
        {"val": "\x36", "alias": "NUMBER-SIX", "printable": True},
        {"val": "\x37", "alias": "NUMBER-SEVEN", "printable": True},
        {"val": "\x38", "alias": "NUMBER-EIGHT", "printable": True},
        {"val": "\x39", "alias": "NUMBER-NINE", "printable": True},

        {"val": "\x3a", "alias": "COLON", "printable": True},
        {"val": "\x3b", "alias": "SEMICOLON", "printable": True},
        {"val": "\x3c", "alias": "OPEN-ANGLED-BRACKET", "printable": True},
        {"val": "\x3d", "alias": "EQUALS", "printable": True},
        {"val": "\x3e", "alias": "CLOSE-ANGLED-BRACKET", "printable": True},
        {"val": "\x3f", "alias": "QUESTION-MARK", "printable": True},
        {"val": "\x40", "alias": "AT", "printable": True},

        {"val": "\x41", "alias": "LETTER-UPPERCASE-A", "printable": True},
        {"val": "\x42", "alias": "LETTER-UPPERCASE-B", "printable": True},
        {"val": "\x43", "alias": "LETTER-UPPERCASE-C", "printable": True},
        {"val": "\x44", "alias": "LETTER-UPPERCASE-D", "printable": True},
        {"val": "\x45", "alias": "LETTER-UPPERCASE-E", "printable": True},
        {"val": "\x46", "alias": "LETTER-UPPERCASE-F", "printable": True},
        {"val": "\x47", "alias": "LETTER-UPPERCASE-G", "printable": True},
        {"val": "\x48", "alias": "LETTER-UPPERCASE-H", "printable": True},
        {"val": "\x49", "alias": "LETTER-UPPERCASE-I", "printable": True},
        {"val": "\x4a", "alias": "LETTER-UPPERCASE-J", "printable": True},
        {"val": "\x4b", "alias": "LETTER-UPPERCASE-K", "printable": True},
        {"val": "\x4c", "alias": "LETTER-UPPERCASE-L", "printable": True},
        {"val": "\x4d", "alias": "LETTER-UPPERCASE-M", "printable": True},
        {"val": "\x4e", "alias": "LETTER-UPPERCASE-N", "printable": True},
        {"val": "\x4f", "alias": "LETTER-UPPERCASE-O", "printable": True},
        {"val": "\x50", "alias": "LETTER-UPPERCASE-P", "printable": True},
        {"val": "\x51", "alias": "LETTER-UPPERCASE-Q", "printable": True},
        {"val": "\x52", "alias": "LETTER-UPPERCASE-R", "printable": True},
        {"val": "\x53", "alias": "LETTER-UPPERCASE-S", "printable": True},
        {"val": "\x54", "alias": "LETTER-UPPERCASE-T", "printable": True},
        {"val": "\x55", "alias": "LETTER-UPPERCASE-U", "printable": True},
        {"val": "\x56", "alias": "LETTER-UPPERCASE-V", "printable": True},
        {"val": "\x57", "alias": "LETTER-UPPERCASE-W", "printable": True},
        {"val": "\x58", "alias": "LETTER-UPPERCASE-X", "printable": True},
        {"val": "\x59", "alias": "LETTER-UPPERCASE-Y", "printable": True},
        {"val": "\x5a", "alias": "LETTER-UPPERCASE-Z", "printable": True},

        {"val": "\x5b", "alias": "OPEN-BRACKET", "printable": True},
        {"val": "\x5c", "alias": "BACKSLASH", "printable": True},
        {"val": "\x5d", "alias": "CLOSE-BRACKET", "printable": True},
        {"val": "\x5e", "alias": "CARET", "printable": True},
        {"val": "\x5f", "alias": "UNDERSCORE", "printable": True},
        {"val": "\x60", "alias": "GRAVE-ACCENT", "printable": True},

        {"val": "\x61", "alias": "LETTER-LOWERCASE-A", "printable": True},
        {"val": "\x62", "alias": "LETTER-LOWERCASE-B", "printable": True},
        {"val": "\x63", "alias": "LETTER-LOWERCASE-C", "printable": True},
        {"val": "\x64", "alias": "LETTER-LOWERCASE-D", "printable": True},
        {"val": "\x65", "alias": "LETTER-LOWERCASE-E", "printable": True},
        {"val": "\x66", "alias": "LETTER-LOWERCASE-F", "printable": True},
        {"val": "\x67", "alias": "LETTER-LOWERCASE-G", "printable": True},
        {"val": "\x68", "alias": "LETTER-LOWERCASE-H", "printable": True},
        {"val": "\x69", "alias": "LETTER-LOWERCASE-I", "printable": True},
        {"val": "\x6a", "alias": "LETTER-LOWERCASE-J", "printable": True},
        {"val": "\x6b", "alias": "LETTER-LOWERCASE-K", "printable": True},
        {"val": "\x6c", "alias": "LETTER-LOWERCASE-L", "printable": True},
        {"val": "\x6d", "alias": "LETTER-LOWERCASE-M", "printable": True},
        {"val": "\x6e", "alias": "LETTER-LOWERCASE-N", "printable": True},
        {"val": "\x6f", "alias": "LETTER-LOWERCASE-O", "printable": True},
        {"val": "\x70", "alias": "LETTER-LOWERCASE-P", "printable": True},
        {"val": "\x71", "alias": "LETTER-LOWERCASE-Q", "printable": True},
        {"val": "\x72", "alias": "LETTER-LOWERCASE-R", "printable": True},
        {"val": "\x73", "alias": "LETTER-LOWERCASE-S", "printable": True},
        {"val": "\x74", "alias": "LETTER-LOWERCASE-T", "printable": True},
        {"val": "\x75", "alias": "LETTER-LOWERCASE-U", "printable": True},
        {"val": "\x76", "alias": "LETTER-LOWERCASE-V", "printable": True},
        {"val": "\x77", "alias": "LETTER-LOWERCASE-W", "printable": True},
        {"val": "\x78", "alias": "LETTER-LOWERCASE-X", "printable": True},
        {"val": "\x79", "alias": "LETTER-LOWERCASE-Y", "printable": True},
        {"val": "\x7a", "alias": "LETTER-LOWERCASE-Z", "printable": True},

        {"val": "\x7b", "alias": "OPEN-BRACE", "printable": True},
        {"val": "\x7c", "alias": "VERTICAL-BAR", "printable": True},
        {"val": "\x7d", "alias": "CLOSE-BRACE", "printable": True},
        {"val": "\x7e", "alias": "TILDE", "printable": True},


    ]

    def __init__(self, father):
        """
        :param father: a ShellIO
        :type father: ShellIO
        """
        threading.Thread.__init__(self)
        self.__father = father

        self.__run = True
        self.__lastIsKey = False
        self.__lastKeypress = ""

        self.__MousePress = False
        self.__MousePressLast = ""

        self.__MouseLastX = False
        self.__MouseLastY = False

    def run(self):
        while self.__run:
            time.sleep(0.05)

            buffer = self.__father.buffer
            # if (buffer!=None and buffer != ""):
            self.key_engine(buffer)
            self.__father.buffer = ""

    def key_engine(self, char):

        b = bytearray()
        b.extend(char)
        temp_val = StandardKeyEngine.alias_by_val(char)
        if temp_val is not False:
            if self.__lastIsKey:
                if self.__lastKeypress is temp_val.get("alias"):
                    self.__father.onKeyContinuingPress(self, self.__father, self.__lastKeypress,
                                                       temp_val.get("alias"), temp_val.get("printable"))
                else:
                    temp_val2 = StandardKeyEngine.alias_by_alias(self.__lastKeypress)
                    if temp_val2 is not False:
                        self.__father.onKeyRelease(self, self.__father, self.__lastKeypress,
                                                   temp_val2.get("alias"), temp_val2.get("printable"))
                    self.__lastIsKey = True
                    self.__lastKeypress = temp_val.get("alias")
                    self.__father.onKeyContinuingPress(self, self.__father, self.__lastKeypress,
                                                       temp_val.get("alias"), temp_val.get("printable"))
            else:
                self.__lastIsKey = True
                self.__lastKeypress = temp_val.get("alias")
                self.__father.onKeyPress(self, self.__father, self.__lastKeypress,
                                         temp_val.get("alias"), temp_val.get("printable"))
        if char is "":
            if self.__lastIsKey:
                temp_val2 = StandardKeyEngine.alias_by_alias(self.__lastKeypress)
                if temp_val2 is not False:
                    self.__father.onKeyRelease(self, self.__father, self.__lastKeypress,
                                               temp_val2.get("alias"), temp_val2.get("printable"))
                self.__lastKeypress = ""
                self.__lastIsKey = False
        else:
            while len(b) >= 5:
                if len(b) > 0:
                    if b[0] == 27:
                        if len(b) > 1:
                            if b[1] == 91:
                                if len(b) > 2:
                                    if b[2] == 77:
                                        if len(b) > 5:
                                            if b[3] == 32:
                                                '''left press'''
                                                if self.__MousePress:
                                                    if self.__MousePressLast == "LEFT":
                                                        if (self.__MouseLastX != (b[4] - 32) or self.__MouseLastY != (
                                                                b[5] - 32)):
                                                            self.__father.onMouseLeftPressMove(self, self.__father,
                                                                                               self.__MouseLastX,
                                                                                               self.__MouseLastY,
                                                                                               b[4] - 32,
                                                                                               b[5] - 32)
                                                            self.__MouseLastX = b[4] - 32
                                                            self.__MouseLastY = b[5] - 32
                                                    else:
                                                        if self.__MousePressLast == "MIDDLE":
                                                            self.__father.onMouseMiddleRelease(self, self.__father,
                                                                                               b[4] - 32,
                                                                                               b[5] - 32)
                                                        if self.__MousePressLast == "RIGHT":
                                                            self.__father.onMouseRightRelease(self, self.__father,
                                                                                              b[4] - 32,
                                                                                              b[5] - 32)
                                                        self.__MousePress = True
                                                        self.__MousePressLast = "LEFT"
                                                        self.__MouseLastX = b[4] - 32
                                                        self.__MouseLastY = b[5] - 32
                                                        self.__father.onMouseLeftPress(self, self.__father,
                                                                                       b[4] - 32,
                                                                                       b[5] - 32)
                                                else:
                                                    self.__MousePress = True
                                                    self.__MousePressLast = "LEFT"
                                                    self.__MouseLastX = b[4] - 32
                                                    self.__MouseLastY = b[5] - 32
                                                    self.__father.onMouseLeftPress(self, self.__father,
                                                                                   b[4] - 32,
                                                                                   b[5] - 32)

                                            if b[3] == 33:
                                                '''middle press'''
                                                if self.__MousePress:
                                                    if self.__MousePressLast == "MIDDLE":
                                                        if (self.__MouseLastX != (b[4] - 32) or self.__MouseLastY != (
                                                                b[5] - 32)):
                                                            self.__father.onMouseMiddlePressMove(self, self.__father,
                                                                                                 self.__MouseLastX,
                                                                                                 self.__MouseLastY,
                                                                                                 b[4] - 32,
                                                                                                 b[5] - 32)
                                                            self.__MouseLastX = b[4] - 32
                                                            self.__MouseLastY = b[5] - 32
                                                    else:
                                                        if self.__MousePressLast == "LEFT":
                                                            self.__father.onMouseLeftRelease(self, self.__father,
                                                                                             b[4] - 32,
                                                                                             b[5] - 32)
                                                        if self.__MousePressLast == "RIGHT":
                                                            self.__father.onMouseRightRelease(self, self.__father,
                                                                                              b[4] - 32,
                                                                                              b[5] - 32)
                                                        self.__MousePress = True
                                                        self.__MousePressLast = "MIDDLE"
                                                        self.__MouseLastX = b[4] - 32
                                                        self.__MouseLastY = b[5] - 32
                                                        self.__father.onMouseMiddlePress(self, self.__father,
                                                                                         b[4] - 32,
                                                                                         b[5] - 32)
                                                else:
                                                    self.__MousePress = True
                                                    self.__MousePressLast = "MIDDLE"
                                                    self.__MouseLastX = b[4] - 32
                                                    self.__MouseLastY = b[5] - 32
                                                    self.__father.onMouseMiddlePress(self, self.__father,
                                                                                     b[4] - 32,
                                                                                     b[5] - 32)
                                            if b[3] == 34:
                                                '''right press'''
                                                if self.__MousePress:
                                                    if self.__MousePressLast == "RIGHT":
                                                        if (self.__MouseLastX != (b[4] - 32) or self.__MouseLastY != (
                                                                b[5] - 32)):
                                                            self.__father.onMouseRightPressMove(self, self.__father,
                                                                                                self.__MouseLastX,
                                                                                                self.__MouseLastY,
                                                                                                b[4] - 32,
                                                                                                b[5] - 32)
                                                            self.__MouseLastX = b[4] - 32
                                                            self.__MouseLastY = b[5] - 32
                                                    else:
                                                        if self.__MousePressLast == "LEFT":
                                                            self.__father.onMouseLeftRelease(self, self.__father,
                                                                                             b[4] - 32,
                                                                                             b[5] - 32)
                                                        if self.__MousePressLast == "MIDDLE":
                                                            self.__father.onMouseMiddleRelease(self, self.__father,
                                                                                               b[4] - 32,
                                                                                               b[5] - 32)
                                                        self.__MousePress = True
                                                        self.__MousePressLast = "RIGHT"
                                                        self.__MouseLastX = b[4] - 32
                                                        self.__MouseLastY = b[5] - 32
                                                        self.__father.onMouseRightPress(self, self.__father,
                                                                                        b[4] - 32,
                                                                                        b[5] - 32)
                                                else:
                                                    self.__MousePress = True
                                                    self.__MousePressLast = "RIGHT"
                                                    self.__MouseLastX = b[4] - 32
                                                    self.__MouseLastY = b[5] - 32
                                                    self.__father.onMouseRightPress(self, self.__father,
                                                                                    b[4] - 32,
                                                                                    b[5] - 32)

                                            if b[3] == 35:
                                                '''all release'''
                                                if self.__MousePress or True:
                                                    self.__MouseLastX = 0
                                                    self.__MouseLastY = 0
                                                    self.__MousePress = False
                                                    if self.__MousePressLast == "LEFT":
                                                        self.__father.onMouseLeftRelease(self, self.__father,
                                                                                         b[4] - 32,
                                                                                         b[5] - 32)
                                                    if self.__MousePressLast == "MIDDLE":
                                                        self.__father.onMouseMiddleRelease(self, self.__father,
                                                                                           b[4] - 32,
                                                                                           b[5] - 32)
                                                    if self.__MousePressLast == "RIGHT":
                                                        self.__father.onMouseRightRelease(self, self.__father,
                                                                                          b[4] - 32,
                                                                                          b[5] - 32)
                                                    self.__MousePressLast = ""
                                            if b[3] == 96:
                                                '''middle up'''
                                                self.__father.onMouseMiddleUp(self, self.__father,
                                                                              b[4] - 32,
                                                                              b[5] - 32)
                                            if b[3] == 97:
                                                '''middle down'''
                                                self.__father.onMouseMiddleDown(self, self.__father,
                                                                                b[4] - 32,
                                                                                b[5] - 32)
                                            b = b[3:]
                                    b = b[1:]
                            b = b[1:]
                    b = b[1:]

    @staticmethod
    def alias_by_val(char):
        for i in StandardKeyEngine.__KeyDict__:
            if char == str(i.get("val")):
                return i
        return False

    @staticmethod
    def alias_by_alias(alias):
        for i in StandardKeyEngine.__KeyDict__:
            if alias == i.get("alias"):
                return i
        return False

    def stop(self):
        self.__run = False

    @property
    def is_running(self):
        return self.__run
