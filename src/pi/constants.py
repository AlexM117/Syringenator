##	@file src/pi/constants.py
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

## The minimum azimuth byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
ARM_AZIMUTH_MIN = 0
## The maximum azimuth byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
ARM_AZIMUTH_MAX = 180
## The minimum range byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
ARM_RANGE_MIN = 12
## The maximum range byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
ARM_RANGE_MAX = 19
## The minimum orientation byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
ARM_ORIENT_MIN = 0
## The maximum orientation byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
ARM_ORIENT_MAX = 180
## The minimum target center x-value that allows a pickup
PICKUP_X_MIN = 250
## The maximum target center x-value that allows a pickup
PICKUP_X_MAX = 415
## The minimum target center y-value that allows a pickup
PICKUP_Y_MIN = 420
## The maximum target center y-value that allows a pickup
PICKUP_Y_MAX = 470
## The pixel value for the arm radius
PICKUP_RADIUS = 120
## The arms offset from the bottom of the image [px]
PICKUP_ARM_OFFSET = 50
## The maximum count of forward ticks used in moveCloser()
FWD_MAX_TICKS = 127
## The minimum count of forward ticks
FWD_MIN_TICKS = 1
## The maximum absolute value of rotation ticks used in moveCloser()
ROT_MAX_TICKS = 127
## The minimum count of rotational ticks
ROT_MIN_TICKS = 10
## Calibration factor used in rotation calculation
CAL_ROT_FACTOR = 0.35
## Calibration factor used in forward calculation
CAL_FWD_FACTOR = 0.07
## Offset of the arm axis from the camera axis [mm]
CAL_ARM_OFFSET = 95
## Height of the camera from the floor [mm]
CAL_CAM_HEIGHT = 984
## Angle of the camera from the horizon [radians]
CAL_CAM_ANGLE = 1.2117
## distance to the floor on the camera's center axis
CAL_CAM_AXIS = 1140
## x-offset between camera and body
CAL_CAM_X_OFFSET = -15
## A place holder for troubleshooting etc.
ARDUINO_NULL = 0
## If the arduino needs to acknowledge something
ARDUINO_STATUS_ACK = 65
## If the arduino needs to indicate it is ready
ARDUINO_STATUS_READY = 82
## Report that the pick failed
ARDUINO_STATUS_PICK_FAIL = 3
## Report that the pick succeded
ARDUINO_STATUS_PICK_SUCCESS = 4
## Report a general arm failure
ARDUINO_STATUS_ARM_FAULT = 5
## Report an obstacle detected
ARDUINO_STATUS_OBSTACLE = 6
## Report the command not understood
ARDUINO_STATUS_NACK = 78
## serial command the arduino to follow the line
ARDUINO_LINE_FOLLOW = 12
## serial command the arduino to avoid an obstacle
ARDUINO_AVOID = 13
## serial command the arduino to return to the line
ARDUINO_RETURN = 14
## serial command the arduino forward
ARDUINO_FWD = 15
## serial command the arduino to rotate right
ARDUINO_RIGHT = 16
## serial command the arduino to rotate left
ARDUINO_LEFT = 17
## serial command the arduino to call the park action sequence
ARDUINO_ARM_PARK = 20
## serial command the arduino to call the dispose action sequence
ARDUINO_ARM_DISPOSE = 21
## serial command the arduino to attempt a pick, followed by three bytes: azimuth, range, and orientation
ARDUINO_ARM_PICKUP = 22
## timer ticks to follow the line
LINE_FOLLOW_TIME = 100
## baudrate for serial communication between Arduino and Pi
SERIAL_BAUD = 9600
## Arduino pin for port motor forward
PORT_MOTOR_FWD = None
## Arduino pin for port motor reverse
PORT_MOTOR_REV = None
## Arduino pin for starboard motor forward
STBD_MOTOR_FWD = None
## Arduino pin for starboard motor reverse
STBD_MOTOR_REV = None
## Arduino pin for the port line sensor
PORT_LINE_SENSE = None
## Arduino pin for the starboard line sensor
STBD_LINE_SENSE = None
## Arduino pin for the port forward obstacle sensor
PORT_FWD_OBSTACLE = None
## Arduino pin for the port aft obstacle sensor
PORT_AFT_OBSTACLE = None
## Arduino pin for the starboard forward obstacle sensor
STBD_FWD_OBSTACLE = None
## Arduino pin for the starboard aft obstacle sensor
STBD_AFT_OBSTACLE = None
## Arduino pin for communication with the xArm
ARM_CONTROL = None
