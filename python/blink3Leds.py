import RPi.GPIO as GPIO # importeer de GPIO bibliotheek.
import time # importeer de 'time' bibliotheek.

GPIO.setmode(GPIO.BCM) # je kan kiezen tussen BOARD and BCM pin-nummering.
GPIO.setup(20, GPIO.OUT) # geef aan dat pin 20 een output is (led).
GPIO.setup(16, GPIO.OUT) # geef aan dat pin 16 een output is (led).
GPIO.setup(12, GPIO.OUT) # geef aan dat pin 12 een output is (led).

print "Eerste led"
GPIO.output(20,True)
time.sleep(2)
GPIO.output(20,False)
time.sleep(2)
print "tweede led"
GPIO.output(16,True)
time.sleep(2)
GPIO.output(16,False)
time.sleep(2)
print "derde led"
GPIO.output(12,True)
time.sleep(2)
print "klaar!"
GPIO.cleanup() # De GPIO wordt weer netjes vrijgegeven als het programma wordt afgebroken.

