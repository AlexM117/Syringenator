

import serial
import constants
import time

## Timeout seconds to wait for status byte
TIMEOUT = 2

##	Instantiate  the communication port with the Arduino
#	@author Ammon Dodson
#
#	I wanted to prevent any situation where we would wait indefinitely for the
#	arduino. So the arduino sends ready bytes repeatedly and this class has to
#	deal with the buffer filling effects.
#
#	@private p is the pyserial port

class ComPort:
	## Constructor opens a serial port.
	def __init__(self):
		# different arduino's appear as different devices
		try: self.p = serial.Serial('/dev/ttyACM0', timeout=1)
		except: self.p = serial.Serial('/dev/ttyUSB0', timeout=1)
	
	##	Get the arduino's current status byte.
	#	@returns an integer with the value of the arduino status.
	def status(self):
		then = time.time()
		status = constants.ARDUINO_NULL
		
		while True:
			if self.p.in_waiting != 0:
				status = bytearray(self.p.read())[0]
			
			if (status!=constants.ARDUINO_STATUS_READY and status!=constants.ARDUINO_NULL):
				break
			
			now = time.time()
			if now > then+TIMEOUT:
				break
		
		return status
	
	##	Send a command to the arduino.
	#	@returns None
	def send(self, bytes):
		length = len(bytes)
		#print "length is: " + str(length)
		# flush the incoming buffer
		#self.p.reset_input_buffer()
		sentLength = self.p.write(bytes)
		if(length != sentLength): print "SySerial: length mismatch"
		self.p.flush()
	
	##	Wait for a ARDUINO_STATUS_READY byte.
	#	@returns None
	#	Will loop indefinitely if no arduino is present.
	def waitForReady(self):
		status = constants.ARDUINO_NULL
		while (status!=constants.ARDUINO_STATUS_READY):
			if self.p.in_waiting != 0:
				status = bytearray(self.p.read())[0]


## Convert an arduino status byte to a human readable string.
def statusString(s):
	table = {
		constants.ARDUINO_NULL               : "ARDUINO_NULL",
		constants.ARDUINO_STATUS_ACK         : "ARDUINO_STATUS_ACK",
		constants.ARDUINO_STATUS_NACK        : "ARDUINO_STATUS_NACK",
		constants.ARDUINO_STATUS_READY       : "ARDUINO_STATUS_READY",
		constants.ARDUINO_STATUS_PICK_FAIL   : "ARDUINO_STATUS_PICK_FAIL",
		constants.ARDUINO_STATUS_PICK_SUCCESS: "ARDUINO_STATUS_PICK_SUCCESS",
		constants.ARDUINO_STATUS_ARM_FAULT   : "ARDUINO_STATUS_ARM_FAULT",
		constants.ARDUINO_STATUS_OBSTACLE    : "ARDUINO_STATUS_OBSTACLE",
#		constants.ARDUINO_ROTATE             : "ARDUINO_ROTATE",
#		constants.ARDUINO_MOVE               : "ARDUINO_MOVE",
		constants.ARDUINO_LINE_FOLLOW        : "ARDUINO_LINE_FOLLOW",
		constants.ARDUINO_AVOID              : "ARDUINO_AVOID",
		constants.ARDUINO_RETURN             : "ARDUINO_RETURN",
		constants.ARDUINO_FWD                : "ARDUINO_FWD",
		constants.ARDUINO_LEFT               : "ARDUINO_LEFT",
		constants.ARDUINO_RIGHT              : "ARDUINO_RIGHT",
		constants.ARDUINO_ARM_PARK           : "ARDUINO_ARM_PARK",
		constants.ARDUINO_ARM_DISPOSE        : "ARDUINO_ARM_DISPOSE",
		constants.ARDUINO_ARM_PICKUP         : "ARDUINO_ARM_PICKUP"
	}
	return table.get(s, "INVALID CODE")


