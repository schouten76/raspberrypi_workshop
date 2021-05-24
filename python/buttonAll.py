import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

leds = [20,16,12, 13];
buttons = [21,26,19,6];

GPIO.setmode(GPIO.BCM) ## you can choose between BOARD and BCM
for pin in leds: GPIO.setup(pin, GPIO.OUT) ## Setup the led to OUT(PUT)
for pin in buttons: GPIO.setup(pin, GPIO.IN)  ## Setup the button to IN(PUT)
 
try: 
    while True: ## infinite loop
        if GPIO.input(buttons[0]):  
            GPIO.output(leds[0], GPIO.HIGH) 
        elif GPIO.input(buttons[1]):
			GPIO.output(leds[1], GPIO.HIGH)
        elif GPIO.input(buttons[2]):
            GPIO.output(leds[2], GPIO.HIGH)
        elif GPIO.input(buttons[3]):
            GPIO.output(leds[3], GPIO.HIGH)
	else: 
        for pin in leds: GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1) ## een vertraging voor de button om kans op debouncing tegen te gaan (een state tussen aan en uit).
 
finally: 
    GPIO.cleanup() ## clean up all the ports that were used
