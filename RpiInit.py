import RPi.GPIO as GPIO

def init():
	
	# to use Raspberry Pi board pin numbers 
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(15, GPIO.OUT)	# A
	GPIO.setup(19, GPIO.OUT)	# B

	GPIO.setup(8, GPIO.OUT)		# select line C
	GPIO.setup(10, GPIO.OUT)	# select line D
	
	GPIO.setup(23, GPIO.OUT)			
	
	GPIO.setup(7, GPIO.OUT)		# NC
	GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_UP)		# input SW NC
	#GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_UP)	# input
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(13, GPIO.LOW)
        GPIO.setup(10, GPIO.LOW)
        GPIO.setup(8, GPIO.LOW)
	GPIO.setup(23, GPIO.LOW) 
        GPIO.setup(7, GPIO.LOW)
	GPIO.setup(15,GPIO.LOW)
	GPIO.setup(19,GPIO.LOW)
	
	GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_UP)		# Input pin to check MUX o/p 
	
	GPIO.setup(21,GPIO.LOW)
	GPIO.setup(11,GPIO.LOW)
	GPIO.setup(13,GPIO.LOW)	
#GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

