# beaglebone-push-buttons
Bypass Python's serial processing with two processes controlling a pushbutton
Python is serial in nature. Even additions like asyncio are limited somehow.
So why not use good old Linux multiprocessing to fire up sub processes that will do the job?
In this example I chose deliberately a "blocking" logic so the subprocess is going to evacuate
the CPU and clear the way for other procecesses (I.e. main).
One will note that even that you press the push button for short time, the relevant process prints several lines.
There is a possibility to overcome this, I leave for the programmer to find.
