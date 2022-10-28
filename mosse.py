import numpy as np
import cv2
import os
import numpy as np
import pry
from matplotlib import pyplot as plt
import math




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


        preimg, ROI = self.getROI()


        self.getPredicted(preimg, ROI):

        fft = self.preprocess(cropped)

        target = self.synthetic_target(cropped)

        F_conj = np.conjugate(fft) #F conjugate
        H_conj = np.multiply(target, F_conj) / np.multiply(fft, F_conj) + 0.001 #to avoid dive by 0 errors

        #initialize()



    def getROI(self):
        #read first image
        #get ROI of image and crop it

        firstframe = cv2.imread(self.framelist[0])
        gray_image = cv2.cvtColor(firstframe, cv2.COLOR_BGR2GRAY)
        frame = gray_image.astype(np.float32)
        region = cv2.selectROI(frame)
        preimg = np.array(region).astype(np.int64)

        imgCrop = frame[int(region[1]):int(region[1]+region[3]), int(region[0]):int(region[0]+region[2])]
        
        

        return preimg frame


    #preprocess step of log transformation and returns fourier domain
    def preprocess(self, img):


        #log transform  S = c * log (1 + r)
        imglog = (np.log(img+1)/(np.log(1+np.max(img))))*255
        imglog = np.array(imglog,dtype=np.uint8)

        cv2.imshow('log_image',imglog)
        cv2.waitKey(1000)


        #Fourier Transform to get the fourier domain

        f = np.fft.fft2(imglog)
        fshift = np.fft.fftshift(f)
        magnitude = 20*np.log(np.abs(fshift))    
        
        plt.subplot(122),plt.imshow(magnitude, cmap = 'gray')
        plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
        plt.show()

        return magnitude

    def synthetic_target(self, img):
        centerx = math.floor(len(img) / 2)
        centery = math.floor(len(img[0]) / 2)
        sig = 2 

        height, width = img.shape
    
        xx, yy = np.meshgrid(np.arange(len(img)), np.arange(len(img[0])))
        difx = np.square(xx - centerx)
        dify = np.square(yy - centery)
        calc = (difx + dify) / (sig ** 2)
                
    

        Gi = np.exp(-calc)
        print("Gi ", Gi)

    
        cv2.imshow('synthetic_target',img)
        cv2.imwrite("synthetic_target.png", img)
        cv2.waitKey(1000)

    def getPredicted(self, preimg, ROI):
        #preimg Getting response to find the center

        h, w = preimg.shape
        xx, yy = np.meshgrid(np.arange(w), np.arange(h))
        x_0 = ROI[0] + 0.5 * ROI[2]
        y_0 = gt[1] + 0.5 * gt[3]
        resp = np.exp(-(np.square(xx - x_0) + np.square(yy - y_0)) / (2 * self.args.sigma))

    def normalize():
        return (img - img.min()) / (img.max() - img.min())

       

















        # Display cropped image
        #cv2.imshow("Image", imgCrop)
        #cv2.waitKey(1000)










    #def initialize():





        #Get first frame of video to get ROI and everything
        #crop that photo and start initializing 