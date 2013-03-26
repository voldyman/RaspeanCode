#!/usr/bin/python

import sys
import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode (GPIO.BOARD)
GPIO.setup (12, GPIO.IN)

while True:
	btn = GPIO.input (12)
	if btn == True:
		print "Pressed"
	sleep(0.5)
	
