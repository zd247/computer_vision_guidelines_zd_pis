from __future__ import print_function
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help ="Path to image")
args = vars(ap.parse_args())

#load the image
image = cv2.imread(args["image"])
image = imutils.resize(image, 500, 700)
print ("width: {} pixels".format(image.shape[1]))
print ("height: {} pixels".format(image.shape[0]))
print ("channels: {} pixels".format(image.shape[2]))

(b,g,r) = image[0,0]
print ("pixel at (0,0) - Red {}, Green {}, Blue {}".format(r,g,b))

cv2.imshow("Frame", image)
cv2.waitKey(0)

#write image to disk
# cv2.imwrite("newimage.jpg", image)
