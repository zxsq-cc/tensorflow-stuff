import numpy as np
import cv2
#import time
from PIL import Image

testjpg = Image.open('./testimg.jpg')
testimg = np.array(testjpg)
copyimg = testimg

def captureMLFrame(imagein, copyin):
    mlimg = cv2.resize(imagein, (224, 224))
    y0, dy = 25, 20
    labstring = ("this is \nsome \ntext on \nscreen.")
    for i, line in enumerate(labstring.split('\n')):
            y = y0 + i*dy
            mlframe = cv2.putText(
            img=copyin,
            text=line,
            org=(10, y),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=10,
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
            #show the image and text
            #key2 = cv2.waitKey(1) & 0xFF
            #grab keypresses
        
        #if key2 == ord("q"):
            #return(0)
        #if x is pressed close this
        
captureMLFrame(testimg, copyimg)
key = cv2.waitKey(1) & 0xFF
        #grab keypresses
if key == ord("q"):
    cv2.destroyAllWindows()