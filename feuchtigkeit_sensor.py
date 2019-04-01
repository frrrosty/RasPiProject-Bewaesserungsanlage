#!/usr/bin/env python

# NOTE:
# 	The wiki suggests the following sensor values:
# 		Min  Typ  Max  Condition
# 		0    0    0    sensor in open air
# 		0    20   300  sensor in dry soil
# 		300  580  700  sensor in humid soil
# 		700  940  950  sensor in water

# 	Sensor values observer:
# 		Val  Condition
# 		0    sensor in open air
# 		18   sensor in dry soil
# 		425  sensor in humid soil
# 		690  sensor in water

import time
import grovepi

# Connect the Grove Moisture Sensor to analog port A0
# SIG,NC,VCC,GND
moisture_sensor = 0


while True:
	try:
		print(grovepi.analogRead(moisture_sensor))

		time.sleep(.5)

	except KeyboardInterrupt:
		break
	except IOError:
		print ("Error")
