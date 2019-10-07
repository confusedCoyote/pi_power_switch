#!/usr/bin/env python

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!")
    print("This is probably because you need superuser privileges.")
    print("You can achieve this by using 'sudo' to run your script")
import subprocess
import os
import time

GPIO.setwarnings(False)

# --STATIC-GLOBAL-VARIABLES----------------------------------------------------


POWER_BUTTON = 3
RED_BCM = 4
GREEN_BCM = 17
BLUE_BCM = 27
SLEEP_TIME = 0.5  # Seconds between flashes

# -----------------------------------------------------------------------------


# blinking function
def blinken_light(BCM_pin):
    GPIO.output(BCM_pin, GPIO.HIGH)
    time.sleep(SLEEP_TIME)
    GPIO.output(BCM_pin, GPIO.LOW)
    time.sleep(SLEEP_TIME)
    return

# -----------------------------------------------------------------------------


def blinken_times(number, BCM_pin):
    print('Blinkenlighten for BCM_pin {}' . format(BCM_pin))
    for i in range(0, int(number)):
        blinken_light(BCM_pin)
    return

# -----------------------------------------------------------------------------


GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,0)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)

try:
    while (True):
        request = raw_input(“RGB—>”)
        if (len(request) == 3):
            GPIO.output(RED,int(request[0]))
            GPIO.output(GREEN,int(request[1]))
            GPIO.output(BLUE,int(request[2]))

except KeyboardInterrupt:
    GPIO.cleanup()

# to use Raspberry Pi board pin numbers
##GPIO.setmode(GPIO.BCM)

##GPIO.setup(POWER_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# PIN 5 on board (GND to 6)
# Wait for the power button to be pressed
##GPIO.wait_for_edge(POWER_BUTTON, GPIO.FALLING)

# Display image before shutdown happens
##image_view = '/usr/bin/fbi -T 2 -once -t 5 -noverbose'
##image_view += ' -a /root/winners-dont-use-drugs.png'
##os.system(image_view)

# set up GPIO output channel for SHUTDOWN, RED, LED
##GPIO.cleanup()

# Shut us down!
##subprocess.call(['shutdown', '-h', 'now'], shell=False)
