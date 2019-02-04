##	@file src/constants.py
#	Constants shared across the whole system.
#	Includes constants used by both the arduino sketch and the the python script.
#	The format of `constants.in` is three whitespace sparated columns:
#	
#	[NAME] [value] [comments]
#	
#	Any changes must be made in `constants.in` and followed by running:
#	
#	`make constants`
#	
#	--ABD
#	
#	@copyright Copyright &copy; 2019 by the authors. All rights reserved.
#	
#	This file has been autogenerated, CHANGES MADE HERE WILL NOT PERSIST

## 
ARM_AZIMUTH_MIN = 0
## 
ARM_AZIMUTH_MAX = 0
## 
ARM_RANGE_MIN = 0
## 
ARM_RANGE_MAX = 0
## 
ARM_ORIENT_MIN = 0
## 
ARM_ORIENT_MAX = 0
## 
PICKUP_X_MIN = 0
## 
PICKUP_X_MAX = 0
## 
PICKUP_Y_MIN = 0
## 
PICKUP_Y_MAX = 0
## A place holder for troubleshooting etc.
ARDUINO_NULL = 0x00
## If the arduino needs to acknowledge something
ARDUINO_STATUS_ACK = 0x01
## If the arduino needs to indicate it is ready
ARDUINO_STATUS_READY = 0x02
## Report that the pick failed
ARDUINO_STATUS_PICK_FAIL = 0x03
## Report that the pick succeded
ARDUINO_STATUS_PICK_SUCCESS = 0x04
## Report a general arm failure
ARDUINO_STATUS_ARM_FAULT = 0x05
## Report an obstacle detected
ARDUINO_STATUS_OBSTACLE = 0x06
## command the arduino to rotate the robot. This byte is followed by a signed byte indicating magnitude and direction
ARDUINO_ROTATE = 0x10
## command the arduino to advance the robot. This byte is followed by a signed byte indicating magnitude and direction
ARDUINO_MOVE = 0x11
## command the arduino to follow the line
ARDUINO_LINE_FOLLOW = 0x12
## call the park action sequence
ARDUINO_ARM_PARK = 0x20
## call the dispose action sequence
ARDUINO_ARM_DISPOSE = 0x21
## attempt a pick, followed by three bytes: azimuth, range, and orientation
ARDUINO_ARM_PICKUP = 0x22
## 
PORT_MOTOR_FWD = None
## 
PORT_MOTOR_AFT = None
## 
STBD_MOTOR_FWD = None
## 
STBD_MOTOR_AFT = None
## 
PORT_LINE_SENSE = None
## 
STBD_LINE_SENSE = None
## 
PORT_FWD_OBSTACLE = None
## 
PORT_AFT_OBSTACLE = None
## 
STBD_FWD_OBSTACLE = None
## 
STBD_AFT_OBSTACLE = None
## 
ARM_CONTROL = None
