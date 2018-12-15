class EscSeq(object):
    @staticmethod
    def SS2():
        return "\033N"

    @staticmethod
    def SS3():
        return "\033O"

    @staticmethod
    def DCS():
        return "\033P"

    @staticmethod
    def CSI():
        return "\033["

    @staticmethod
    def ST():
        return "\033\\"

    @staticmethod
    def OSC():
        return "\033]"

    @staticmethod
    def SOS():
        return "\033X"

    @staticmethod
    def PM():
        return "\033^"

    @staticmethod
    def APC():
        return "\033_"

    @staticmethod
    def RIS():
        return "\033c"

