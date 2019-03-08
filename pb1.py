#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time
import signal
import sys

def signal_handler(signal, frame):
	print ('Ctrl+C pressed, process exit')
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

GPIO.setup("P8_10", GPIO.IN)
GPIO.cleanup()

print('push button 1 subprocess active')

# Raise an event for P8_10
#GPIO.add_event_detect("P8_10", GPIO.RISING)

while True:
	
	GPIO.wait_for_edge("P8_10", GPIO.RISING)
	if GPIO.input("P8_10"):
		print("Button P8_10 was pressed")
	else:
		continue
	#if GPIO.event_detected("P8_10"):
	#	print('Push Button "P8_10" IS pressed')
	#time.sleep(1)


