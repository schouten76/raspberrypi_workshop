import RPi.GPIO as GPIO # importeer de GPIO bibliotheek.
import time # importeer de 'time' bibliotheek.

GPIO.setmode(GPIO.BCM) # je kan kiezen tussen BOARD and BCM pin-nummering.
GPIO.setup(20, GPIO.OUT) # geef aan aan dat pin 20 gebruikt wordt als output (led).
GPIO.setup(21, GPIO.IN)  # geef aan dat pin 21 gebruikt wordt als input (button).
 
try: 
    while True: # oneindige loop
        if GPIO.input(21): 				# als pin 21 hoog is dan:
            print "Button is on" 		# print tekst.
            GPIO.output(20, GPIO.HIGH) 	# zet voltage op de led(pin) zodat de led aan gaat.
        else: 							# anders (dus pin 21 is laag):
            GPIO.output(20, GPIO.LOW) 	# zet geen voltage op de led(pin) zodat de led uit gaat.
        time.sleep(0.1) # een vertraging om kans op debouncing van de button tegen te gaan (een state tussen aan en uit).
 
finally: 
    GPIO.cleanup() # De GPIO wordt weer netjes vrijgegeven als het programma wordt afgebroken.
