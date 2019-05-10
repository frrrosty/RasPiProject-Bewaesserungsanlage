from ultrasonic_sensor import *
from relay_pump import *
from feuchtigkeit_sensor import *

def traenken_starten():

	feuchtigkeit = topf_hum()
	fuelmenge = wasserstand()
	fuelmenge_proz = wasserstand_proz()

	global traenken, counter
	while traenken == True:
		if fuelmenge >= 45:
			print("Kein Wasser")
			traenken = False
			counter = 50
			break
		elif fuelmenge < 40 and fuelmenge > 1:
			counter += 1
			print("Das Fass ist zu " + str(fuelmenge_proz) + "% gefuellt.")
			fuelmenge = 1
			if fuelmenge == 1:
				time.sleep(5)
				while feuchtigkeit <= 550:
					relay_on()
					time.sleep(10)
					feuchtigkeit = topf_hum()
					fuelmenge_proz = wasserstand_proz()
					if fuelmenge_proz < 10:
						print("Wasserstand kritisch!")
						relay_off()
						traenken = False
						break
					if feuchtigkeit >= 550:
						relay_off()
						feuchtigkeit = topf_hum()
						fuelmenge = wasserstand()
						traenken = False

