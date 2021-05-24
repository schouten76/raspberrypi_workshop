import RPi.GPIO as GPIO # importeer de GPIO bibliotheek.
import time # importeer de 'time' bibliotheek.

GPIO.setmode(GPIO.BCM) # je kan kiezen tussen BOARD and BCM pin-nummering.
GPIO.setup(20, GPIO.OUT) # geef aan aan dat pin 20 gebruikt wordt als output (led).
GPIO.setup(21, GPIO.IN)  # geef aan dat pin 21 gebruikt wordt als input (button).
 
try: 
    prevButtonState = False
	ledAanUit = False
    while True: # oneindige loop
        if GPIO.input(21) and prevButtonState == False: 				# als pin 21 hoog is dan:
            ledAanUit = !ledAanUit
            GPIO.output(20, ledAanUit) 	# zet voltage op de led(pin) zodat de led aan gaat.
        time.sleep(0.1) # een vertraging om kans op debouncing van de button tegen te gaan (een state tussen aan en uit).
        prevButtonState = GPIO.input(21)
finally: 
    GPIO.cleanup() # De GPIO wordt weer netjes vrijgegeven als het programma wordt afgebroken.
