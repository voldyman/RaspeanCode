import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode (GPIO.BOARD)
GPIO.setup (12, GPIO.IN)

count = 0
while True:
	btn = GPIO.input (12)
	if btn == True and last_state == False:
		print "Press number", count
		count += 1
	last_state = btn
