# Wasserstand messen

from grovepi import *

def wasserstand():
 ultrasonic_ranger = 4
 distanz = ultrasonicRead(ultrasonic_ranger)

 print(distanz)

 if distanz < 5:
  print("Das Fass ist voll")
 elif distanz < 20:
  print("Das Fass ist halb voll")
 elif distanz < 50:
  print("Das Fass ist leer")
 elif distanz > 50:
  print("Es besteht ein Fehler mit dem Sensor!")

wasserstand()