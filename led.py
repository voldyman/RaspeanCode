import RPi.GPIO as GPIO
import sys

GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
if sys.argv[1] == "on":
	GPIO.output (11, True)
elif sys.argv[1] == "off":
	GPIO.output (11, False)

