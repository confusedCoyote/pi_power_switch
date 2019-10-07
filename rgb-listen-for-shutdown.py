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
GPIO.setmode(GPIO.BCM)

# --STATIC-GLOBAL-VARIABLES----------------------------------------------------


POWER_BUTTON = 3
RED_BCM = 4
GREEN_BCM = 17
BLUE_BCM = 27
SLEEP_TIME = 0.5  # Seconds between flashes


# -----------------------------------------------------------------------------

# Make the 3 pins active
GPIO.setup(RED_BCM, GPIO.OUT)
GPIO.setup(GREEN_BCM, GPIO.OUT)
GPIO.setup(BLUE_BCM, GPIO.OUT)

p_R = GPIO.PWM(RED_BCM, 2000)  # set Frequece to 2KHz
p_G = GPIO.PWM(GREEN_BCM, 2000)
p_B = GPIO.PWM(BLUE_BCM, 5000)

p_R.start(0)      # Initial duty Cycle = 0(leds off)
p_G.start(0)
p_B.start(0)


# -----------------------------------------------------------------------------


def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

   
# -----------------------------------------------------------------------------


def set_color(col):   # For example : col = 0x112233
	R_val = (col & 0xFF0000) >> 16
	G_val = (col & 0x00FF00) >> 8
	B_val = (col & 0x0000FF) >> 0
	
	R_val = map(R_val, 0, 255, 0, 100)
	G_val = map(G_val, 0, 255, 0, 100)
	B_val = map(B_val, 0, 255, 0, 100)
	
	p_R.ChangeDutyCycle(R_val)     # Change duty cycle
	p_G.ChangeDutyCycle(G_val)
	p_B.ChangeDutyCycle(B_val)

   
# -----------------------------------------------------------------------------


def blink_light(loop_number, col) :

    print('Blinkenlighten for colour {} looping  {} times' . format(col, loop_number))
    for i in range(0, int(loop_number)):
        set_color(col)
        time.sleep(SLEEP_TIME)
        set_color(0x000000)
        time.sleep(SLEEP_TIME)
    return


# -----------------------------------------------------------------------------


blink_light(3, 0xFFFF00)

set_color(0x00FF00)

GPIO.setup(POWER_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# PIN 5 on board (GND to 6)
# Wait for the power button to be pressed
GPIO.wait_for_edge(POWER_BUTTON, GPIO.FALLING)

blink_light(5, 0xFF0000)

# Display image before shutdown happens
image_view = '/usr/bin/fbi -T 2 -once -t 5 -noverbose'
image_view += ' -a /root/winners-dont-use-drugs.png'
os.system(image_view)

# set up GPIO output channel for SHUTDOWN, RED, LED

GPIO.cleanup()

# Shut us down!
subprocess.call(['shutdown', '-h', 'now'], shell=False)
