import sys
sys.path[0]=(sys.path[0].replace("/Tests", ""))
from Spartan.Shell.Demons import ShellSize

SS = ShellSize()
print(ShellSize.help())
