from .EscSeq import EscSeq


class CSISeq(object):

    @staticmethod
    def CUU(n):
        return EscSeq.CSI()+str(n)+"A"

    @staticmethod
    def CursorUp(n):
        return CSISeq.CUU(n)

    @staticmethod
    def CUD(n):
        return EscSeq.CSI()+str(n)+"B"

    @staticmethod
    def CursorDown(n):
        return CSISeq.CUD(n)

    @staticmethod
    def CUF(n):
        return EscSeq.CSI()+str(n)+"C"

    @staticmethod
    def CursorForward(n):
        return CSISeq.CUF(n)

    @staticmethod
    def CUB(n):
        return EscSeq.CSI() + str(n) + "D"

    @staticmethod
    def CursorBack(n):
        return CSISeq.CUF(n)

    @staticmethod
    def CNL(n):
        return EscSeq.CSI() + str(n) + "E"

    @staticmethod
    def CursorNextLine(n):
        return CSISeq.CNL(n)

    @staticmethod
    def CPL(n):
        return EscSeq.CSI() + str(n) + "F"

    @staticmethod
    def CursorPreviousLine(n):
        return CSISeq.CPL(n)

    @staticmethod
    def CHA(n):
        return EscSeq.CSI() + str(n) + "G"

    @staticmethod
    def CursorHorizontalAbsolute(n):
        return CSISeq.CHA(n)

    @staticmethod
    def CUP(x, y):
        return EscSeq.CSI() + str(y) + ";" + str(x) + "H"

    @staticmethod
    def CursorPosition(x, y):
        return CSISeq.CUP(x, y)

    @staticmethod
    def ED(n=0):
        return EscSeq.CSI() + str(n) + "J"

    @staticmethod
    def EraseDisplay(n=0):
        return CSISeq.ED(n)

    @staticmethod
    def CLS(n=0):
        return CSISeq.ED(n)

    @staticmethod
    def EL(n=0):
        return EscSeq.CSI() + str(n) + "K"

    @staticmethod
    def EraseLinen(n=0):
        return CSISeq.EL(n)

    @staticmethod
    def SU(n):
        return EscSeq.CSI() + str(n) + "S"

    @staticmethod
    def ScrollUp(n):
        return CSISeq.SU(n)

    @staticmethod
    def SD(n):
        return EscSeq.CSI() + str(n) + "T"

    @staticmethod
    def ScrollDown(n):
        return CSISeq.SD(n)

    @staticmethod
    def HVP(x, y):
        return EscSeq.CSI() + str(y) + ";" + str(x) + "f"

    @staticmethod
    def HorizontalVerticalPosition(x, y):
        return CSISeq.HVP(x, y)

    @staticmethod
    def SGR(n):
        return EscSeq.CSI() + str(n) + "m"

    @staticmethod
    def SelectGraphicRendition(n):
        return CSISeq.SGR(n)

    @staticmethod
    def SCP():
        return EscSeq.CSI() + "s"

    @staticmethod
    def SaveCursorPosition(n):
        return CSISeq.SCP(n)

    @staticmethod
    def RCP():
        return EscSeq.CSI() + "u"

    @staticmethod
    def RestoreCursorPosition(n):
        return CSISeq.RCP(n)

    @staticmethod
    def SC():
        return EscSeq.CSI() + "?25h"

    @staticmethod
    def ShowsCursor():
        return CSISeq.SC()

    @staticmethod
    def HC():
        return EscSeq.CSI() + "?25l"

    @staticmethod
    def HidesCursor():
        return CSISeq.HC()

    @staticmethod
    def ESB():
        return EscSeq.CSI() + "?1049h"

    @staticmethod
    def EnableScreenBuffer():
        return CSISeq.ESB()

    @staticmethod
    def DSB():
        return EscSeq.CSI() + "?1049l"

    @staticmethod
    def DisableScreenBuffer():
        return CSISeq.DSB()

