import numpy as np
import cv2
#import time
from PIL import Image

# # # testjpg = Image.open('./testimg.jpg')
# # # copyjpg = Image.open('./img2.jpg')
# # # copyimg = np.array(copyjpg)
# # # testimg = np.array(testjpg)
testimg = cv2.imread('./testimg.jpg')
copyimg = cv2.imread('./img2.jpg')

def captureMLFrame(imagein, copyin):
    mlimg = cv2.resize(imagein, (224, 224))
#     copywidth, copyheight = int(copyin.shape[1] * 0.5), int(copyin.shape[0] * 0.5)
#     copydim = (copywidth, copyheight)
#     copyframe = cv2.resize(copyin, copydim)
    dim = (100, int(copyin.shape[0] * (100 / copyin.shape[1])))
    cv2.resize(copyin, dim, interpolation = cv2.INTER_AREA)
    y0, dy = 25, 20
    labstring = ("this is \nsome \ntext on \nscreen.")
    for i, line in enumerate(labstring.split('\n')):
        y = y0 + i*dy
        mlframe = cv2.putText(
        img=copyin,
        text=line,
        org=(10, y),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1,
        color=(0, 222, 222))
            #******
            #for each line in the label string, lines splitting with a newline:
            #put the text a distance down from the previous line
            #build the cv2 frame with:
            #this image
            #the text we just formatted
            #text starting at this origin
            #in this font
            #at this size
            #in this bgr color
            #******
        cv2.imshow("MLFrame", mlframe)
        cv2.waitKey(1)
        #cv2.resizeWindow("MLFrame", 640,480)
            #show the image and text
            #key2 = cv2.waitKey(1) & 0xFF
            #grab keypresses
        
        #if key2 == ord("q"):
            #return(0)
        #if x is pressed close this
        
captureMLFrame(testimg, copyimg)
#cv2.resizeWindow("MLFrame", 1600,900)
cv2.waitKey(0)