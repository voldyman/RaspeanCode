import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
GPIO.setup (12, GPIO.OUT)
GPIO.setup (7, GPIO.OUT)

while True:
	GPIO.output (7, True)
	
	GPIO.output (11, True)
	GPIO.output (12, False)
	sleep (3)
	GPIO.output (11, False)
	GPIO.output (12, True)
	sleep (3)
