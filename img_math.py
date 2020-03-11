import cv2
import argparse
import imutils
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False)
args = vars(ap.parse_args())

#image processing: resize image, create a circle and rectangle
image = cv2.imread(args["image"])
image = imutils.resize(image, 300, 600)
cv2.imshow("Original", image)

#initialize dummy images
rectangle = np.zeros((300,300), dtype = "uint8")
cv2.rectangle(rectangle, (25,25), (275,275), 255, -1)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150,150), 150, 255, -1)
cv2.imshow("Circle", circle)

#===================[perform bitwise]=================

#true if and only if BOTH pixels are greater than zero.
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

#true if either of the two pixels are greater than zero
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

#true if and only if either of the two pixels are greater than zero, but not both.
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

#inverts the “on” and “off” pixels
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)

#================[masking]=======================

# mask = np.zeros(image.shape[:2], dtype= "uint8")
# (cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
# cv2.rectangle(mask, (cX -60, cY - 150), (cX + 60, cY + 75), 255, -1)

# masked = cv2.bitwise_and(image, image, mask = mask)

# cv2.imshow("Masked", masked)

#=================[splitting & merging channels]=============
# (B,G,R) = cv2.split(image)

# # cv2.imshow("Red", R)
# # cv2.imshow("Green", G)
# # cv2.imshow("Blue", B)

# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imshow("HSV", hsv)

cv2.waitKey(0)
