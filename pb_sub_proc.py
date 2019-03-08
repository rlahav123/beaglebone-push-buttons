#!/usr/bin/python3

#import os
import subprocess
import time
import signal
import sys

def signal_handler(signal, frame):
	print ('Ctrl+C pressed, main exiting')
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)






print('PB1 about to be fired')
p1 = subprocess.Popen(["/media/microsd/bbb/py/pb1.py"], shell=True)
time.sleep(1)
print (p1.pid)
#pid1 = os.fork()
#if pid1==0:
#	os.system("nohup /usr/bin/python3 /media/microsd/bbb/py/pb1.py")
#	exit() 

print('PB2 about to be fired')
p2 = subprocess.Popen(["/media/microsd/bbb/py/pb2.py"], shell=True)
time.sleep(1)
print (p2.pid)
#pid2 = os.fork()
#if pid2==0:
#	os.system("nohup /usr/bin/python3 /media/microsd/bbb/py/pb2.py")
#	exit()

    
while (p1.poll() and p2.poll) is None:
	print('the two processes are running')
	time.sleep(5)


