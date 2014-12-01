# This script will upload the Arduino test sketches to Tah and test for Analog LOW-HIGH and Digital LOW-HIGH states

import RPi.GPIO as GPIO
import os
import time
import RpiInit
import xlwt
from datetime import datetime
from Tah_Testing import Tah 
#from lcd_1 import HD44780
import Tah_LCD


prev_state = 0
RpiInit.init()		#initialze all GPIOs

testbed = Tah()
#lcd = HD44780

book = xlwt.Workbook(encoding="utf-8") 
sheet1 = book.add_sheet("Tah First Batch ") 
row =5
col =0
count =0
val =0

#lcd.message("Starting")
while (val <2):
	val =val+1
	# Switch input 
	startTest = GPIO.input(11)		#Read Start pulse from Switch S1
	print startTest
	if((not prev_state) and startTest):	#switch press
		GPIO.output(23,GPIO.HIGH)		#Buzzer ON
		time.sleep(0.5)
		GPIO.output(23,GPIO.LOW)		# OFF Buzzer
	        #Test  Start Time Log
		StartTime  = datetime.now() 
		#Testing Started here
		os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setAnalogLow/")
                os.system("make")
                os.system("make upload")
		time.sleep(1)
		AL = testbed.testAnalogLow()
                print AL 	
	
# Now test for Analog HIGH states
                os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setAnalogHigh/")
                os.system("make")
                os.system("make upload")
		time.sleep(1)
                AH = testbed.testAnalogHigh()
		
# NOw test for Digital LOW  State
                os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setGPIOLow/")
                os.system("make")
                os.system("make upload")
		time.sleep(1)
		DL = testbed.testGPIOLow()
#Now test for Digital HIGH state
                os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setGPIOHigh/")
                os.system("make")
                os.system("make upload")
		time.sleep(1)
		DH = testbed.testGPIOHigh()
		
		print "Done Testing"

		EndTime  = datetime.now()	
		

		ElapsedTime = EndTime - StartTime
		print "ElapsedTime:",ElapsedTime

		sheet1.write(row,1,str(StartTime))
		sheet1.write(row,2,str(EndTime))
		sheet1.write(row,3,str(ElapsedTime))
		#sheet1.write(row,4,"PASS")

		row = row+1 
		count = count+1
		
		if(AL ==6 and AH ==6 and DL==12 and DH ==12):
                	sheet1.write(row,4,"PASS")
		else:
                	sheet1.write(row,4,"Failed")
		
		book.save("Tah_TestbeReport.xls")
	else:
		print 'SW not pressed'
