import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
import tensorflow as tf
import tensorflow.keras
from PIL import Image
import numpy as np
np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model('/home/pi/Desktop/tffull/keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
image = Image.open('/home/pi/Desktop/tffull/testimg.jpg')
image.resize((224, 224))
image_array = np.asarray(image)
normalized_image_array = image_array / 255.0
data[0] = normalized_image_array
prediction = model.predict(data)
print(prediction)