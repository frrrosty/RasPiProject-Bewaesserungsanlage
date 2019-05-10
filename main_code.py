from def_traenken import *
from day_checker import *
from day_average import *

neustart = 0
counter = 0
letzte_bewaesserung = 0

while neustart == 0:

	print("Programm gestartet: Counter steht bei: " + str(counter))
	time.sleep(5)
	traenken = tag_zum_traenken()

	if counter >= 50:
		print("Neustart notwendig!")
		neustart = 1
		break

	if traenken == True:
		traenken_starten()

	elif traenken == False:
		continue
