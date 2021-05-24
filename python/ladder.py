##########################################################################################
## Ladder Game
## Het doel van dit spel is om de knop in te drukken als de led aan is
## Als dat lukt dan gaat de volgende led (trap trede) knipperen, maar dan iets sneller.
## Als je mist (de led is op dat moment uit) dan ga je een level (trap trede) omlaag.
## Kan jij het einde van de ladder bereiken?
##########################################################################################
import RPi.GPIO as GPIO # Import GPIO library
import time             # Import 'time' library.
import random           # Import 'random' library

# variabelen
led1 = 20               # het pinnummer van led 1
led2 = 16               # het pinnummer van led 2
led3 = 12               # het pinnummer van led 3
button = 21             # het pinnummer van de button
level = 1               # start met level 1, er zijn 3 levels (3 leds)
gameOn = True           # zolang deze waar (True) is, loopt het spel
ledOn = True            # begin met de led aan
mode = 1		        # game mode (1 = ritmisch, anders willekeurig)  
prevButtonState = False # bewaar de vorige button state (True, dan was deze ingedrukt)

# Setup
GPIO.setmode(GPIO.BCM)      # gebruik de broadcom pin nummering
GPIO.setup(led1, GPIO.OUT)  # geef aan dat pin 20 gebruikt wordt als output (led)
GPIO.setup(led2, GPIO.OUT)  # geef aan dat pin 16 gebruikt wordt als output (led)
GPIO.setup(led3, GPIO.OUT)  # geef aan dat pin 12 gebruikt wordt als output (led)
GPIO.setup(button, GPIO.IN) # geef aan dat pin 21 gebruikt wordt als input (button)

# initialisatie
GPIO.output(led1, GPIO.LOW) # zet de led uit bij begin van het spel
GPIO.output(led2, GPIO.LOW) # zet de led uit bij begin van het spel
GPIO.output(led3, GPIO.LOW) # zet de led uit bij begin van het spel

# Methode om de led te bepalen aan de hand van het huidige level
def getLed(level):
   if level == 1 : return led1
   if level == 2 : return led2
   if level == 3 : return led3

# Methode om de tijd dat de led aan of uit gaat te bepalen (moeilijkheid)
# bij iedere cycle wordt geluisterd of op de knop is gedrukt
# iedere cycle duurt 0.1 seconden
def getCycles(level):
   if level == 1 : cycles = 10
   if level == 2 : cycles = 5
   if level == 3 : cycles = 2
   return cycles

# Methode om het volgende level te bepalen (promotie of degradatie)
def nextLevel(promotie):
   global level
   global gameOn
   newLevel = level
   if level == 1:
      if promotie:
         newLevel = 2 # een level omhoog
         print("Raak, -> niveau 2")
      else:
         gameOn = False # verloren (spel wordt beeindigd)
         print("Mis, game over :(")
   if level == 2:
      if promotie:
         newLevel = 3 # een level omhoog
         print("Raak, -> niveau 3")
      else:
         newLevel = 1 # een level omlaag
         print("Mis, <- niveau 1")
   if level == 3:
      if promotie:
         gameOn = False # gewonnen (spel wordt beeindigd)
         print("Raak, -> Gewonnen!")
      else:
         newLevel = 2 # een level omlaag
         print("Mis, <- niveau 2")
   level = newLevel
   
# Methode om te bepalen of de led aan of uit moet (radom)
def getLedOn():
   global ledOn
   global mode
   if (mode == 1): return not ledOn 
   else:
      if random.randint(0,1) == 1:
         return True
      else: 
         return False

def isButtonPressed():
   global prevButtonState
   global button
   result = False
   buttonState = GPIO.input(button)
   if buttonState !=  prevButtonState:
      if buttonState == True:
         result = True	  
   prevButtonState = buttonState
   return result
	
try: # hierdoor kan je het spel netjes beeindigen met CTRL + C (zie finally)
    while gameOn: # GAME LOOP, blijf het spel uitvoeren totdat het spel gewonnen of verloren is
        maxCycles = getCycles(level) # bepaal het aantal cycles voor dit level (snelheid van de leds)
        goCycles = True # dit geeft aan of de cycles doorlopen moeten worden, geeft de mogelijkheid uit de cycles te stappen na button press.
        cycle = 0 # begin weer bij 0

        led = getLed(level) # bepaal de led voor dit level
        ledOn = getLedOn() 
        
        GPIO.output(led, ledOn) # zet de led aan of uit
        while cycle < maxCycles and goCycles:  # Loop door de cycles heen
           if isButtonPressed(): # de knop is ingedrukt, en hiervoor nog niet (voorkomt dat je de knop ingedrukt kan houden
              nextLevel(ledOn) # Promomtie of degratatie
              goCycles = False # stop door de cycles te lopen, en begin met nieuw level   
           cycle = cycle + 1 # volgende cycle
           time.sleep(0.1) # wacht even voor de volgende cycles (dit bepaalt de tijd per cycle)

finally: 
    GPIO.cleanup() ## De GPIO wordt weer netjes vrijgegeven als het programma wordt afgebroken
