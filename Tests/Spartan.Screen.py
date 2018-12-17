import sys
sys.path[0] = (sys.path[0].replace("/Tests", ""))

import time
from Spartan import Screen

Screen1 = Screen()

def ev1(sender,fron,to):
    to = int(to)
    while(to>255):
        to-=255
    sender.Background.G  =to
    sender.Foreground.G = 255-to

def ev2(sender,fron,to):
    to = int(to)
    while(to>255):
        to-=255
    sender.Background.R=to
    sender.Foreground.R = 255 - to
    sender.Foreground.B = 255 - to


Screen1.beforeOnHeightChange += ev1
Screen1.beforeOnWidthChange += ev2

Screen1.DisplayFps=True

Screen1.start()
