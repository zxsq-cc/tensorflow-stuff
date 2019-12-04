#reqs: tensorflow, opencv, opencv-contrib-python==3.4.3.18 (4.0+ buggy), ...?

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
#hide deprecation warnings from tf's use of numpy
import tensorflow as tf
import tensorflow.keras
#using tensorflow's keras implementation, *not* keras itself.
import numpy as np
import cv2
#import time
from PIL import Image
#used for jpg->array

testjpg = Image.open('/home/pi/Desktop/tffull/testimg.jpg')
testimg = np.array(testjpg)
#path to test image
testimg = testimg[..., ::-1]
testimg = np.array(testimg)
testdup = testimg

print("loading model...")
print("(this will take a minute)")
model = tensorflow.keras.models.load_model('/home/pi/Desktop/tffull/keras_model.h5')
#***absolute path to keras h5 model***

def captureMLFrame(imagein):
    mlimg = cv2.resize(imagein, (224, 224))
    #resize video frame to 224x224, since the pixels will be stored as an array in memory
    mlimg = mlimg.astype("float") / 255.0
    #shift the values to 0-255 floats
    mlimg = tf.keras.preprocessing.image.img_to_array(mlimg)
    #actually save the frame into an array
    mlimg = np.expand_dims(mlimg, axis=0)
    (fuel, redBall, whiteBall, none) = model.predict(mlimg)[0]
    #(put, your, classnames, here)
    probf = fuel
    probr = redBall
    probw = whiteBall
    probn = none
    #probability vars for each class
    labstring = (f"{probf:.3f} 'fuel'\n{probr:.3f} 'red'\n{probw:.3f} 'white'\n{probn:.3f} 'none'")
    #text string for probabilities
    y0, dy = 25, 20
    #size of text in cv2 window
    for i, line in enumerate(labstring.split('\n')):
        y = y0 + i*dy
        mlframe = cv2.putText(
        img=testdup,
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
    
    return (0)
    
    
#***"main"***
captureMLFrame(testimg)
key = cv2.waitKey(1) & 0xFF
        #grab keypresses
if key == ord("q"):
    cv2.destroyAllWindows()
        #cleanly close all windows