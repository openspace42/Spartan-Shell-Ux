import sys
import time
sys.path[0]=(sys.path[0].replace("/Tests", ""))
from Spartan.Shell.Demons.IO import ShellIO


SIO = ShellIO()
print(ShellIO.help())
print("\n\npress enter to continue the demo\n\n")
a = sys.stdin.read(1)

exit = False


def locate(x, y):
    sys.stdout.write("\033[" + str(y) + ";" + str(x) + "H")


def on_key_press(sender, father, input, key_alias, printable):
    if key_alias == "CTRL+ALT+C":
        SIO.stop()
    else:
        locate(33, 4)
        sys.stdout.write("                     ")
        locate(33, 4)
        sys.stdout.write(key_alias)
        locate(64, 4)
        sys.stdout.write("True " if printable else "False")
        sys.stdout.flush()


def on_key_release(sender, father, input, key_alias, printable):
    if key_alias == "CTRL+ALT+C":
        SIO.stop()
    else:
        locate(33, 5)
        sys.stdout.write("                     ")
        locate(33, 5)
        sys.stdout.write(key_alias)
        locate(64, 5)
        sys.stdout.write("True " if printable else "False")
        sys.stdout.flush()


def on_key_continuing_press(sender, father, input, key_alias, printable):
    if key_alias == "CTRL+ALT+C":
        SIO.stop()
    else:
        locate(33, 6)
        sys.stdout.write("                     ")
        locate(33, 6)
        sys.stdout.write(key_alias)
        locate(64, 6)
        sys.stdout.write("True " if printable else "False")
        sys.stdout.flush()


def on_mouse_left_press(sender, father, x_location, y_location):
    locate(29, 9)
    sys.stdout.write("    ")
    locate(29, 9)
    sys.stdout.write(str(x_location))
    locate(37, 9)
    sys.stdout.write("    ")
    locate(37, 9)
    sys.stdout.write(str(y_location))
    sys.stdout.flush()


def on_mouse_left_release(sender, father, x_location, y_location):
    locate(29, 10)
    sys.stdout.write("    ")
    locate(29, 10)
    sys.stdout.write(str(x_location))
    locate(37, 10)
    sys.stdout.write("    ")
    locate(37, 10)
    sys.stdout.write(str(y_location))
    sys.stdout.flush()


def on_mouse_left_press_move(sender, father, last_x_location, last_y_location, x_location, y_location):
    locate(29, 11)
    sys.stdout.write("    ")
    locate(29, 11)
    sys.stdout.write(str(x_location))
    locate(37, 11)
    sys.stdout.write("    ")
    locate(37, 11)
    sys.stdout.write(str(y_location))
    locate(50, 11)
    sys.stdout.write("    ")
    locate(50, 11)
    sys.stdout.write(str(x_location))
    locate(63, 11)
    sys.stdout.write("    ")
    locate(63, 11)
    sys.stdout.write(str(y_location))
    sys.stdout.flush()


def on_mouse_right_press(sender, father, x_location, y_location):
    locate(29, 14)
    sys.stdout.write("    ")
    locate(29, 14)
    sys.stdout.write(str(x_location))
    locate(37, 14)
    sys.stdout.write("    ")
    locate(37, 14)
    sys.stdout.write(str(y_location))
    sys.stdout.flush()


def on_mouse_right_release(sender, father, x_location, y_location):
    locate(29, 15)
    sys.stdout.write("    ")
    locate(29, 15)
    sys.stdout.write(str(x_location))
    locate(37, 15)
    sys.stdout.write("    ")
    locate(37, 15)
    sys.stdout.write(str(y_location))
    sys.stdout.flush()


def on_mouse_right_press_move(sender, father, last_x_location, last_y_location, x_location, y_location):
    locate(29, 16)
    sys.stdout.write("    ")
    locate(29, 16)
    sys.stdout.write(str(x_location))
    locate(37, 16)
    sys.stdout.write("    ")
    locate(37, 16)
    sys.stdout.write(str(y_location))
    locate(50, 16)
    sys.stdout.write("    ")
    locate(50, 16)
    sys.stdout.write(str(x_location))
    locate(63, 16)
    sys.stdout.write("    ")
    locate(63, 16)
    sys.stdout.write(str(y_location))
    sys.stdout.flush()


def on_mouse_middle_press(sender, father, x_location, y_location):
    locate(29, 19)
    sys.stdout.write("    ")
    locate(29, 19)
    sys.stdout.write(str(x_location))
    locate(37, 19)
    sys.stdout.write("    ")
    locate(37, 19)
    sys.stdout.write(str(y_location))
    sys.stdout.flush()


def on_mouse_middle_release(sender, father, x_location, y_location):
    locate(29, 20)
    sys.stdout.write("    ")
    locate(29, 20)
    sys.stdout.write(str(x_location))
    locate(37, 20)
    sys.stdout.write("    ")
    locate(37, 20)
    sys.stdout.write(str(y_location))
    sys.stdout.flush()


