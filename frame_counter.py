from pyimagesearch.countframe import count_frames
import argparse
import os

ap =  argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "video path")
ap.add_argument("-o", "--override", required = True, help = "override or nah")
args = argparse.vars(ap.parse_args())

total = count_frames(args["video"], args["override"])

print("[INFO] {:,} total frames read from {}".format(total,
	args["video"][args["video"].rfind(os.path.sep) + 1:]))

