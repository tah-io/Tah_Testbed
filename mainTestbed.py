# This script will upload the Arduino test sketches to Tah and test for Analog LOW-HIGH and Digital LOW-HIGH states

import RPi.GPIO as GPIO
import os
import time
import RpiInit
import xlwt
from datetime import datetime
from Tah_Testing import Tah 
from lcd_1 import HD44780




prev_state = 0
testbed = Tah()
lcd = HD44780()

lcd.__init__()
lcd.clear()
lcd.message('starting')

book = xlwt.Workbook(encoding="utf-8") 
sheet1 = book.add_sheet("Tah First Batch ") 
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
		lcd.message('Analog LOW test')
	
		StartTime  = datetime.now() 
		#Testing Started here
		os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setAnalogLow/")
                os.system("make")
                os.system("make upload")
		time.sleep(1)
		AL = testbed.testAnalogLow()
                print AL 	
	
# Now test for Analog HIGH states
		lcd.__init__()
		lcd.message('Analog HIGH Test')

                os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setAnalogHigh/")
                os.system("make")
                os.system("make upload")
		time.sleep(1)
                AH = testbed.testAnalogHigh()
		print AH

# NOw test for Digital LOW  State
		lcd.__init__()
		lcd.message('GPIO LOW Test')

                os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setGPIOLow/")
                os.system("make")
                os.system("make upload")
		time.sleep(1)
		DL = testbed.testGPIOLow()
		print DL

#Now test for Digital HIGH state
		lcd.__init__()
		lcd.message('GPIO HIGH Test')

                os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/setGPIOHigh/")
                os.system("make")
                os.system("make upload")
		time.sleep(1)
		DH = testbed.testGPIOHigh()
	
		print DH
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
			print 'PASS'
			lcd.__init__()
			lcd.message('Tested OK!')
		else:
                	sheet1.write(row,4,"Failed")
			print 'Failed'
			lcd.__init__()
			lcd.message('Failed')
			
			while (i<4):
				GPIO.output(23,GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(23,GPIO.LOW)
				i=i+1

		book.save("Tah_TestbeReport.xls")
	else:
		print 'SW not pressed'
