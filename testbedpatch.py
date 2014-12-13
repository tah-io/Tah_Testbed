import subprocess, os
from shutil import move
MAKEFILE_PATH = ["/home/pi/GitRepo/Tah_Testbed/Tahsketches/setAnalogHigh/Makefile","/home/pi/GitRepo/Tah_Testbed/Tahsketches/setGPIOHigh/Makefile","/home/pi/GitRepo/Tah_Testbed/Tahsketches/ArdSCL/Makefile"] # make sure you use the absolute path and not the relative

def remafterequals(text):
  where_ellipsis = text.find('=')
  if where_ellipsis == -1:
    return text
  return text[:where_ellipsis + 3]

os.chdir('/dev') # change this to /dev eventually
ls = subprocess.Popen('ls', stdout=subprocess.PIPE)
grep = subprocess.check_output(('grep','ttyACM[0-9]'), stdin=ls.stdout)
ls.wait()
port = grep
print port

for i in MAKEFILE_PATH:
    makefile = open(i)
    new_makefile = open(i+'new','wt')
    for line in makefile:
        if (line.rstrip().find('ARDUINO_PORT')==0):
            head, sep, tail = line.rstrip().partition('=')
            print head+"= /dev/"+port
            new_makefile.write(head+" = /dev/"+port)
        else:
            new_makefile.write(line)
            
    makefile.close()
    new_makefile.close()
    os.remove(i)
    move(i+'new',i)
