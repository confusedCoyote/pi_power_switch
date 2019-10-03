#!/usr/bin/env python

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
import subprocess
import os
import time

GPIO.setwarnings(False)

#---------------------------------------------------------------------------------------

# blinking function
def blinken_light(BCM_pin):
	sleep_time = 0.5 # Seconds between flashes
        GPIO.output(BCM_pin,GPIO.HIGH)
        time.sleep(sleep_time)
        GPIO.output(BCM_pin,GPIO.LOW)
        time.sleep(sleep_time)
        return

#---------------------------------------------------------------------------------------

def blinken_times(number, BCM_pin):
    print('Blinkenlighten for BCM_pin {}' . format(BCM_pin))
    for i in range(0, int(number)):
        blinken_light(BCM_pin)
    return

#---------------------------------------------------------------------------------------

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel for ON, AMBER, LED
GPIO.setup(4, GPIO.OUT) # PIN 7 on board (GND to 9)
# blink GPIO4 3 times
blinken_times(3, 4)

#Turn on the POWER ON, GREEN, LED & leave it on
GPIO.setup(27, GPIO.OUT)   # PIN 13 on board (GND to 14)
GPIO.output(27, GPIO.HIGH) # and turn the fecker on

GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP) # PIN 5 on board (GND to 6)
# Wait for the power button to be pressed
GPIO.wait_for_edge(3, GPIO.FALLING)

# Display image before shutdown happens
image_view = '/usr/bin/fbi -T 2 -once -t 5 -noverbose -a /root/winners-dont-use-drugs.png'
os.system(image_view)

# set up GPIO output channel for SHUTDOWN, RED, LED
GPIO.setup(24, GPIO.OUT) # PIN 18 on board (GND to 20)
# blink GPIO24 5 times
blinken_times(5, 24)
GPIO.cleanup()

# Shut us down!
subprocess.call(['shutdown', '-h', 'now'], shell=False)
