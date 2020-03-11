import numpy as np
import cv2

canvas1 = np.zeros((300,300,3), dtype="uint8")
canvas2 = np.zeros((300, 300, 3), dtype="uint8")
canvas3 = np.zeros((300, 300, 3), dtype="uint8")

blue = (255,0,0)
green = (0,255,0)
red = (0,0,255)
white = (255, 255, 255)


(centerX, centerY) = (canvas2.shape[1] // 2 , canvas2.shape[0] // 2) #floor division


cv2.line(canvas1, (0,0), (300,300), green, 2)
cv2.line(canvas1, (0,300), (300,0), red, 2)

cv2.rectangle(canvas1, (50,200), (200,225), red, 5)
cv2.rectangle(canvas1, (200, 50), (225, 125), blue, -1)

for i in range (0, 175, 25): # 0-175 with step is 25
	cv2.circle(canvas2,(centerX,centerY), i, white, 1)

for i in range (0,25):
	radius = np.random.randint(5,high=200)
	color = np.random.randint(0,high=256, size = (3,)).tolist()
	pt = np.random.randint(0,high=300,size=(2,))

	cv2.circle(canvas3, tuple(pt), radius, color ,-1)

cv2.imshow("Canvas1", canvas1)
cv2.imshow("Canvas2", canvas2)
cv2.imshow("Canvas3", canvas3)
cv2.waitKey(0)
