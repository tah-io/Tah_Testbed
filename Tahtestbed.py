# This script will upload the Arduino test sketches to Tah and test for Analog LOW-HIGH and Digital LOW-HIGH states

import RPi.GPIO as GPIO
import os
import time
import RpiInit

prev_state = 0
RpiInit.init()		#initialze all GPIOs


while True:

	# Switch input 
	startTest = GPIO.input(11)		#Read Start pulse from Switch S1
	if((not prev_state) and startTest):	#switch press
		GPIO.output(23,GPIO.HIGH)		#Buzzer ON
       		time.sleep(1)
	        GPIO.output(23,GPIO.LOW)		# OFF Buzzer

#first Test for Analog pins 
	   
	    	os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setAnalogLow/")
	    	time.sleep(1)
	    	os.system("make")
            	os.system("make upload")
            	print "Testing For Analog Low State"
	    	os.system("sudo python /home/pi/GitRepo/Tah_Testbed/testAnalogLow.py")
		print "********************** DONE Analog LOW state Testing**********************"
		time.sleep(5)
# NOw test for Analog HIGH states
		os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setAnalogHigh/")
                time.sleep(1)
                os.system("make")
                os.system("make upload")
                print "Testing For Analog HIGH State"
                os.system("sudo python /home/pi/GitRepo/Tah_Testbed/testAnalogHigh.py")
                print "******************* DONE Analog HIGH Testing*****************************"
	
# NOw test for Digital LOW  State
		os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setGPIOLow/")
                time.sleep(1)
                os.system("make")
                os.system("make upload")
                print "Testing For GPIO LOW State"
                os.system("sudo python /home/pi/GitRepo/Tah_Testbed/testGPIOLow.py")
                print "**************** DONE GPIO LOW state  Testing*********************************"
	
#Now test for Digital HIGH state
		os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setGPIOHigh/")
                time.sleep(1)
                os.system("make")
                os.system("make upload")
                print "Testing For GPIO HIGH State"
                os.system("sudo python /home/pi/GitRepo/Tah_Testbed/testGPIOLow.py")
                print "******************* DONE GPIO HIGH state  Testing**************************"
	
		break
	else:
		print "Test not Started"


		
print "--------------------------------DONE------------------------------"
GPIO.cleanup()
