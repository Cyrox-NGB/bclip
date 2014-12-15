#!/usr/bin/python

## EXAMPLE PSEUDOCODE:
##
## Creates a new BClip object to call the library functions,
## Turns on LEDs 1, 3 and 5,
## Turns on LEDs 2, 4 and 6 for 1 second each,
## Waits till the user presses the switch,
## Beeps 5 times 500ms with 500ms pause,
## Waits till the user presses the switch,
## Exits and cleans up GPIO at once.

from berryclip import BerryClip

bc = BClip()
bc.leds([1, 3, 5], True)
bc.ledsPulse([2, 4, 6], 1000, True)
bc.switchWait()
bc.beeps(5, 500, 500)
print("Press the switch to exit.")
bc.switchWait()
bc.clean()
