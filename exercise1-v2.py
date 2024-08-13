from microbit import *
import maqueenplusv2
from time import sleep_ms

# Initialise the MaqueenPlus robot
# If it's successful, you should see the robot version number (2.1) scroll
# across the Microbit, and it will then show a tick
mq = maqueenplusv2.MaqueenPlusV2()

# Show 'A' for Australia!
display.show("A")

# Loop through the Aussie colours. Aussie Aussie Aussie!
while True:
    mq.set_underglow_light(0, mq.COLOR_GREEN)
    mq.set_underglow_light(1, mq.COLOR_GREEN)
    mq.set_underglow_light(2, mq.COLOR_YELLOW)
    mq.set_underglow_light(3, mq.COLOR_YELLOW)
    sleep_ms(1000)
    mq.set_underglow_light(0, mq.COLOR_YELLOW)
    mq.set_underglow_light(1, mq.COLOR_YELLOW)
    mq.set_underglow_light(2, mq.COLOR_GREEN)
    mq.set_underglow_light(3, mq.COLOR_GREEN)
    sleep_ms(1000)

#
# Excercise 1: House Colours
#
# Can you change the loop above to loop through the Arden House
# colours (Birnam, Jenolan, Sherwood). You should also show the
# first letter of the house on the Microbit when you display its
# colour. Pause for 1 second after each house.
#
# Note you can set all the underglow lights at the same time by
# using mq.set_underglow(color)
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
# Can you improve the responsiveness so it will stop after the next house?
#
