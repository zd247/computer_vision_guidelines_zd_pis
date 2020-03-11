from __future__ import print_function
import cv2
import argparse
import imutils
import numpy as np
import mahotas # new image processing package

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

#image processing: grayscaled then blurred
image = cv2.imread(args["image"])
image = imutils.resize(image, 500,500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
cv2.imshow("Image", image)
cv2.imshow("Blurred", blurred)

# ===================[simple thresholding] ===============================================
# #types of thresholdings: https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a147222a96556ebc1d948b372bcd7ac59
# (T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY) #
# cv2.imshow("Threshold Binary", thresh)

# (T, threshInv) = cv2.threshold(blurred, 155 ,255, cv2.THRESH_BINARY_INV)
# cv2.imshow("Threshold Binary Inverse", threshInv)

# (T, threshTrunc) = cv2.threshold(blurred, 155, 255, cv2.THRESH_TRUNC)
# cv2.imshow("Threshold Truncate", threshTrunc)

# (T, threshToZero) = cv2.threshold(blurred, 155, 255, cv2.THRESH_TOZERO)
# cv2.imshow("Threshold to zero", threshToZero)

# (T, threshToZeroInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_TOZERO_INV)
# cv2.imshow("Threshold to zero inverse", threshToZeroInv)

# cv2.imshow("Coins", cv2.bitwise_and(image, image, mask = threshToZero))

# =============== [adaptive thresholding: comparing neighbouring pixels-> edge detection] ==============

# thresh = cv2.adaptiveThreshold(blurred, 255,
# 								cv2.ADAPTIVE_THRESH_MEAN_C,
# 								cv2.THRESH_BINARY_INV, 11, 4)
# 								# 11: 11x11 comparison kernel, 4: fine-tuning param
# cv2.imshow("Mean Thresh", thresh)

# gaussian_thresh = cv2.adaptiveThreshold(blurred, 255,
# 								cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
# 								cv2.THRESH_BINARY_INV, 15, 3)
# cv2.imshow("Gaussian Thresh", gaussian_thresh)

cv2.waitKey(0)
