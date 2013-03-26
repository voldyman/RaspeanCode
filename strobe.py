import RPi.GPIO as GPIO
from time import sleep
import sys

def main():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT)

	while (True):
		GPIO.output(7,True)
		sleep (float(sys.argv[1]))
		GPIO.output (7, False)
		sleep(float(sys.argv[1]))

try:
	main()
except KeyboardInterrupt:
	GPIO.output(7,False)
