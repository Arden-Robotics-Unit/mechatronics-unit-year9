#
# Excercise 1: House Colours
#
# Part 1:
#
# Can you change the loop above to go through the Arden House
# colours (Birnam, Jenolan, Sherwood). You should also show the
# first letter of the house on the Microbit when you display its
# colour. Pause for 1 second after each house.
#
# Note: You can set both headlights at once using mq.HEADLIGHT_BOTH
# as the light.
#
# Part 2:
#
# Change your code so that the house colours only start showing after
# you touch the Microbit logo. And when you press the 'A' button
# they stop showing (all the lights should be off). And if you touch
# the logo again, the colours start showing again.
#
# Note: Look in the reference for "Touch Logo" and "Buttons"
#
# Hint: Try using a Boolean called 'show_houses' to control if the
# house colours are shown.
#


from microbit import *
import maqueenplus
from time import sleep_ms

# Initialise the MaqueenPlus robot
# If it's successful, you should see the robot version number (1.4) scroll
# across the Microbit, and it will then show a tick
mq = maqueenplus.MaqueenPlus(pin1, pin2)

# Controls whether to show the house colours or not
show_houses = False

while True:
    # Check if the logo is being touched
    if pin_logo.is_touched():
        show_houses = True

    # Check if button A has been pressed
    if button_a.was_pressed():
        show_houses = False
        # We need to turn all the lights off
        display.clear()
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_OFF)

    if show_houses:
        # Birnam is Red
        display.show("B")
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_RED)
        sleep_ms(1000)
        # Jenolan is Yellow
        display.show("J")
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_YELLOW)
        sleep_ms(1000)
        # Sherwood is Blue
        display.show("S")
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_BLUE)
        sleep_ms(1000)
