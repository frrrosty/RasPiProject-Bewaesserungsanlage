# RasPiProject_Bewaesserungsanlage
Dies ist ein Projekt, welches von Studierenden im Masterstudiengang Fachdidaktik - Medien und Informatik erstellt wurde. 
Die Module der Sensoren und Aktoren wurden aus der Datenbank von GroovePi angepasst. Der Code wird hier im laufenden Prozess 
angepasst. Zusätzlich zum hier bereitgestellten Code wird die GrovePi Bibliothek benötigt, welche auf GitHub verfügbar ist.

Folgende Hardware wurde verwendet:
- Raspberry Pi Model 3b+
- GrovePi+, Seeed Studio
- Grove Moisture Sensor
- Grove Temperature&Humidity Sensor Pro
- Grove SPDT Relay(30A)
- Grove Ultrasonic Ranger
- 230V Tauchpumpe (Landi)

Weiter wurde folgendes Material verwendet:
- 60 Liter Regentonne (Coop Bau und Hobby)
- 3 Meter Schlauch, passend zur Tauchpumpe (Coop Bau und Hobby)
- Schrumpfschlauch
- Klingeldrat
- Isolierband
- 230V Verlängerungskabel
- Teilmchr3 (3D-Druck der Gehäuse)
- Gehäuse für Relay und RaspberryPi (https://www.thingiverse.com/thing:3620389)
- Mehrfachstecker

Die Anschlüsse, welche für das Programm verwendet wurden sind dem Code zu entnehmen.

- moisture_sensor                         = Analog Port 0
- Temperatur und Luftfeuchigkeitssensor   = Digital Port 3
- Relais                                  = Digital Port 2
- Ultrasonic Ranger                       = Digital Port 4

Längen von Kabel und Schläuchen müssen auf die Gegebenheiten angepasst werden. Der "Ultrasonic Ranger" wurde mit Klebeband direkt am Deckel des Fasses befestigt. Eine Funktion gibt den Wert als Distanz zum Wasser aus, eine zweite Funktion gibt den Füllstand in Prozent angegeben aus. Die Werte müssen an die höhe des Verweddeten Fasses angepasst werden.

Der Code wurde in verschiedene Module unterteilt, welche an die eigenen Bedürfnisse angepasst werden können. Gundsätzlich wird das Programm über den "main_code" gesteuert. Eines der Zentralen Programme ist die Definition "traenken". Diese Steuert die Bewässerung. Das Programm kann auch nur mit dieser Funktion genutzt werden, wenn keine Sensoren verbaut werden. Somit würde nur der Aktor "Relais" benötigt werden. 

Die Funktionen "day_average" und "day_checker" sind zur steuereung, ob es sich um einen Tag zum tränken handelt. Diese müssen auf die eigenen Bedürfnisse angepasst werden, hier wurde folgende logik verwendet:

- Wenn der Tagesdurchschnitt der Temperatur über 30°C liegt soll getränkt werden
- Wenn der Tagesdurchschnitt der Temperatur zwischen 25°C und 30°C liegt soll an jedem 2. Tag getränkt werden
- Wenn es Freitag ist und nicht am Vortag getränkt wurde, soll getränkt werden

Das ganze Projekt befindet sich noch in der Testphase. 
