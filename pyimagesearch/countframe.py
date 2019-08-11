from ..convenience import is_cv3
import cv2
def count_frames (path, override = False):
	if path is None:
		path = 0
	video = cv2.VideoCapture(path)
	total = 0

	if override:
		total = count_frames_manual(video)
	else:
		# this method is proned to bug
		try:
			#check if we're using cv3
			if is_cv3():
				total = int (video.get(cv2.CAP_PROP_FRAME_COUNT))
			else:
				total = int (video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
		except:
			total = count_frames_manual(video)
	video.release()

	return total


def count_frames_manual(video):
	total = 0
	while True:
		(grabbed, frame) = video.read()
		if not grabbed or frame is None:
			break
		total += 1
	return total

