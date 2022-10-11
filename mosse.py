import numpy as np
import cv2
import os
import numpy as np
import pry




class MOSSE:
    def __init__(self, args):

        #this is where you make a list of all your video frames


        
        videopath = args.videopath
        framepath = args.framepath
        '''
        cap = cv2.VideoCapture(videopath)
        ret,frame = cap.read()
        count = 0
        while ret:

            cv2.imwrite(os.path.join(framepath , 'frame%d.png' % count), frame) # save frame as png file        
            ret,frame = cap.read()
            count += 1

        '''

        #create a list for the frames
        framelist = []


        count = 0 
        for frame in os.listdir(framepath):

            path = framepath + 'frame%d.png' % count
            framelist.append(path)
            count +=1           
        

        self.framelist = framelist

        '''

        for i in range(len(self.framelist)):

            img = cv2.imread(framelist[i])
            #cv2.imshow("framelist[%d] " % i , img)
            #cv2.waitKey(50)

            '''

        print("Data has already been initialized and read")


    def tracking(self):


        cropped = self.getROI()

        self.preprocess(cropped)
        #initialize()



    def getROI(self):
        #read first image
        #get ROI of image and crop it

        firstframe = cv2.imread(self.framelist[0])
        region = cv2.selectROI(firstframe)
        imgCrop = firstframe[int(region[1]):int(region[1]+region[3]), int(region[0]):int(region[0]+region[2])]
        gray_image = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2GRAY)

        return gray_image

    def preprocess(self, img):


        #log transform  S = c * log (1 + r)
        imglog = (np.log(img+1)/(np.log(1+np.max(img))))*255
        img_log = np.array(imglog,dtype=np.uint8)

        cv2.imshow('log_image',img_log)
        cv2.waitKey(1000)


        #Fourier Transform to get the fourier domain









        # Display cropped image
        #cv2.imshow("Image", imgCrop)
        #cv2.waitKey(1000)










    #def initialize():





        #Get first frame of video to get ROI and everything
        #crop that photo and start initializing 