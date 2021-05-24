import RPi.GPIO as GPIO # importeer de GPIO bibliotheek.
import time # importeer de 'time' bibliotheek.

GPIO.setmode(GPIO.BCM) # je kan kiezen tussen BOARD and BCM pin-nummering.
GPIO.setup(20, GPIO.OUT) # geef aan dat pin 20 gebruikt wordt als output (led).
GPIO.setup(16, GPIO.OUT) # geef aan dat pin 16 gebruikt wordt als output (led).
GPIO.setup(12, GPIO.OUT) # geef aan dat pin 12 gebruikt wordt als output (led).
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # geef aan dat pin 21 gebruikt wordt als input (button).

# variabelen.
led = 12
prevState = 0

# Methode om de volgende led te bepalen.
def nextLed(prevLed):
   if (prevLed == 20) : newLed = 16 # als de vorige led(pin) 20 was dan wordt de nieuwe led(pin) 16.
   if (prevLed == 16) : newLed = 12	# als de vorige led(pin) 16 was dan wordt de nieuwe led(pin) 12.
   if (prevLed == 12) : newLed = 20	# als de vorige led(pin) 12 was dan wordt de nieuwe led(pin) 20.
   return newLed

try: 
    while True: # oneindige loop
        if  GPIO.input(21) and (prevState == 0) :  	# als de button is ingegdrukt (pin 21 is hoog) en de vorige state is gelijk aan 0 dan:
            print "Button is ingedrukt" 			# druk deze tekst af
            led = nextLed(led)						# roep de methode om de volgende led te bepalen en ken deze waarde toe aan variabele led.
            GPIO.output(led, GPIO.HIGH) 			# zet voltage op de led(pin) zodat de led aan gaat.
            prevState = 1							# geeef de variabele prevState de waarde 1.
        if  (not GPIO.input(21)) and (prevState == 1): # als de button niet is ingegdrukt (pin 21 is laag) en de vorige state is gelijk aan 1 dan:
            GPIO.output(20, GPIO.LOW)				# zet geen voltage op de led(pin) 20 zodat de led uit gaat (als die nog niet uit was).
            GPIO.output(16, GPIO.LOW)				# zet geen voltage op de led(pin) 16 zodat de led uit gaat (als die nog niet uit was).
            GPIO.output(12, GPIO.LOW) 				# zet geen voltage op de led(pin) 12 zodat de led uit gaat (als die nog niet uit was).
            prevState = 0							# geeef de variabele prevState de waarde 0.
        time.sleep(0.1) # een vertraging om kans op debouncing van de button tegen te gaan (een state tussen aan en uit).
 
finally: 
    GPIO.cleanup() # De GPIO wordt weer netjes vrijgegeven als het programma wordt afgebroken.
