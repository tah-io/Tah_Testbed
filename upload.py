import RPi.GPIO as GPIO
import os
import time

os.chdir("/home/pi/GitRepo/Tah_Testbed/bootloaders/")
time.sleep(1)
os.system("./atm32U4.sh")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT, pull_up_down=GPIO.PUD_UP)
GPIO.output(22,GPIO.LOW)

os.chdir("/home/pi/GitRepo/Tah_Testbed/bootloaders/")
time.sleep(1)
os.system("./analogHIGH.sh")
GPIO.output(22,GPIO.LOW)

os.chdir("/home/pi/GitRepo/Tah_Testbed/bootloaders/")
time.sleep(1)
os.system("./analogLOW.sh")
GPIO.output(22,GPIO.LOW)



'''print "Compiled for LED BLINK"
os.system("make upload")
print "Uploaded Complete "
time.sleep(1)
'''
#os.chdir("/home/pi/GitRepo/tah-testbed/Vikas/Tahsketches/setAnalogLow")
#time.sleep(1)
#os.system("make")
#os.system("make upload")
#print "Upload Complete Analog LOW State"

#time.sleep(1)

    
print "END"


