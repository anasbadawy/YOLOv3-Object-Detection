import os
import cv2
import random
import subprocess
import sys


# constants
image_folder = 'JPEGImages'
savedir = 'labels'
obj = 'enemy'




if __name__ == '__main__':
    for n, image_file in enumerate(os.scandir(image_folder)):
        img = image_file
        image = cv2.imread(image_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	
        image = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)

        #image = imutils.resize(image,400,400)
        imh, imw = image.shape[:2]
        
        fil=open(savedir+'/'+image_file.name[:8]+'.txt', 'w')
        
        while True:
            bbox = cv2.selectROI(image, False)
        
            x=int(bbox[0])
            y=int(bbox[1])
            w=int(bbox[2])
            h=int(bbox[3])
            xav=int((w/2))
            yav=int((h/2))
            # Tracking success
            xcent =(x+xav)
            ycent =(y+yav)
        
            p1= xcent/imw
            p2= ycent/imh
            p3= w/imw
            p4= h/imh

            fil.write(str(0)+' '+str(p1)+' '+str(p2)+' '+str(p3)+' '+str(p4)+'\n')
            
            k = cv2.waitKey(0) 
            if k == 27 : continue
            break
                
        cv2.destroyAllWindows()
