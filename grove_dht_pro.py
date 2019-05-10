#!/usr/bin/env python

import grovepi

sensor = 3

blue = 0
white = 1

def aussentemp():
    [temp, humidity] = grovepi.dht(sensor, white)
    return temp

def luftfeuchtikeit():
    [temp, humidity] = grovepi.dht(sensor, white)
    return humidity
