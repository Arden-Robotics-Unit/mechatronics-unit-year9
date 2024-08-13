from microbit import *
import maqueenplus
from time import sleep_ms

# Initialise the MaqueenPlus robot
# If it's successful, you should see the robot version number (1.4) scroll
# across the Microbit, and it will then show a tick
mq = maqueenplus.MaqueenPlus(pin1, pin2)

# Show 'A' for Australia!
display.show("A")

# Loop through the Aussie colours. Aussie Aussie Aussie!
while True:
    mq.set_headlight_rgb(mq.HEADLIGHT_LEFT, mq.COLOR_GREEN)
    mq.set_headlight_rgb(mq.HEADLIGHT_RIGHT, mq.COLOR_YELLOW)
    sleep_ms(1000)
    mq.set_headlight_rgb(mq.HEADLIGHT_LEFT, mq.COLOR_YELLOW)
    mq.set_headlight_rgb(mq.HEADLIGHT_RIGHT, mq.COLOR_GREEN)
    sleep_ms(1000)

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
# Advanced:
#
# Your code probably takes up to 3 seconds to respond to the press of
# button A - that is, it goes through all three houses before it stops.
# Can you improve the responsiveness so it will respond within 1 second,
# that is, stop after the current house?
#
# Can you improve it to be better than 1 second?
#
