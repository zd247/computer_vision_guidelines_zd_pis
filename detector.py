# import the necessary packages
import argparse
import imutils
import cv2
from pyimagesearch.shapedetector import ShapeDetector
from pyimagesearch.colorlabeler import ColorLabeler

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# resize
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# image processing
lab = cv2.cvtColor(cv2.GaussianBlur(resized, (5,5), 0), cv2.COLOR_BGR2LAB)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)


sd = ShapeDetector()
cl = ColorLabeler()

# loop over the contours
for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	if M["m00"] == 0:
		M["m00"] = 1
	cX = int(M["m10"] / M["m00"] * ratio)
	cY = int(M["m01"] / M["m00"] * ratio)

	shape = sd.detect(c)
	color = cl.label(lab, c)

	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape on the image
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")

	# draw the contour and center of the shape on the image
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	text = "{} {}".format(color, shape)
	cv2.putText(image, text, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (255, 255, 255), 2)
	# show the image
	cv2.imshow("Image", image)
	cv2.waitKey(0)

cv2.destroyAllWindows()