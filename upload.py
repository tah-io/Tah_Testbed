import os
import time



os.chdir("/home/pi/GitRepo/Tah_Testbed/Tahsketches/blink/")
time.sleep(1)
os.system("make")
print "Compiled for LED BLINK"
os.system("make upload")
print "Uploaded Complete "
time.sleep(1)

#os.chdir("/home/pi/GitRepo/tah-testbed/Vikas/Tahsketches/setAnalogLow")
#time.sleep(1)
#os.system("make")
#os.system("make upload")
#print "Upload Complete Analog LOW State"

#time.sleep(1)

    
print "END"


