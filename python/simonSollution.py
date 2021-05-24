##########################################################################################
## Simon says (game)
## Dit is een oplossing / implementatie van het spel.
##########################################################################################
import RPi.GPIO as GPIO # importeer de GPIO bibliotheek.
import time # importeer de 'time' bibliotheek.
import random # Import 'random' bibliotheek

# Constanten declaratie
leds =    [20,16,12,7]  # array met pinnummers van de leds
buttons = [21,6,13,19]  # array met pinnummers van de buttons
aantal = len(leds)      # totaal aantal buttons en leds
wacht = 0.5	            # de tijd in seconden tussen een led aan en uit.

# Setup
GPIO.setmode(GPIO.BCM) # je kan kiezen tussen BOARD and BCM pin-nummering.
for pin in leds: GPIO.setup(pin, GPIO.OUT) ## Setup the leds to OUT(PUT)
for pin in buttons: GPIO.setup(pin, GPIO.IN)  ## Setup the buttons to IN(PUT)
      
# Methode om alle leds een x aantal keer te laten knipperen
def blinkAll(times):
   for x in range(0,times):
      for pin in leds: GPIO.output(pin, GPIO.HIGH)
      time.sleep(wacht)
      for pin in leds: GPIO.output(pin, GPIO.LOW)
      time.sleep(wacht)

# Methode om een led 1x te laten knipperen
# Color is gelijkt aan de index van de array: 0 ..3
def blink(color):
   GPIO.output(leds[color], GPIO.HIGH)
   time.sleep(wacht)
   GPIO.output(leds[color], GPIO.LOW)
   time.sleep(wacht)

# GAME START
blinkAll(1)
print "Het spel is begonnen, herhaal de steeds langer wordende reeks. Succes!"
sequence = []   # sequence van type colors (= led pins)
gameOn = True

# GAME LOOP
while gameOn:
   # voeg een willekeurige led (kleur) toe aan de sequence (0, 1, 2 of 3)
   sequence.append(random.randint(0,aantal-1))
   
   ## speel de sequence af
   for color in sequence : blink(color)

   # Luister naar de buttons, de speler herhaalt de sequence
   position = 0
   while (position < len(sequence) and gameOn):
      for i in range(0,aantal):
         if GPIO.input(buttons[i]):
            blink(i) # zet de gekozen led aan en uit 
            gameOn = sequence[position] == i # controleer de gekozen button
            position += 1 # ga naar de volgende positie van de sequence
      time.sleep(0.1) # een vertraging voor de button debounce (minder gevoelig).

# GAME END
blinkAll(3)
print "Game over!"
print "Score: ", len(sequence)-1
GPIO.cleanup() ## clean up all the ports that were used
 