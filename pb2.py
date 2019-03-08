#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time
import signal
import sys

def signal_handler(signal, frame):
	print ('Ctrl+C pressed, process exit')
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

GPIO.setup("P8_11", GPIO.IN)
GPIO.cleanup()

print('push button 2 subprocess active')

# Raise an event for P8_10
#GPIO.add_event_detect("P8_11", GPIO.RISING)
    
while True:
	
	GPIO.wait_for_edge("P8_11", GPIO.RISING)
	if GPIO.input("P8_11"):
		print("Button P8_11 was pressed")
	else:
		continue
	#if GPIO.event_detected("P8_11"):
	#	print('Push Button "P8_11" IS pressed')
	#time.sleep(1)


