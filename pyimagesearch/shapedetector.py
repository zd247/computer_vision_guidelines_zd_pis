import cv2

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, c):
		shape = "unidentified"

		# contour approximation (Ramer-Douglas-Peucker or split-and-merge algorithm)
		peri = cv2.arcLength(c , True)
		approx = cv2.approxPolyDP(c, 0.04*peri, True) #see how many curves

		if len(approx) == 3:
			shape = "triangle"
		elif len(approx) == 4:
			(x,y,w,h) = cv2.boundingRect(approx)
			ar = w / float(h) # w,h ratio

			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
		elif len(approx) == 5:
			shape = "pentagon"
		else:
			shape = "circle"

		return shape