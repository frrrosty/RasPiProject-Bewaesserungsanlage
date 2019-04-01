#!/usr/bin/env python

import grovepi
import math
import time

sensor = 3

blue = 0
white = 1

[temp, humidity] = grovepi.dht(sensor, white)
if math.isnan(temp) == False and math.isnan(humidity) == False:
    print("temp = %.02f C humidity =%.02f%%" % (temp, humidity))

    if temp > int(25):
        print("Test Temp")



