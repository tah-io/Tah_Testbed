# This script will upload the Arduino test sketches to Tah and test for Analog LOW-HIGH and Digital LOW-HIGH states

import RPi.GPIO as GPIO
import csv
import os
import time
import RpiInit
import xlwt
from datetime import datetime
from Tah_Testing import Tah 
from lcd_1 import HD44780


#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(22, GPIO.OUT, pull_up_down=GPIO.PUD_UP)

prev_state = 0
testbed = Tah()
lcd = HD44780()

lcd.__init__()
lcd.clear()
lcd.message('Star The Test...')

f = open('13DEC_Log.csv','wb')
writer = csv.writer(f)
writer.writerow( ('Sr.No', 'Start Time', 'End Time','Elapsed Time','Remark') )
	

row =5
col =0
count =0
val =0
i=0
while True:
	RpiInit.init()		#initialze all GPIOs

	val =val+1
	# Switch input 
	startTest = GPIO.input(11)		#Read Start pulse from Switch S1
	print startTest
	if((not prev_state) and startTest):	#switch press
		GPIO.output(23,GPIO.HIGH)		#Buzzer ON
		time.sleep(0.5)
		GPIO.output(23,GPIO.LOW)		# OFF Buzzer
	        
		#Test  Start Time Log
		lcd.__init__()
#        lcd.message("Bootloader \n Burning...")
		
#		os.chdir("/home/pi/GitRepo/Tah_Testbed/bootloaders/")#
#		time.sleep(1)
#		os.system("./atm32U4.sh")
#		GPIO.output(22,GPIO.LOW)
		StartTime  = datetime.now()

#        lcd.message("Analog LOW Test") #
#		#Testing Started here
#		os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setAnalogLow/")
 #       	os.system("make")
  #      	os.system("make upload")
#		time.sleep(1)
#		AL = testbed.testAnalogLow()
 #       	print AL
        

        
# Now test for Analog HIGH states
		lcd.__init__()
		lcd.message('Analog Testing...')

        	os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setAnalogHigh/")
        	os.system("make")
        	os.system("make upload")
		time.sleep(1)
        	AH = testbed.testAnalogHigh()
		print AH

# Now test for Digital LOW  State
#		lcd.__init__()
#		lcd.message('GPIO LOW Test')
##
  #      	os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setGPIOLow/")
   #     	os.system("make")
    #    	os.system("make upload")
#		time.sleep(1)
#		DL = testbed.testGPIOLow()
#		print DL
# Now test for Digital HIGH state
		lcd.__init__()
		lcd.message('GPIO Testing...')

        	os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setGPIOHigh/")
        	os.system("make")
        	os.system("make upload")
		time.sleep(1)
		DH = testbed.testGPIOHigh()
	
		print DH
		print "Done Testing"
	

		if(AH==6 and DH >=10):
	        	'''lcd.__init__()
			lcd.message('Uploading ArdSCL')'''

	        	os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/ArdSCL/")	# Upload ArdSCL sketche
        		os.system("make")
	        	os.system("make upload")
			
        		EndTime  = datetime.now()	
				
	        	ElapsedTime = EndTime - StartTime
        		print "ElapsedTime:",ElapsedTime
	        	#print "Start Time:",StartTime
	
 		       	writer.writerow((i+1, StartTime, EndTime,ElapsedTime,'PASS')) 
	        	print 'PASS'
			i=i+1

  		      	GPIO.output(23,GPIO.HIGH)
	        	time.sleep(1)
        		GPIO.output(23,GPIO.LOW)
               	 	
	        	lcd.__init__()
        		lcd.message('Tested OK!')
		
		else:
			EndTime  = datetime.now()

                        ElapsedTime = EndTime - StartTime
                        print "ElapsedTime:",ElapsedTime

                        writer.writerow((i+1, StartTime, EndTime,ElapsedTime,'Failed'))
                        i=i+1

                        GPIO.output(23,GPIO.HIGH)
                        time.sleep(2)
                        GPIO.output(23,GPIO.LOW)

                        lcd.__init__()
                        lcd.message('Failed !')

				
	else:
		print "Start Test"
			
f.close()
#print open('TestBedLog.csv','r').read()

