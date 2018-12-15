from .CSISeq import CSISeq


class SRGSeq(object):

    @staticmethod
    def Reset():
        return CSISeq.SGR(0)

    @staticmethod
    def Normal():
        return CSISeq.SGR(0)

    @staticmethod
    def Bold():
        return CSISeq.SGR(1)

    @staticmethod
    def IncreasedIntensity():
        return CSISeq.SGR(1)

    @staticmethod
    def Faint():
        return CSISeq.SGR(2)

    @staticmethod
    def DecreasedIntensity():
        return CSISeq.SGR(2)

    @staticmethod
    def Italic():
        return CSISeq.SGR(3)

    @staticmethod
    def Underline():
        return CSISeq.SGR(4)

    @staticmethod
    def Blink():
        return CSISeq.SGR(5)

    @staticmethod
    def SlowBlink():
        return CSISeq.SGR(5)

    @staticmethod
    def RapidBlink():
        return CSISeq.SGR(6)

    @staticmethod
    def Reverse():
        return CSISeq.SGR(7)

    @staticmethod
    def Conceal():
        return CSISeq.SGR(8)

    @staticmethod
    def Conceal_out():
        return CSISeq.SGR(9)

    @staticmethod
    def DefaultFont():
        return CSISeq.SGR(10)

    @staticmethod
    def Font(n):
        if 0 <= n < 10:
            return CSISeq.SGR(10+n)
        return ""

    @staticmethod
    def Fraktur():
        return CSISeq.SGR(20)

    @staticmethod
    def Bold_Off2():
        return CSISeq.SGR(21)

    @staticmethod
    def DoublyUnderline():
        return CSISeq.SGR(21)

    @staticmethod
    def NormalIntensity():
        return CSISeq.SGR(22)

    @staticmethod
    def Bold_Off():
        return CSISeq.SGR(22)

    @staticmethod
    def Italic_Off():
        return CSISeq.SGR(23)

    @staticmethod
    def Fraktur_Off():
        return CSISeq.SGR(23)

    @staticmethod
    def Underline_Off():
        return CSISeq.SGR(24)

    @staticmethod
    def Blink_Off():
        return CSISeq.SGR(25)

    @staticmethod
    def Inverse_Off():
        return CSISeq.SGR(27)

    @staticmethod
    def Conceal_Off():
        return CSISeq.SGR(28)

    @staticmethod
    def Reveal():
        return CSISeq.SGR(28)

    @staticmethod
    def Conceal_out_Off():
        return CSISeq.SGR(29)

    @staticmethod
    def Foreground_3bit(n):
        if 0 <= n < 8:
            return CSISeq.SGR(30+n)
        return ""

    @staticmethod
    def Foreground_8bit(n):
        if 0 <= n < 255:
            return CSISeq.SGR("38;5;"+str(n))
        return ""

    @staticmethod
    def Foreground_24bit(r, g, b):
        if 0 <= r < 255 and 0 <= g < 255 and 0 <= b < 255:
            return CSISeq.SGR("38;2;"+str(r)+";"+str(g)+";"+str(b))
        return ""

    @staticmethod
    def DefaultForeground():
        return CSISeq.SGR(39)

    @staticmethod
    def Background_3bit(n):
        if 0 <= n < 8:
            return CSISeq.SGR(40+n)
        return ""

    @staticmethod
    def Background_8bit(n):
        if 0 <= n < 255:
            return CSISeq.SGR("48;5;"+str(n))
        return ""

    @staticmethod
    def Background_24bit(r, g, b):
        if 0 <= r < 255 and 0 <= g < 255 and 0 <= b < 255:
            return CSISeq.SGR("48;2;"+str(r)+";"+str(g)+";"+str(b))
        return ""

    @staticmethod
    def DefaultBackground():
        return CSISeq.SGR(49)

    @staticmethod
    def Framed():
        return CSISeq.SGR(51)

    @staticmethod
    def Encircled():
        return CSISeq.SGR(52)

    @staticmethod
    def OverLined():
        return CSISeq.SGR(53)

    @staticmethod
    def Framed_Off():
        return CSISeq.SGR(54)

    @staticmethod
    def Encircled_Off():
        return CSISeq.SGR(54)

    @staticmethod
    def OverLined_Off():
        return CSISeq.SGR(55)

    @staticmethod
    def IdeogramUnderline():
        return CSISeq.SGR(60)

    @staticmethod
    def RightSideLine():
        return CSISeq.SGR(60)

    @staticmethod
    def IdeogramDoubleUnderline():
        return CSISeq.SGR(61)

    @staticmethod
    def DoubleRightSideLine():
        return CSISeq.SGR(61)

    @staticmethod
    def IdeogramOverline():
        return CSISeq.SGR(62)

    @staticmethod
    def LeftSideLine():
        return CSISeq.SGR(62)

    @staticmethod
    def IdeogramDoubleOverline():
        return CSISeq.SGR(63)

    @staticmethod
    def DoubleLeftSideLine():
        return CSISeq.SGR(63)

    @staticmethod
    def IdeogramStressMarking():
        return CSISeq.SGR(64)

    @staticmethod
    def IdeogramAttributes_Off():
        return CSISeq.SGR(65)

    # noinspection SpellCheckingInspection
    ''' aixterm '''

    @staticmethod
    def Foreground_Bright_3bit(n):
        if 0 <= n < 8:
            return CSISeq.SGR(90+n)
        return ""

    @staticmethod
    def Background_Bright_3bit(n):
        if 0 <= n < 8:
            return CSISeq.SGR(100+n)
        return ""
