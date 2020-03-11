from __future__ import print_function
from matplotlib import pyplot as plt
import cv2
import imutils
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, 450, 900)


#=============[grayscaled]============
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grayed", gray)

# hist = cv2.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(hist)
# plt.xlim([0,256])
# plt.show()

#==============[colored]==============

# cv2.imshow("Original", image)
# chans = cv2.split(image) #split image into 3 channels
# colors = ("b", "g", "r")
# plt.figure()
# plt.title("'Flattened' Color Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")

# for (chan, color) in zip (chans, colors):
# 	hist = cv2.calcHist([chan], [0], None, [256], [0,256])
# 	plt.plot(hist, color = color)
# 	plt.xlim([0,256])
# plt.show()

#==============[equalization]============

# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# eq = cv2.equalizeHist(image)

# cv2.imshow("Histogram Equalization", np.hstack([image, eq]))

#===========[masked histogram]============

def plot_histogram(image, title, mask = None):
	chans = cv2.split(image)
	colors = ("b", "g", "r")
	plt.figure()
	plt.title(title)
	plt.xlabel("Bins")
	plt.ylabel("# of pixels")

	for(chan, color) in zip(chans, colors):
		hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
		plt.plot(hist, color = color)
		plt.xlim([0,256])
	plt.show()

# cv2.imshow("Original", image)
plot_histogram(image, "Histogram for original image")

#define our mask
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (150,100), (350,350), 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked image", masked)
plot_histogram(image, "Histogram for masked image", mask = mask)


cv2.waitKey(0)
