from grovepi import *

ultrasonic_ranger = 4

def wasserstand():
 distanz = ultrasonicRead(ultrasonic_ranger)
 return distanz

def wasserstand_proz():
 fuelmenge_proz = int(((-1)*(wasserstand()) + 51) * 2)
 return fuelmenge_proz

