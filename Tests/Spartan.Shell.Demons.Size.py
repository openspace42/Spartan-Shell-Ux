import sys
import time
sys.path[0]=(sys.path[0].replace("/Tests", ""))


from Spartan.Shell.Demons import ShellSize

SS = ShellSize()
print(ShellSize.help())
print("\n\npress enter to continue the demo\n\n")
a = sys.stdin.read(1)


def locate(x, y):
    sys.stdout.write("\033[" + str(y) + ";" + str(x) + "H")


def cls():
    sys.stdout.write("\033[2J")


def normalize(num):
    if num < 10:
        return "  "+str(num)
    if num < 100:
        return " "+str(num)
    return str(num)


def on_change(sender, last_columns, last_row, new_columns, new_row):
    if new_columns <= 25 or new_row <= 8:
        sender.stop()
    else:
        cls()
        for i in range(1, new_columns+1):
            locate(i, 1)
            if i is 1:
                sys.stdout.write(u"\u250C")
            if i is new_columns:
                sys.stdout.write(u'\u2510')
            else:
                sys.stdout.write(u'\u2500')
        for i in range(2,new_row):
            locate(1, i)
            sys.stdout.write(u'\u2502')
            locate(new_columns, i)
            sys.stdout.write(u'\u2502')
        for i in range(1, new_columns+1):
            locate(i, new_row)
            if i is 1:
                sys.stdout.write(u"\u2514")
            if i is new_columns:
                sys.stdout.write(u'\u2518')
            else:
                sys.stdout.write(u'\u2500')

        y=int((new_row-2)/2)
        x= int((new_columns-21)/2)
        locate(x, y)
        sys.stdout.write(u'\u2554' + u"\u2550" * 10 + u"\u2566" + u"\u2550" * 10 + u"\u2557")
        locate(x, y+1)
        sys.stdout.write(u'\u2551' + " Old Size " + u'\u2551' + " New Size " + u'\u2551')
        locate(x, y+2)
        sys.stdout.write(u'\u2560' + u"\u2550" * 10 + u"\u256C" + u"\u2550" * 10 + u"\u2563")
        locate(x, y + 3)
        sys.stdout.write(u'\u2551' + " "+normalize(last_columns)+"x"+normalize(last_row)+"  " + u'\u2551' +
                         " "+normalize(new_columns)+"x"+normalize(new_row)+"  " + u'\u2551')
        locate(x, y + 4)
        sys.stdout.write(u'\u255A' + u"\u2550" * 10 + u"\u2569" + u"\u2550" * 10 + u"\u255D")
    locate(2, 2)
    sys.stdout.write("\033[38;2;253;204;0mFor exit x<=25 or y<=8\033[39m")
    locate(1, 1)
    sys.stdout.flush()


SS.OnChange += on_change

SS.start()

while SS.is_running is True:
    time.sleep(0.05)

cls()
sys.stdout.flush()
print("\n")

