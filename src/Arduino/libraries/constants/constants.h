/**	@file src/Arduino/libraries/constants/constants.h
 *	Constants shared across the whole system.
 *	Includes constants used by both the arduino sketch and the the python script.
 *	The format of `constants.in` is three whitespace sparated columns:
 *	
 *	[NAME] [value] [comments]
 *	
 *	Any changes must be made in `constants.in` and followed by running:
 *	
 *	`make constants`
 *	
 *	--ABD
 *	
 *	@copyright Copyright &copy; 2019 by the authors. All rights reserved.
 *	
 *	This file has been autogenerated, CHANGES MADE HERE WILL NOT PERSIST
 */


#ifndef CONSTANTS_H
#define CONSTANTS_H


#define ARM_AZIMUTH_MIN 0 ///< The minimum azimuth byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
#define ARM_AZIMUTH_MAX 180 ///< The maximum azimuth byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
#define ARM_RANGE_MIN 12 ///< The minimum range byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
#define ARM_RANGE_MAX 19 ///< The maximum range byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
#define ARM_ORIENT_MIN 0 ///< The minimum orientation byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
#define ARM_ORIENT_MAX 180 ///< The maximum orientation byte value that can be passed to the arduino with ARDUINO_ARM_PICKUP
#define PICKUP_X_MIN 250 ///< The minimum target center x-value that allows a pickup
#define PICKUP_X_MAX 410 ///< The maximum target center x-value that allows a pickup
#define PICKUP_Y_MIN 420 ///< The minimum target center y-value that allows a pickup
#define PICKUP_Y_MAX 470 ///< The maximum target center y-value that allows a pickup
#define FWD_MAX_TICKS 127 ///< The maximum count of forward ticks used in moveCloser()
#define FWD_MIN_TICKS 1 ///< The minimum count of forward ticks
#define ROT_MAX_TICKS 127 ///< The maximum absolute value of rotation ticks used in moveCloser()
#define ROT_MIN_TICKS 1 ///< The minimum count of rotational ticks
#define CAL_ROT_FACTOR 1 ///< Calibration factor used in rotation calculation
#define CAL_FWD_FACTOR 0.07 ///< Calibration factor used in forward calculation
#define CAL_ARM_OFFSET 95 ///< Offset of the arm axis from the camera axis [mm]
#define CAL_CAM_HEIGHT 984 ///< Height of the camera from the floor [mm]
#define CAL_CAM_ANGLE 1.2117 ///< Angle of the camera from the horizon [radians]
#define CAL_CAM_AXIS 1140 ///< distance to the floor on the camera's center axis
#define ARDUINO_NULL 0 ///< A place holder for troubleshooting etc.
#define ARDUINO_STATUS_ACK 65 ///< If the arduino needs to acknowledge something
#define ARDUINO_STATUS_READY 82 ///< If the arduino needs to indicate it is ready
#define ARDUINO_STATUS_PICK_FAIL 3 ///< Report that the pick failed
#define ARDUINO_STATUS_PICK_SUCCESS 4 ///< Report that the pick succeded
#define ARDUINO_STATUS_ARM_FAULT 5 ///< Report a general arm failure
#define ARDUINO_STATUS_OBSTACLE 6 ///< Report an obstacle detected
#define ARDUINO_STATUS_NACK 78 ///< Report the command not understood
#define ARDUINO_LINE_FOLLOW 12 ///< serial command the arduino to follow the line
#define ARDUINO_AVOID 13 ///< serial command the arduino to avoid an obstacle
#define ARDUINO_RETURN 14 ///< serial command the arduino to return to the line
#define ARDUINO_FWD 15 ///< serial command the arduino forward
#define ARDUINO_RIGHT 16 ///< serial command the arduino to rotate right
#define ARDUINO_LEFT 17 ///< serial command the arduino to rotate left
#define ARDUINO_ARM_PARK 20 ///< serial command the arduino to call the park action sequence
#define ARDUINO_ARM_DISPOSE 21 ///< serial command the arduino to call the dispose action sequence
#define ARDUINO_ARM_PICKUP 22 ///< serial command the arduino to attempt a pick, followed by three bytes: azimuth, range, and orientation
#define SERIAL_BAUD 9600 ///< baudrate for serial communication between Arduino and Pi
#define PORT_MOTOR_FWD None ///< Arduino pin for port motor forward
#define PORT_MOTOR_REV None ///< Arduino pin for port motor reverse
#define STBD_MOTOR_FWD None ///< Arduino pin for starboard motor forward
#define STBD_MOTOR_REV None ///< Arduino pin for starboard motor reverse
#define PORT_LINE_SENSE None ///< Arduino pin for the port line sensor
#define STBD_LINE_SENSE None ///< Arduino pin for the starboard line sensor
#define PORT_FWD_OBSTACLE None ///< Arduino pin for the port forward obstacle sensor
#define PORT_AFT_OBSTACLE None ///< Arduino pin for the port aft obstacle sensor
#define STBD_FWD_OBSTACLE None ///< Arduino pin for the starboard forward obstacle sensor
#define STBD_AFT_OBSTACLE None ///< Arduino pin for the starboard aft obstacle sensor
#define ARM_CONTROL None ///< Arduino pin for communication with the xArm

#endif // CONSTANTS_H


