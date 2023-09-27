import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
import glob

img_glob = "*.png"
basedir = "D:/SuperPointPretrainedNetwork-master/assets/icl_snippet/"
img_glob = "*.jpg"
basedir = "D:/Datasets/Dataset-20211126-GIV/img0/data/040000/"
search = os.path.join(basedir, img_glob)
listing = glob.glob(search)
listing.sort()

win = "Fast Tracker"
cv2.namedWindow(win)

for img_path in listing:

    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Initiate FAST object with default values
    fast = cv2.FastFeatureDetector_create(threshold = 10) # great = 5

    # find and draw the keypoints
    kp = fast.detect(img, None)
    out2 = (np.dstack((img, img, img))).astype("uint8")

    for pt in kp:
        pt1 = (int(pt.pt[0]),int(pt.pt[1]))
        cv2.circle(out2, pt1, 1, (0, 255, 0), -1, lineType=16)

    cv2.imshow(win, out2)

    # img2 = cv2.drawKeypoints(img, kp, outImage=None, color=(0, 255, 0))
    # cv2.imshow(win, img2)


    key = cv2.waitKey(300) & 0xFF
    if key == ord('q'):
        print('Quitting, \'q\' pressed.')
        break

# # Print all default params
# print "Threshold: ", fast.getInt("threshold")
# print "nonmaxSuppression: ", fast.getBool("nonmaxSuppression")
# print "neighborhood: ", fast.getInt("type")
# print "Total Keypoints with nonmaxSuppression: ", len(kp)

# cv2.imwrite("fast_true.png",img2)

# # Disable nonmaxSuppression
# fast.setBool("nonmaxSuppression",0)
# kp = fast.detect(img,None)

# print "Total Keypoints without nonmaxSuppression: ", len(kp)

# img3 = cv2.drawKeypoints(img, kp, color=(255,0,0))

# cv2.imwrite("fast_false.png",img3)
