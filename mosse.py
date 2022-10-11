import numpy as np
import cv2
import os
import pry




class MOSSE:
    def __init__(self, args):

        #this is where you make a list of all your video frames
        videopath = args.videopath
        framepath = args.framepath
        cap = cv2.VideoCapture(videopath)
        ret,frame = cap.read()
        count = 0
        while ret:

            cv2.imwrite(os.path.join(framepath , 'frame%d.png' % count), frame) # save frame as png file        
            ret,frame = cap.read()
            count += 1


    #def initialize():



        #Get first frame of video to get ROI and everything


        #crop that photo and start initializing 



