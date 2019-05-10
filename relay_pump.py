import grovepi

relay = 2

grovepi.pinMode(relay,"OUTPUT")

def relay_on():
	grovepi.digitalWrite(relay,1)


def relay_off():
	grovepi.digitalWrite(relay,0)
