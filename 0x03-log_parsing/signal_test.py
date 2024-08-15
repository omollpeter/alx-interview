#!/usr/bin/python3

import signal
import sys
import time

def signal_handler(sig, frame):
    print("\nKeyboard interrupt received. Exiting gracefully")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print("Press CTRL + C tro interrupt")

while True:
    try:
        time.sleep(1)
        print("Working")
    except KeyboardInterrupt:
        print("Keyboard interrupt detected")
        sys.exit()