def on_mouse_middle_press_move(sender, father, last_x_location, last_y_location, x_location, y_location):
    locate(29, 21)
    sys.stdout.write("    ")
    locate(29, 21)
    sys.stdout.write(str(x_location))
    locate(37, 21)
    sys.stdout.write("    ")
    locate(37, 21)
    sys.stdout.write(str(y_location))
    locate(50, 21)
    sys.stdout.write("    ")
    locate(50, 21)
    sys.stdout.write(str(x_location))
    locate(63, 21)
    sys.stdout.write("    ")
    locate(63, 21)
    sys.stdout.write(str(y_location))
    sys.stdout.flush()


def on_mouse_middle_up(sender, father, x_location, y_location):
    locate(29, 22)
    sys.stdout.write("    ")
    locate(29, 22)
    sys.stdout.write(str(x_location))
    locate(37, 22)
    sys.stdout.write("    ")
    locate(37, 22)
    sys.stdout.write(str(y_location))
    sys.stdout.flush()


def on_mouse_middle_down(sender, father, x_location, y_location):
    locate(29, 23)
    sys.stdout.write("    ")
    locate(29, 23)
    sys.stdout.write(str(x_location))
    locate(37, 23)
    sys.stdout.write("    ")
    locate(37, 23)
    sys.stdout.write(str(y_location))
    sys.stdout.flush()


SIO.onKeyPress += on_key_press
SIO.onKeyRelease += on_key_release
SIO.onKeyContinuingPress += on_key_continuing_press

SIO.onMouseLeftPress += on_mouse_left_press
SIO.onMouseLeftRelease += on_mouse_left_release
SIO.onMouseLeftPressMove += on_mouse_left_press_move

SIO.onMouseRightPress += on_mouse_right_press
SIO.onMouseRightRelease += on_mouse_right_release
SIO.onMouseRightPressMove += on_mouse_right_press_move

SIO.onMouseMiddlePress += on_mouse_middle_press
SIO.onMouseMiddleRelease += on_mouse_middle_release
SIO.onMouseMiddlePressMove += on_mouse_middle_press_move

SIO.onMouseMiddleUp += on_mouse_middle_up
SIO.onMouseMiddleDown += on_mouse_middle_down

SIO.start()

locate(1, 1)
sys.stdout.write("\033[38;2;253;204;0mPress CTRL+ALT+C to exit\033[39m")
locate(1, 3)
sys.stdout.write("\033[38;2;241;203;255mKeyboard Events:\033[39m")
locate(1, 4)
sys.stdout.write("onKeyPress            -> alias:                      Printable: ")
locate(1, 5)
sys.stdout.write("onKeyRelease          -> alias:                      Printable: ")
locate(1, 6)
sys.stdout.write("onKeyContinuingPress  -> alias:                      Printable: ")

locate(1, 8)
sys.stdout.write("\033[38;2;241;203;255mMouseLeft Events:\033[39m")
locate(1, 9)
sys.stdout.write("onMouseLeftPress      -> x:      y: ")
locate(1, 10)
sys.stdout.write("onMouseLeftRelease    -> x:      y: ")
locate(1, 11)
sys.stdout.write("onMouseLeftPressMove  -> x:      y:      last x:      last y: ")

locate(1, 13)
sys.stdout.write("\033[38;2;241;203;255mMouseRight Events:\033[39m")
locate(1, 14)
sys.stdout.write("onMouseRightPress     -> x:      y: ")
locate(1, 15)
sys.stdout.write("onMouseRightRelease   -> x:      y: ")
locate(1, 16)
sys.stdout.write("onMouseRightPressMove -> x:      y:      last x:      last y: ")

locate(1, 18)
sys.stdout.write("\033[38;2;241;203;255mMouseMiddle Events:\033[39m")
locate(1, 19)
sys.stdout.write("onMouseMiddlePress     -> x:      y: ")
locate(1, 20)
sys.stdout.write("onMouseMiddleRelease   -> x:      y: ")
locate(1, 21)
sys.stdout.write("onMouseMiddlePressMove -> x:      y:      last x:      last y: ")
locate(1, 22)
sys.stdout.write("onMouseMiddleUp        -> x:      y: ")
locate(1, 23)
sys.stdout.write("onMouseMiddleDown      -> x:      y: ")

locate(1, 25)
sys.stdout.write("\033[38;2;241;203;255mBuffer:\033[39m")

sys.stdout.flush()

while SIO.is_running is True:
    time.sleep(0.05)
    if SIO.buffer is not "":
        locate(1, 26)
        sys.stdout.write(" "*200)
        locate(1, 26)
        b = bytearray()
        b.extend(SIO.buffer)
        sys.stdout.write(''.join(format(x, '02x') for x in b))
        sys.stdout.flush()

print("\n")
