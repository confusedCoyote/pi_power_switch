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
ON_LIGHT_BCM = 27
OFF_LIGHT_BCM = 24
BOOT_LIGHT_BCM = 4

# -----------------------------------------------------------------------------


# blinking function
def blinken_light(BCM_pin):
    sleep_time = 0.5  # Seconds between flashes
    GPIO.output(BCM_pin, GPIO.HIGH)
    time.sleep(sleep_time)
    GPIO.output(BCM_pin, GPIO.LOW)
    time.sleep(sleep_time)
    return

# -----------------------------------------------------------------------------


def blinken_times(number, BCM_pin):
    print('Blinkenlighten for BCM_pin {}' . format(BCM_pin))
    for i in range(0, int(number)):
        blinken_light(BCM_pin)
    return

# -----------------------------------------------------------------------------


# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel for ON, AMBER, LED
GPIO.setup(BOOT_LIGHT_BCM, GPIO.OUT)  # PIN 7 on board (GND to 9)
# blink GPIO4 3 times
blinken_times(3, BOOT_LIGHT_BCM)

# Turn on the POWER ON, GREEN, LED & leave it on
GPIO.setup(ON_LIGHT_BCM, GPIO.OUT)    # PIN 13 on board (GND to 14)
GPIO.output(ON_LIGHT_BCM, GPIO.HIGH)  # and turn the fecker on

GPIO.setup(POWER_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# PIN 5 on board (GND to 6)
# Wait for the power button to be pressed
GPIO.wait_for_edge(POWER_BUTTON, GPIO.FALLING)

# Display image before shutdown happens
image_view = '/usr/bin/fbi -T 2 -once -t 5 -noverbose'
image_view += ' -a /root/winners-dont-use-drugs.png'
os.system(image_view)

# set up GPIO output channel for SHUTDOWN, RED, LED
GPIO.setup(OFF_LIGHT_BCM, GPIO.OUT)  # PIN 18 on board (GND to 20)
# blink GPIO24 5 times
blinken_times(5, OFF_LIGHT_BCM)
GPIO.cleanup()

# Shut us down!
subprocess.call(['shutdown', '-h', 'now'], shell=False)
