import os
import time



os.chdir("/home/pi/Ali/tah-testbed/Vikas/Tahsketches/setAnalogHigh/")
time.sleep(1)
os.system("make")
print "Compiled for Analog HIGH State"
os.system("make upload")
print "Uploaded Complete Analog HIGH"
time.sleep(5)

os.chdir("/home/pi/Ali/tah-testbed/Vikas/Tahsketches/setAnalogLow")
time.sleep(1)
os.system("make")
os.system("make upload")
print "Upload Complete Analog LOW State"

time.sleep(2)
    
print "END"


