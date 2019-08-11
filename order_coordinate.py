from __future__ import print_function
import argparse
import imutils
from imutils import perspective
from imutils import contours
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
				help = "image path to be loaded")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=600)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)

edged = cv2.Canny(gray,50,100)
edged = cv2.dilate(edged, None, iterations = 2)
edged = cv2.erode(edged, None, iterations = 2)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

(cnts, _) = contours.sort_contours(cnts)
colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0))

for (i,c) in enumerate (cnts):
	if cv2.contourArea(c) < 100:
		continue

	box = cv2.minAreaRect(c) # forming a (4,1,2) array
	box = cv2.boxPoints(box)
	box = np.array(box, dtype = "int")

	cv2.drawContours(image, [box], -1 , (0,255,0), 2)

	print ("Object #{}: " .format(i+1))
	print (box)

	rect = perspective.order_points(box)

	print (rect.astype("int"))
	print ("")

	# loop over the original points and draw them
	for ((x, y), color) in zip(rect, colors):
		cv2.circle(image, (int(x), int(y)), 5, color, -1)

	# draw the object num at the top-left corner
	cv2.putText(image, "Object #{}".format(i + 1),
		(int(rect[0][0] - 15), int(rect[0][1] - 15)),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)

	# show the image
	cv2.imshow("Image", image)
	cv2.waitKey(0)


