import RPi.GPIO as GPIO # importeer de GPIO bibliotheek.
import time # importeer de 'time' bibliotheek.
import random # importeer de 'random' bibliotheek.

GPIO.setmode(GPIO.BCM) # je kan kiezen tussen BOARD and BCM pin-nummering.
GPIO.setup(20, GPIO.OUT) # geef aan dat pin 20 gebruikt wordt als output (led).
GPIO.setup(16, GPIO.OUT) # geef aan dat pin 16 gebruikt wordt als output (led).
GPIO.setup(12, GPIO.OUT) # geef aan dat pin 12 gebruikt wordt als output (led).

# methode om de volgende willekeurige led te bepalen.
def nextLed():
   i = random.randint(0,2)	# deze methode geeft een willekeurig getal terug tussen de 0 en de 2.
   if i == 0:				# als i gelijk is aan 0 dan :
      return 12				# geef de waarde 12 terug.
   elif i == 1:				# als i gelijk is aan 1 dan :
      return 16				# geef de waarde 16 terug.
   else :					# in alle andere gevallen (dus de waarde is 2) :
      return 20				# geef de waarde 20 terug.
   
# variable voor de tijd tussen aan en uit.
wacht = 0.2

try: 
    while True: # oneindige loop
        led = nextLed() 			# roep de methode om de volgende led te bepalen op.
        GPIO.output(led, GPIO.HIGH) # zet de led (pin van de led) aan.
        time.sleep(wacht)     		# wacht het opgegeven (variable wacht) aantal seconden.
        GPIO.output(led, GPIO.LOW) 	# zet de led (pin van de led) uit.
 
finally: 
    GPIO.cleanup() # De GPIO wordt weer netjes vrijgegeven als het programma wordt afgebroken.
