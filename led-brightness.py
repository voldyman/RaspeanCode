import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN) #button
GPIO.setup(7, GPIO.OUT)#led

def blink (intent):
	for x in range(1,500):
		GPIO.output (7, True)
		sleep (0.0008 * intent)
		GPIO.output (7, False)
		sleep (0.003 - 0.0001 * intent)

def btn_pressed ():
	print "level 1"
	blink(1)
	print "level 2"
	blink(2)
	print "level 3"
	blink(3)

last_state = False

while True:
	btn = GPIO.input(12)
	if btn == True and last_state == False:
		btn_pressed()
		print "Btn Pressed"
	last_state = btn

	
