# This script will upload the Arduino test sketches to Tah and test for Analog LOW-HIGH and Digital LOW-HIGH states

import RPi.GPIO as GPIO
import os
import time
import RpiInit
from Tah_Testing import Tah 
from lcd_1 import HD44780

prev_state = 0
RpiInit.init()		#initialze all GPIOs

testbed = Tah()


while True:

	# Switch input 
	startTest = GPIO.input(11)		#Read Start pulse from Switch S1
	print startTest
	if((not prev_state) and startTest):	#switch press
		GPIO.output(23,GPIO.HIGH)		#Buzzer ON
		time.sleep(0.5)
		GPIO.output(23,GPIO.LOW)		# OFF Buzzer
	       
		AL = testbed.testGPIOLow()
                print AL 	
		
		

	else:
		print 'SW not pressed'
