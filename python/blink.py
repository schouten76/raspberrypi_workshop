import RPi.GPIO as GPIO # importeer de GPIO bibliotheek.
import time # importeer de 'time' bibliotheek.

GPIO.setmode(GPIO.BCM) # je kan kiezen tussen BOARD and BCM pin-nummering.
GPIO.setup(20, GPIO.OUT) # geef aan dat pin 20 een output is (led).

# variable voor de tijd tussen aan en uit.
wacht = 0.5

print "begin met 10x kipperen"	# druk de tekst af.
for x in range(10):				# loop: doorloop x, waarbij x van 1 tot 10 loopt.
    GPIO.output(20,GPIO.HIGH)	# zet voltage op de led(pin) zodat de led aan gaat.
    time.sleep(wacht)			# wacht het opgegeven (variable wacht) aantal seconden.
    GPIO.output(20,GPIO.LOW)	# zet geen voltage op de led(pin) zodat de led uit gaat.
    time.sleep(wacht)			# wacht het opgegeven (variable wacht) aantal seconden.

print "einde"	# druk de tekst af.
GPIO.cleanup() 	# De GPIO wordt weer netjes vrijgegeven als het programma wordt afgebroken.