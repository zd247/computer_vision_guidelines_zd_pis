from imutils import paths
import numpy as np
import imutils
import cv2

def find_marker(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	blurred = cv2.GaussianBlur(cv2, (7,7), 0)
	edged = cv2.Canny(blurred,35, 125)

	cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	# find the largest contour in the image (assume that we only track one object)
	c = max(cnts , key = cv2.contourArea)

	# draw rectangle of the reference object
	return cv2.minAreaRect(c)

	def distance_to_camera(knownWidth, focalLength, perWidth):
		return (knownWidth * focalLength) / perWidth
