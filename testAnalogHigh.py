import RPi.GPIO as GPIO
import time
import os
import RpiInit
from lcd_1 import HD44780
import serial


RpiInit.init()
lcd =  HD44780()

# setup input channel
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.OUT, pull_up_down=GPIO.PUD_UP)

while True:

        GPIO.setwarnings(False)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)       # set channel 7 _19
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        #lcd.message("A0 Testing")
        #Tah_LCD.lcd_byte(LCD_LINE_1, LCD_CMD)
        #Tah_LCD.lcd_string("Tah Testing")

        print "A0 Testing"
        value0 =GPIO.input(21)          # Mux output pin
        if value0:
                print "A0 OK!"
	else:
	        print "A0 Failed"
        time.sleep(0.5)

        GPIO.output(15,GPIO.HIGH)
        GPIO.output(19,GPIO.LOW)        # set channel 5
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)

        print "A1 Testing"
        value1 = GPIO.input(21)         # read input
        if value1:
                print "A1 OK!"
        else:
                print "A1 Failed"
        time.sleep(0.5)

	GPIO.output(15,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)        # set channel 6
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        print "A2 Testing"
        value2 = GPIO.input(21)         # read input
        if value2:
                print "A2 OK!"
        else:
                print "A2 Failed"
        time.sleep(0.5)

	GPIO.output(15,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)        # set channel 4
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        print "A3 Testing"
        value3 = GPIO.input(21)         # read input
        if value3:
                print "A3 OK!"
        else:
                print "A3 Failed"
        time.sleep(0.5)

	GPIO.output(15,GPIO.LOW)
        GPIO.output(19,GPIO.HIGH)        # set channel 2
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        print "A4 Testing"
        value4 = GPIO.input(21)         # read input
        if value4:
                print "A4 OK!"
        else:
                print "A4 Failed"
        time.sleep(0.5)

        GPIO.output(15,GPIO.HIGH)
        GPIO.output(19,GPIO.LOW)        # set channel 1
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        print "A5 Testing"
        value5 = GPIO.input(21)         # read input
        if value5:
                print "A5 OK!"
        else:
                print "A5 Failed"
        time.sleep(0.5)
        break
print "************Tested Analog HIGH State************"
GPIO.cleanup()


