import cv2
import imutils
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, 450, 600)
cv2.imshow("Baseline", image)

#defining blur kernel (kernel size increases, more blurred the picture)
blurred = np.hstack([
	cv2.blur(image, (3, 3)),
	cv2.blur(image, (5, 5)),
	cv2.blur(image, (7, 7))
])

#using GaussianBlur to get more natural blurring effect
g_blurred = np.hstack([
	cv2.GaussianBlur(image,(3,3), 0),
	cv2.GaussianBlur(image,(5,5), 0),
	cv2.GaussianBlur(image,(7,7), 0)
])

#using medianBlur to reduce image noise
m_blurred = np.hstack([
	cv2.medianBlur(image,3),
	cv2.medianBlur(image,5),
	cv2.medianBlur(image,7)
])

b_blurred = np.hstack([
	cv2.bilateralFilter(image, 5,21,21),
	cv2.bilateralFilter(image, 7,31,31),
	cv2.bilateralFilter(image, 9,41,41)
])

cv2.imshow("Averaged", blurred)
cv2.imshow("Gaussian", g_blurred)
cv2.imshow("Median", m_blurred)
cv2.imshow("Bilateral", b_blurred)
cv2.waitKey(0)


