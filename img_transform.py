import numpy as np
import imutils
import argparse
import cv2

#remember: 0 is height, 1 is width

ap = argparse.ArgumentParser();
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Original", image)

#================[Shifting]==================
#[1,0]: shift left or right (neg = left, pos = right)
#[0,1]: shift up or down (neg = up, pos = down)
M = np.float32([[1,0,25], [0,1,50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

M = np.float32([[1,0,-50], [0,1,-90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)


#or we can use the imultils library from Adrian
shifted = imutils.translate(image, 0, 100) # no shifting horizontal and down 100 vertically
cv2.imshow("Shifted Down", shifted)

#==============[Rotating]====================
(h,w) = image.shape[:2]
center = (w // 2, h // 2) # return a tuple of center

M = cv2.getRotationMatrix2D(center, 45, 1.0) #you can rotate at any point
#warpAffine function: apply M tranformation to the image
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated by 45 Degrees", rotated)

M = cv2.getRotationMatrix2D(center, -90, 0.5) # rotate and resize
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated by -90 Degrees", rotated)

#or we can use Adrian library
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)


#===============[Resizing]========================
#image aspect ratio
r = 150.0/image.shape[1] # defining the new width = 150 | ratio = new width / old width
dim = (150, int(image.shape[0] * r)) # new height = old height * ratio

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

#or we can use Adrian resize library
resized = imutils.resize(image, width=100)
cv2.imshow("Resized using Adrian's", resized)

#===============[Flipping]========================
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)

#==============[Cropping]========================
cropped = image[0:350, 35:image.shape[1]]
cv2.imshow("Daniel's face", cropped)

cv2.waitKey(0)
