from microbit import *
import maqueenplus
from time import sleep_ms

# Initialise the MaqueenPlus robot
# If it's successful, you should see the robot version number (1.4) scroll
# across the Microbit, and it will then show a tick
#
# Check the pins that you have your ultrasonic sensor plugged into.
# Change the pins below if you need to
mq = maqueenplus.MaqueenPlus(pin1, pin2)

MOTOR_SPEED = 35
driving = False

while True:
    # Check if button A has been pressed
    if button_a.was_pressed():
        driving = True
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_GREEN)

    # Check if the logo is being touched
    if pin_logo.is_touched():
        driving = False
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_RED)
        display.clear()

    L3, L2, L1, R1, R2, R3 = mq.line_track()

    if driving:
        all_sensors = (L3, L2, L1, R1, R2, R3)
        # In Python you can test tuples directly, eg
        # if all_sensors == (True, True, True, True, True, True):
        #     do_something()

#
# Exercise 3: Line Tracking
#
# Part 1:
#
# Make the robot follow a straight line. Figure out what sensors should
# be True or False to able to drive straight ahead. Stop the robot if
# it moves off the path.
#
# Now implement turning to keep the robot on the line if it moves off.
# To turn you need to have the wheels moving at different speeds. They
# can both still be moving forwards, or one could    be stopped, or one
# could be moving backwards. What method works best?
#
# Part 2:
#
# What happens if you increase MOTOR_SPEED? Can you vary the speed
# depending on what the robot is doing (straight, turning, etc)?
#
# Advanced:
#
# Make the robot track a line that has a 90 degree turn on it.
#
