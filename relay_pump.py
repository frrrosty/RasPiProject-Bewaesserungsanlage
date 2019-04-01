import time
import grovepi


relay = 7

grovepi.pinMode(relay,"OUTPUT")

# switch on for 5 seconds
grovepi.digitalWrite(relay,1)
print "on"
time.sleep(5)

# switch off for 5 seconds
grovepi.digitalWrite(relay,0)
print "off"
time.sleep(5)