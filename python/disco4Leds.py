import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import random ## Import 'random' library.

leds = [20,16,12, 13]

GPIO.setmode(GPIO.BCM) ## you can choose between BOARD and BCM
for pin in leds:GPIO.setup(pin, GPIO.OUT) ## Setup the leds to OUT(PUT)

wacht = 0.2

try: 
    while True: ## infinite loop
        led = leds[random.randint(0,3)] 
        GPIO.output(led, GPIO.HIGH) 
        time.sleep(wacht)     
        GPIO.output(led, GPIO.LOW)
 
finally: 
    GPIO.cleanup() ## clean up all the ports that were used
