import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN) #button
GPIO.setup(7, GPIO.OUT)#led

def blink ():
	GPIO.output (7, True)
	sleep (0.5)
	GPIO.output (7, False)
	sleep (0.5)

def btn_pressed ():
	blink()
	blink()

last_state = False

while True:
	btn = GPIO.input(12)
	if btn == True and last_state == False:
		btn_pressed()
		print "Btn Pressed"
	last_state = btn

	
