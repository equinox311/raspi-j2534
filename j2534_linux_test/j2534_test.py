import sys

#sys.path.insert(0,'home/pi/Documents/j2534_linux_test/pythonj2534')
#import tactrix

from ctypes import *

op20 = cdll.LoadLibrary("/home/pi/Documents/j2534_linux_test/j2534.so")

interface = op20

name = None
devID = None
channelID = None
baudrate = 500000
protocol = 5

print("Opening Pass through device")
name, devID = interface.PassThruOpen()

