import RPi.GPIO as GPIO
from time import sleep
from urllib import urlencode
import os

GPIO.setmode (GPIO.BOARD)
GPIO.setup (12, GPIO.IN) #button
GPIO.setup (7, GPIO.OUT) #LED

def do_tweet (st):
	st = urlencode({'status':st})
# you can get this command from dev.twitter.com, select the curl command option
	os.system ("""curl --request 'POST' 'https://api.twitter.com/1/statuses/update.json' --data '"""+st+"""' --header 'Authorization: OAuth oauth_consumer_key="xxxxxxxxxxxxxxxxxxxxxx", oauth_nonce="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", oauth_signature="xxxxxxxxxxxxxxxxxxxxxxxxxxxx, oauth_signature_method="HMAC-SHA1", oauth_timestamp="1364024274", oauth_token="xxxxxxxxxxxxxxxxxxxxxxx", oauth_version="1.0"'""")
	print "This is legen"
	blink ()
	print "Wait for it.."
	blink ()
	print "dairy"
	blink ()
	print "^^"

def blink():
	GPIO.output (7, True)
	sleep (0.5)
	GPIO.output (7, False)
	sleep (0.5)

def main():
	last_state = False
	while True:
		btn = GPIO.input (12)
		if btn == True and last_state == False:
			tweet_string = raw_input ("Enter the Tweet:")
			do_tweet (tweet_string)
		
		last_state = btn

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "Ctrl-C pressed"
