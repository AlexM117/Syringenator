

import cv2
import pyrealsense2 as rs

pipeline = rs.pipeline()

try:
	# Create a context object. This object owns the handles to all connected
	# realsense devices
	pipeline.start()
except:
	print("Camera not found")
	exit()



while True:
	# Create a pipeline object. This object configures the streaming camera
	# and owns it's handle
	frames = pipeline.wait_for_frames()
	depth = frames.get_depth_frame()
	if not depth: continue

	# Print a simple text-based representation of the image, by breaking it
	# into 10x20 pixel regions and approximating the coverage of pixels
	# within one meter
	coverage = [0]*64
	
	for y in xrange(480):
		for x in xrange(640):
			dist = depth.get_distance(x, y)
			if 0 < dist and dist < 1:
				coverage[x/10] += 1
		
		if y%20 is 19:
			line = ""
			for c in coverage:
				line += " .:nhBXWW"[c/25]
			
			print(line)
			coverage = [0]*64
