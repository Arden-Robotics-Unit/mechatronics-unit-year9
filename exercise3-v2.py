from microbit import *
import maqueenplusv2
from time import sleep_ms

# Initialise the MaqueenPlus robot
# If it's successful, you should see the robot version number (2.1) scroll
# across the Microbit, and it will then show a tick
mq = maqueenplusv2.MaqueenPlusV2()

MOTOR_SPEED = 35
driving = False

while True:
    # Check if button A has been pressed
    if button_a.was_pressed():
        driving = True
        mq.set_underglow(mq.COLOR_GREEN)

    # Check if the logo is being touched
    if pin_logo.is_touched():
        driving = False
        mq.set_underglow(mq.COLOR_RED)
        display.clear()

    L2, L1, M, R1, R2 = mq.line_track()
    display.clear()
    display.set_pixel(0, 0, 9 if R2 else 0)
    display.set_pixel(1, 0, 9 if R1 else 0)
    display.set_pixel(2, 0, 9 if M else 0)
    display.set_pixel(3, 0, 9 if L1 else 0)
    display.set_pixel(4, 0, 9 if L2 else 0)

    if driving:
        all_sensors = (L2, L1, M, R1, R2)
        # In Python you can test tuples directly, eg
        # if all_sensors == (True, True, True, True, True):
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
