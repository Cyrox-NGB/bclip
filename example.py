#!/usr/bin/python

from berryclip import BerryClip

bc = BerryClip()
bc.leds([1, 3, 5], True)
bc.ledsPulse([2, 4, 6], 1000, True)
bc.switchWait()
bc.beeps(5, 500, 500)
bc.switchWait()
bc.clean()
