from grove_dht_pro import *
from time import gmtime, strftime
from internet_anbindung import *

def tagesdurchschnitt():

	aktueller_tag = int(strftime("%w", gmtime()))
	aktuelle_stunde = int(strftime("%H", gmtime()))
	aktuelle_minute = int(strftime("%M", gmtime()))

	messung1_temp = 0
	messung2_temp = 0
	messung3_temp = 0
	tages_durchschnitt_temp = 0

	while aktueller_tag != None:
		if aktuelle_stunde == 10 and aktuelle_minute == 0:
			messung1_temp = int(aussentemp())
		elif aktuelle_stunde == 13 and aktuelle_minute == 0:
			messung2_temp = int(aussentemp())
		elif aktuelle_stunde == 17 and aktuelle_minute == 0:
			messung3_temp = int(aussentemp())

		elif messung1_temp != 0 and messung2_temp != 0 and messung3_temp != 0:
			tages_durchschnitt_temp = int((messung1_temp + messung2_temp + messung3_temp) / 3)
			send_data(tages_durchschnitt_temp)
			return int(tages_durchschnitt_temp)
