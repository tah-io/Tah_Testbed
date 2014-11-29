import RPi.GPIO as GPIO
import time
import RpiInit



class Tah:
	
	RpiInit.init()
	def testAnalogLow(self):
		
		count = 0

	        GPIO.output(15,GPIO.HIGH)
        	GPIO.output(19,GPIO.HIGH)       # set channel 7 _19
       		GPIO.output(8,GPIO.HIGH)
        	GPIO.output(10,GPIO.LOW)
        	#lcd.message("A0 Testing")
        	#Tah_LCD.lcd_byte(LCD_LINE_1, LCD_CMD)
        	#Tah_LCD.lcd_string("Tah Testing")

        	print "A0 Testing"
        	#GPIO.cleanup(21)
        	value0 =GPIO.input(21)          # Mux output pin
	        if(not value0):
			count =count +1
		time.sleep(0.5)

        	GPIO.output(15,GPIO.HIGH)
        	GPIO.output(19,GPIO.LOW)        # set channel 5
        	GPIO.output(8,GPIO.HIGH)
        	GPIO.output(10,GPIO.LOW)

		print "A1 Testing"
       		value1 = GPIO.input(21)         # read input
	        if( not value1):
			count = count +1
		time.sleep(0.5)

        	GPIO.output(15,GPIO.LOW)
        	GPIO.output(19,GPIO.HIGH)        # set channel 6
        	GPIO.output(8,GPIO.HIGH)
        	GPIO.output(10,GPIO.LOW)
        	
		print "A2 Testing"
        	value2 = GPIO.input(21)         # read input
	        if(not value2):
			count =count +1
		time.sleep(0.5)

		GPIO.output(15,GPIO.LOW)
        	GPIO.output(19,GPIO.LOW)        # set channel 4
       		GPIO.output(8,GPIO.HIGH)
        	GPIO.output(10,GPIO.LOW)
        	print "A3 Testing"
        	value3 = GPIO.input(21)         # read input
		if(not value3):
			count =count +1
	        time.sleep(0.5)

		GPIO.output(15,GPIO.LOW)
       		GPIO.output(19,GPIO.HIGH)        # set channel 2
        	GPIO.output(8,GPIO.LOW)
        	GPIO.output(10,GPIO.LOW)
       		print "A4 Testing"
        	value4 = GPIO.input(21)         # read input
		if(not value4):
			count = count +1
	        time.sleep(0.5)

        	GPIO.output(15,GPIO.HIGH)
       		GPIO.output(19,GPIO.LOW)        # set channel 1
        	GPIO.output(8,GPIO.LOW)
        	GPIO.output(10,GPIO.LOW)
        	print "A5 Testing"
        	value5 = GPIO.input(21)         # read input
		if(not value5):
			count = count +1
		time.sleep(0.5)

		print count
		
		print "****************************Analog Pin LOW State***************************"
		return count

		GPIO.cleanup()




	def testAnalogHigh(self):
		
		count = 0

                GPIO.output(15,GPIO.HIGH)
                GPIO.output(19,GPIO.HIGH)       # set channel 7 _19
                GPIO.output(8,GPIO.HIGH)
                GPIO.output(10,GPIO.LOW)
                #lcd.message("A0 Testing")
                #Tah_LCD.lcd_byte(LCD_LINE_1, LCD_CMD)
                #Tah_LCD.lcd_string("Tah Testing")

                print "A0 Testing"
                #GPIO.cleanup(21)
                value0 =GPIO.input(21)          # Mux output pin
                if(value0):
                        count =count +1
                time.sleep(0.5)

                GPIO.output(15,GPIO.HIGH)
                GPIO.output(19,GPIO.LOW)        # set channel 5
                GPIO.output(8,GPIO.HIGH)
                GPIO.output(10,GPIO.LOW)

                print "A1 Testing"
                value1 = GPIO.input(21)         # read input
                if(value1):
                        count = count +1
                time.sleep(0.5)

		GPIO.output(15,GPIO.LOW)
                GPIO.output(19,GPIO.HIGH)        # set channel 6
                GPIO.output(8,GPIO.HIGH)
                GPIO.output(10,GPIO.LOW)

                print "A2 Testing"
                value2 = GPIO.input(21)         # read input
                if(value2):
                        count =count +1
                time.sleep(0.5)

                GPIO.output(15,GPIO.LOW)
                GPIO.output(19,GPIO.LOW)        # set channel 4
                GPIO.output(8,GPIO.HIGH)
                GPIO.output(10,GPIO.LOW)
                print "A3 Testing"
                value3 = GPIO.input(21)         # read input
                if(value3):
                        count =count +1
                time.sleep(0.5)

                GPIO.output(15,GPIO.LOW)
                GPIO.output(19,GPIO.HIGH)        # set channel 2
                GPIO.output(8,GPIO.LOW)
                GPIO.output(10,GPIO.LOW)
                print "A4 Testing"

		value4 = GPIO.input(21)         # read input
                if(value4):
                        count = count +1
                time.sleep(0.5)

                GPIO.output(15,GPIO.HIGH)
                GPIO.output(19,GPIO.LOW)        # set channel 1
                GPIO.output(8,GPIO.LOW)
                GPIO.output(10,GPIO.LOW)
                print "A5 Testing"
                value5 = GPIO.input(21)         # read input
                if(value5):
                        count = count +1
                time.sleep(0.5)

                print count

                print "****************************Analog pins High State****************************"
		return count
                GPIO.cleanup()

		
	def testGPIOLow(self):
		
		count = 0

	        GPIO.output(15,GPIO.HIGH)
        	GPIO.output(19,GPIO.HIGH)       # set channel 11 
        	GPIO.output(8,GPIO.LOW)
        	GPIO.output(10,GPIO.HIGH)
       		#lcd.message("D2 Testing")
        	print "D2 Testing"

	        value0 =GPIO.input(21)          # Mux output pin
        	print value0
		
		if (not value0):
			count =count +1
                	print "D2 Ok!"
       		time.sleep(0.5)
                           
		GPIO.output(15,GPIO.LOW)
        	GPIO.output(19,GPIO.HIGH)        # set channel 10
        	GPIO.output(8,GPIO.LOW)
        	GPIO.output(10,GPIO.HIGH)

       		print "D3 Testing"
        
		value1 = GPIO.input(21)         # read input
        	print value1
		if(not value1):
                	count =count +1
			print "D3 Ok!"
        	time.sleep(0.5)
	
		GPIO.output(15,GPIO.HIGH)
        	GPIO.output(19,GPIO.LOW)        # set channel 9
       		GPIO.output(8,GPIO.LOW)
        	GPIO.output(10,GPIO.HIGH)
        	print "D4 Testing"
        	value2 = GPIO.input(21)         # read input
        	print value2
		if(not value2):
			count =count +1
			print "D4 Ok!"
	
	        time.sleep(0.5)
	
		GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.LOW)        # set channel 8
	        GPIO.output(8,GPIO.LOW)
	        GPIO.output(10,GPIO.HIGH)
	        print "D5 Testing"
	        value3 = GPIO.input(21)         # read input
	        if (not value3):
			count =count +1
			print "D5 Ok!"
	        
	        time.sleep(0.5)
	
	        GPIO.output(15,GPIO.HIGH)
	        GPIO.output(19,GPIO.HIGH)        # set channel 7
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D6 Testing"
	        value4 = GPIO.input(21)         # read input
	        if(not value4):
			count =count +1
			print "D6 Ok!"
	        time.sleep(0.5)
	
		GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D7 Testing"
	        value5 = GPIO.input(21)         # read input
	        if(not value5):
			count =count +1
			print "D7 Ok!"
	        time.sleep(0.5)
	
	
		GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D8 Testing"
	        value6 = GPIO.input(21)         # read input
	        if(not value6):
			count =count +1
			print "D8 Ok!"
	        time.sleep(0.5)
	
		GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D9 Testing"
	        value7 = GPIO.input(21)         # read input
	        if(not value7):
			count =count +1
			print "D9 Ok!"
	        time.sleep(0.5)
	
	        GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D10 Testing"
	        value8 = GPIO.input(21)         # read input
	        if(not value8):
			count =count +1
			print "D10 Ok!"
	        time.sleep(0.5)
	
		GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D11 Testing"
	        value9 = GPIO.input(21)         # read input
	        if(not value9):
			count =count +1
			print "D11 ok!"
	        time.sleep(0.5)
	
	
		GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D12 Testing"
	        value10 = GPIO.input(21)         # read input
	        if(not value10):
			count =count +1
			print "D12 Ok!"
	        time.sleep(0.5)
	
	        GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D13 Testing"
	        value11 = GPIO.input(21)         # read input
	        if(not value11):
			count =count +1
			print "D13 Ok!"
	        time.sleep(0.5)
	        
		print "****************************GPIO Pins Low Tested****************************"
		return count

		GPIO.cleanup()



	def testGPIOHigh(self):
		
		count = 0

	        GPIO.output(15,GPIO.HIGH)
        	GPIO.output(19,GPIO.HIGH)       # set channel 11 
        	GPIO.output(8,GPIO.LOW)
        	GPIO.output(10,GPIO.HIGH)
       		#lcd.message("D2 Testing")
        	print "D2 Testing"

	        value0 =GPIO.input(21)          # Mux output pin
        	print value0
		
		if (value0):
			count =count +1
                	print "D2 Ok!"
       		time.sleep(0.5)
                           
		GPIO.output(15,GPIO.LOW)
        	GPIO.output(19,GPIO.HIGH)        # set channel 10
        	GPIO.output(8,GPIO.LOW)
        	GPIO.output(10,GPIO.HIGH)

       		print "D3 Testing"
        
		value1 = GPIO.input(21)         # read input
        	print value1
		if(value1):
                	count =count +1
			print "D3 Ok!"
        	time.sleep(0.5)
	
		GPIO.output(15,GPIO.HIGH)
        	GPIO.output(19,GPIO.LOW)        # set channel 9
       		GPIO.output(8,GPIO.LOW)
        	GPIO.output(10,GPIO.HIGH)
        	print "D4 Testing"
        	value2 = GPIO.input(21)         # read input
        	print value2
		if(value2):
			count =count +1
			print "D4 Ok!"
	
	        time.sleep(0.5)
	
		GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.LOW)        # set channel 8
	        GPIO.output(8,GPIO.LOW)
	        GPIO.output(10,GPIO.HIGH)
	        print "D5 Testing"
	        value3 = GPIO.input(21)         # read input
	        if (value3):
			count =count +1
			print "D5 Ok!"
	        
	        time.sleep(0.5)
	
	        GPIO.output(15,GPIO.HIGH)
	        GPIO.output(19,GPIO.HIGH)        # set channel 7
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D6 Testing"
	        value4 = GPIO.input(21)         # read input
	        if(value4):
			count =count +1
			print "D6 Ok!"
	        time.sleep(0.5)
	
		GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D7 Testing"
	        value5 = GPIO.input(21)         # read input
	        if(value5):
			count =count +1
			print "D7 Ok!"
	        time.sleep(0.5)
	
	
		GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D8 Testing"
	        value6 = GPIO.input(21)         # read input
	        if(value6):
			count =count +1
			print "D8 Ok!"
	        time.sleep(0.5)
	
		GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D9 Testing"
	        value7 = GPIO.input(21)         # read input
	        if(value7):
			count =count +1
			print "D9 Ok!"
	        time.sleep(0.5)
	
	        GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D10 Testing"
	        value8 = GPIO.input(21)         # read input
	        if(value8):
			count =count +1
			print "D10 Ok!"
	        time.sleep(0.5)
	
		GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D11 Testing"
	        value9 = GPIO.input(21)         # read input
	        if(value9):
			count =count +1
			print "D11 ok!"
	        time.sleep(0.5)
	
	
		GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D12 Testing"
	        value10 = GPIO.input(21)         # read input
	        if(value10):
			count =count +1
			print "D12 Ok!"
	        time.sleep(0.5)
	
	        GPIO.output(15,GPIO.LOW)
	        GPIO.output(19,GPIO.HIGH)        # set channel 6
	        GPIO.output(8,GPIO.HIGH)
	        GPIO.output(10,GPIO.LOW)
	        print "D13 Testing"
	        value11 = GPIO.input(21)         # read input
	        if(value11):
			count =count +1
			print "D13 Ok!"
	        time.sleep(0.5)
	        
		print "****************************GPIO pins High Tested****************************"
		return count

		GPIO.cleanup()


if __name__ == '__main__':
	
	A =Tah()
	A.testAnalogLow()
