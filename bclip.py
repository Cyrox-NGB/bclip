## bclip.py (by Cyrox @ngb.to)
## Last edited: 30/07/2014
## -----------------------------
## A small but functional library for the BerryClip GPIO AddOn board.
## Makes it easy to use the leds, buzzer and switch. Functions are mainly self-explanatory.

import sys
import time
import RPi.GPIO as GPIO

AI_GPIO_LEDS = [4, 17, 22, 10, 9, 11]
I_GPIO_SWITCH = 7
I_GPIO_BUZZER = 8

class BClip:
	
	def __init__(self):
		"Initializes the class and the GPIO pins"
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(I_GPIO_SWITCH, GPIO.IN)
		GPIO.setup(I_GPIO_BUZZER, GPIO.OUT)
		GPIO.output(I_GPIO_BUZZER, False)
		for i in range(6):
    			GPIO.setup(AI_GPIO_LEDS[i], GPIO.OUT)
			GPIO.output(AI_GPIO_LEDS[i], False)
	
	def led(self, iNr, bState):
		"Switches one single led (iNr) on or off"
		GPIO.output(AI_GPIO_LEDS[iNr-1], bState)
	
	def leds(self, aiNrs, bState):
		"Switches leds (aiNrs) on or off"
		for i in range(len(aiNrs)):
			self.led(aiNrs[i], bState)
	
	def ledPulse(self, iNr, iPulseMS):
		"Turns led on for a specified time in ms (iPulseMS)"
		self.led(iNr, True)
		time.sleep(float(iPulseMS) / 1000.0)
		self.led(iNr, False)

	def ledsPulse(self, aiNrs, iPulseMS, bOneByOne = False):
		"Turns leds on for a specified time in ms (iPulseMS)"
		if bOneByOne:
			for i in range(len(aiNrs)):
				self.ledPulse(aiNrs[i], iPulseMS)
		else:
			self.leds(aiNrs, True)
			time.sleep(float(iPulseMS) / 1000.0)
			self.leds(aiNrs, False)
	
	def switchWait(self, iMinPushMS = 100):
		"Pauses the script until the switch is pressed a specified time in milliseconds (iMinPushMS)"
		try:
			while GPIO.input(I_GPIO_SWITCH) == 0:
				pass
			fTimeStart = time.time()
			while GPIO.input(I_GPIO_SWITCH) == 1:
				fTimeStop = time.time()
			iDiffMS = int(round((fTimeStop - fTimeStart)*1000))
			if iDiffMS < iMinPushMS:
				self.switchWait(iMinPushMS)
		except KeyboardInterrupt:
			self.clean()	
	
	def buzzer(self, bState):
		"Uses the buzzer / turns it on or off"
		GPIO.output(I_GPIO_BUZZER, bState)	

	def beep(self, iBeepMS):
		"Uses the buzzer to beep a defined time in milliseconds (iBeepMS)"
		self.buzzer(True)
		time.sleep(float(iBeepMS) / 1000.0)
		self.buzzer(False)
	
	def beeps(self, iTimes, iBeepMS, iSleepMS):
		"Uses the buzzer to beep in a defined interval n times"
		for i in range(0, iTimes):
			self.beep(iBeepMS)
			time.sleep(float(iSleepMS) / 1000.0)	
	
	def beepSequences(self, iaBeepMS, iaSleepMS):
		"Uses the buzzer to beep in sequences"
		for i in range(len(iaBeepMS)):
			self.beep(iaBeepMS[i])
			if i < len(iaSleepMS):
				time.sleep(float(iaSleepMS[i]) / 1000.0)
	
	def clean(self):
		"Resets/Cleans up GPIO and exits"
		GPIO.cleanup()
		sys.exit(0)
