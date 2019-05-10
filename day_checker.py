from day_average import *


def tag_zum_traenken():

	global letzte_bewaesserung, messung1_temp, messung2_temp, messung3_temp, tages_durchschnitt_temp

	tages_durchschnitt_temp = int(tagesdurchschnitt())

	aktueller_tag = int(strftime("%w", gmtime()))
	aktuelle_stunde = int(strftime("%H", gmtime()))
	aktuelle_minute = int(strftime("%M", gmtime()))


	if aktueller_tag == 5:
		if (int(aktueller_tag) - int(letzte_bewaesserung)) == 2 or (int(aktueller_tag) - int(letzte_bewaesserung)) == -5 and aktuelle_stunde == 23 and aktuelle_minute == 0:
			letzte_bewaesserung = int(strftime("%w", gmtime()))
			return True
		elif aktuelle_stunde == 23 and aktuelle_minute == 0 and letzte_bewaesserung == 0:
			letzte_bewaesserung = int(strftime("%w", gmtime()))
			return True
		else:
			return False

	if aktueller_tag != 5 and tages_durchschnitt_temp > 30:
		messung1_temp, messung2_temp, messung3_temp = 0,0,0
		letzte_bewaesserung = int(strftime("%w", gmtime()))
		return True

	if (aktueller_tag - letzte_bewaesserung) == 2 or (aktueller_tag - letzte_bewaesserung) == -5 and aktuelle_stunde == 19 and aktuelle_minute == 0:
		if tages_durchschnitt_temp > 20 and tages_durchschnitt_temp < 30:
			tages_durchschnitt_temp = 0
			letzte_bewaesserung = aktueller_tag
			return True
		else:
			return False

	else:
		return False