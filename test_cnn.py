import keras
import numpy as np
import sys
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

# Initialising the CNN
model = keras.models.load_model('model.h5')
labels = {'tulips': 4, 'roses': 2, 'dandelion': 1, 'sunflowers': 3, 'daisy': 0}

# TESTING CODE
image = sys.argv[1]
test_image = load_img(image, target_size = (64,64))
test_image = img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result_label = model.predict_classes(test_image)

for label,key in labels.items():
	if key==result_label[0]:
		print(label)

