import glob, os
import re
import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance as dist
from tqdm import tqdm
import os 

from new import FrameCapture


FrameCapture("/home/sharan/recap_videos/recap_1/video/mp4/recap_1.mp4", "/home/sharan/recap_videos/recap_1/frames")


numbers = re.compile(r'(\d+)')

def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

frames = []

for infile in sorted(glob.glob(os.path.join( '/home/sharan/recap_videos/recap_1/frames', '*.jpg')), key = numericalSort):
    #print(infile)
    frames.append(infile)


hist_sum = []


for i in range(0, len(frames)-2):
	#print(i)
	frame_1 = cv2.imread(frames[i])
	frame_2 = cv2.imread(frames[i+1])

	frame_1_hsv = cv2.cvtColor(frame_1, cv2.COLOR_BGR2HSV)
	frame_2_hsv = cv2.cvtColor(frame_2, cv2.COLOR_BGR2HSV)

	f1_hsv = cv2.split(frame_1_hsv)
	f2_hsv = cv2.split(frame_2_hsv)

	f1_v_hist = cv2.calcHist(f1_hsv, [2], None, [256], [0, 255])
	f2_v_hist = cv2.calcHist(f2_hsv, [2], None, [256], [0, 255])

	sum_here = 0
	for i in range(0, f1_v_hist.size):
		sum_here+=abs(f1_v_hist[i] - f2_v_hist[i])

	hist_sum.append(sum_here)

index = []
for i in range(0, len(frames)-1):
	index.append(i)

hist_tbs = dict(zip(index, hist_sum))

#for keys, values in hist_tbs.items():
    #print("Keys: ", keys, "  and Values: ", values)

sorted_by_value = sorted(hist_tbs.items(), key=lambda kv: kv[1])




print(" ")
print(" ")

for i in range(0, len(frames)-2):
    if(sorted_by_value[i+1][1] - sorted_by_value[i][1] > 20000):	#20000
        frame_start = i+1
        break
    else:
        continue

frame_changes = []

for i in range(frame_start, len(frames)-2):
    frame_changes.append(sorted_by_value[i][0])

#for each in frame_changes:
    #print(each)


frame_changes.sort()

shots = []
shots.append([0, frame_changes[0]])


for i in range(1, len(frame_changes)):
    shots.append([frame_changes[i-1]+1, frame_changes[i]])

shots.append([frame_changes[i]+1, len(frames)-2])
    
print(shots)

'''
shots_final = []

for i in range(0, len(shots)):
	if(shots[i][0] != shots[i][1]):
		shots_final.append(shots[i])

for i in range(0, len(shots_final)-1):
	if(shots_final[i+1][0] - shots_final[i][1] > 1):
		shots_final[i+1][0] = shots_final[i][1] + 1
'''



print(" ")
#print("Shots: ", len(shots))
print("Shots: " , len(shots))




