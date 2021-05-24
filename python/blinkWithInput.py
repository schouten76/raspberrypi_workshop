import RPi.GPIO as GPIO # importeer de GPIO bibliotheek.
import time # importeer de 'time' bibliotheek.

GPIO.setmode(GPIO.BCM) # je kan kiezen tussen BOARD and BCM pin-nummering.
GPIO.setup(20, GPIO.OUT) # geef aan dat pin 20 een output is (led).

##Definieer een functie genaamd Blink()
def Blink(numTimes,speed):
   try:
      for i in range(0,numTimes): 
         print "Iteration "+ str(i +1)
         GPIO.output(20,True)
         time.sleep(speed)
         GPIO.output(20,False)
         time.sleep(speed)
      print "Done"
   finally:   # voer uit indien het programma wordt afgebroken
      GPIO.cleanup() # De GPIO wordt weer netjes vrijgegeven als het programma wordt afgebroken.

iterations = raw_input("Enter total number of times to blink: ")
speed = raw_input("Enter length of each blink(seconds): ")

Blink(int(iterations), float(speed))