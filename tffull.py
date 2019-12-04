import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
#hide deprecation warnings from tf's use of numpy
import tensorflow as tf
import tensorflow.keras
#using tensorflow's keras implementation, *not* keras itself.
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2
import time

#np.set_printoptions(precision=3, suppress=True)
#3 decimal place precision, don't use sci notation
print("starting camera stream")
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 40
rawCapture = PiRGBArray(camera, size=(640,480))
#set up the camera
time.sleep(0.1)
#give a little time for it to warm up and create the first frame
###testimage =
print("loading model...")
print("(this will take a minute)")
model = tensorflow.keras.models.load_model('/home/pi/Desktop/tffull/keras_model.h5')
#absolute path to keras h5 model

def captureMLFrame(imagein):
    mlimg = cv2.resize(imagein, (224, 224))
    #resize video frame to 224x224, since the pixels are stored as an array in memory
    mlimg = mlimg.astype("float") / 255.0
    #shift the values to 0-255 floats
    mlimg = tf.keras.preprocessing.image.img_to_array(mlimg)
    #actually save the frame into an array
    mlimg = np.expand_dims(mlimg, axis=0)
    (fuel, redBall, whiteBall, none) = model.predict(mlimg)[0]
    #(put, your, classnames, here)
    label = "none"
    #default label
    probf = fuel
    probr = redBall
    probw = whiteBall
    probn = none
    #probability vars for each class
    
# # #     if fuel > none and fuel > redBall and fuel > whiteBall:
# # #         label = "Fuel"
# # #         proba = fuel
# # #     elif redBall > none and redBall > fuel and redBall > whiteBall:
# # #         label = "Red Ball"
# # #         proba = redBall
# # #     elif whiteBall > none and whiteBall > redBall and whiteBall > fuel:
# # #         label = "white ball"
# # #         proba = whiteBall
# # #     else:
# # #         label = "none"
# # #         proba = none
    #determine correct label to apply

    labstring = (f"{probf:.3f} 'fuel'\n{probr:.3f} 'red'\n{probw:.3f} 'white'\n{probn:.3f} 'none'")
    #text string for probabilities
    y0, dy = 25, 20
    #size of text in cv2 window
    
#     label = labstring
#     #((probf * 100) + 'fuel' + (probr * 100) + 'red' + (probw * 100) + 'white' + (probn * 100) + 'none')
#     mlframe = cv2.putText(
#         img=imagein,
#         text=label,
#         org=(10, 25),
#         fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#         fontScale=0.7,
#         color=(0, 255, 0))
#         
#         #thickness=2)
    for i, line in enumerate(labstring.split('\n')):
        y = y0 + i*dy
        mlframe = cv2.putText(
        img=imagein,
        text=line,
        org=(10, y),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.7,
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
        key2 = cv2.waitKey(1) & 0xFF
        #grab keypresses
    
    if key2 == ord("x"):
        return(0)
    #if x is pressed close this
    
    return (1)
    #shouldn't happen

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    
    cv2.imshow("picamera live view", image)
    #show camera live view
    
    key = cv2.waitKey(1) & 0xFF
    #grab keypresses
    rawCapture.truncate(0)
    if key == ord("q"):
        break
        #break out of capturing live images on q pressed
    if key == ord("c"):
        captureMLFrame(image)
        #capture image for processing on c pressed


    
cv2.destroyAllWindows()
#cleanly close all windows

# # # data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# # # image = Image.open('/home/pi/Desktop/tffull/testimg.jpg')
# # # image = image.resize((224, 224))
# # # image_array = np.asarray(image)
# # # normalized_image_array = image_array / 255.0
# # # data[0] = normalized_image_array
# # # prediction = model.predict(data)
# # # print(prediction)
# # # print("[[---fuel-------red--------white------none---]]")