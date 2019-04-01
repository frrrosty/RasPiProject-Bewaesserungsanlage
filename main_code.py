import time
import calendar
import math
from grovepi import *
from grove.gpio import GPIO
import sys

#Anschluesse:
moisture_sensor = 0
ultrasonic_ranger = 4
dht_pro = 3
relay_pump = 7
white = 1

#Variablen:
water_given = "Day"
fuellstand = ultrasonicRead(ultrasonic_ranger)
moisture_soil = grovepi.analogRead(moisture_sensor)
temp_hum = grovepi.dht(sensor, white)




