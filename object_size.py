from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import cv2
import imutils
import argparse

def midPoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5 , (ptA[1] + ptB[1])* 0.5)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True)
ap.add_argument("-w", "--width", type=float, required= True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width= 600)

# processing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)

edged = cv2.Canny(blurred, 50, 100)
edged = cv2.dilate(edged, None, iterations = 2)
edged = cv2.erode(edged, None, iterations = 2)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts) # create a contour container

(cnts, _) = contours.sort_contours(cnts) # sort contours from left to right
pixelsPerMetric = None

for c in cnts:
	if cv2.contourArea(c) < 100:
		continue

	orig = image.copy()
	box = cv2.minAreaRect(c)
	box = cv2.boxPoints(box)
	box = np.array(box, dtype = "int")

	box = perspective.order_points(box)
	cv2.drawContours(orig, [box.astype("int")], -1, (0,255,0) ,2)

	for (x,y) in box:
		cv2.circle(orig, ( int(x), int(y) ), 5 , (0,0,255) , -1)

	#unpacking the box
	(tl, tr, br, bl) = box

	#calculate mid-points
	(tltrX, tltrY) = midPoint(tl, tr)
	(blbrX, blbrY) = midPoint(bl, br)

	(tlblX, tlblY) = midPoint(tl, bl)
	(trbrX, trbrY) = midPoint(tr, br)

	#draw mid-point on the image
	cv2.circle(orig, (int(tltrX), int(tltrY) ), 5, (0,255,0), -1 )
	cv2.circle(orig, (int(blbrX), int(blbrY) ), 5, (0,255,0), -1 )
	cv2.circle(orig, (int(tlblX), int(tlblY) ), 5, (0,255,0), -1 )
	cv2.circle(orig, (int(trbrX), int(trbrY) ), 5, (0,255,0), -1 )

	#draw a line between mid-points
	#width
	cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
		(255, 0, 255), 2)
	#length
	cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
		(255, 0, 255), 2)

	#compute the distance between mid-points
	dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY)) # width
	dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY)) # length

	if pixelsPerMetric is None:
		pixelsPerMetric = dB / args["width"] # measured_width / known_width

	# convert distance of object to inches
	dimA = dA / pixelsPerMetric
	dimB = dB / pixelsPerMetric

	# draw the object sizes on the image
	cv2.putText(orig, "{:.1f}in".format(dimA),
		(int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)
	cv2.putText(orig, "{:.1f}in".format(dimB),
		(int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)

	# show the output image
	cv2.imshow("Image", orig)
	cv2.waitKey(0)


