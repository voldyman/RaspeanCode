import RPi.GPIO as GPIO
from time import sleep
from BeautifulSoup import BeautifulSoup
from requests import get

# ToDo before running this code
# connect a blue led to GPIO pin 11
#
# connect a red led to GPIO pin 12

def get_unread ():
#	print "Fetching Email"
    # change auth to auth = (yourEmailUsername,yourEmailPassword)
	doc = BeautifulSoup(get('https://mail.google.com/mail/feed/atom', auth=('','')).text)
	count = doc.findAll('fullcount')[0]

	return count.contents[0]

def blue_light ():
	GPIO.output (11, True)
	GPIO.output (12, False)

def red_light ():
	GPIO.output (12, True)
	GPIO.output (11, False)

GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
GPIO.setup (12, GPIO.OUT)

while True:
	if get_unread () != '0':
#		print "Unread mail => red"
		red_light()
	else:
#		print "All mail read => blue"
		blue_light ()

