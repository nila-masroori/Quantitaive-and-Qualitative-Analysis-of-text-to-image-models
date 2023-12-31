# -*- coding: utf-8 -*-
"""Face extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XK6s4oxggadu4RSA9_4hvFl6fw0ipGDB

Face extraction
"""

# install all packages
import os
from keras.models import load_model
!pip install mtcnn
# confirm mtcnn was installed correctly
import mtcnn
# print version
print(mtcnn.__version__)

import numpy as np
from mtcnn.mtcnn import MTCNN
from numpy import asarray
from PIL import Image
import matplotlib.pyplot as plt


# Simple python package to shut up Tensorflow warnings and logs.
!pip install silence_tensorflow
import silence_tensorflow.auto

# extract a single face from a given photograph
def extract_face(filename,img_name, required_size=(250, 250)):
    # load image from file
    image = Image.open(filename)
    # convert to RGB, if needed
    image = image.convert('RGB')
    # convert to array
    pixels = np.asarray(image)
    # create the detector, using default weights
    detector = MTCNN()
    # detect faces in the image
    results = detector.detect_faces(pixels)
    # extract the bounding box from the first face
    if len(results) >=1:
        x1, y1, width, height = results[0]['box']
        if height-width>=15:
            # bug fix
            x1, y1 = abs(x1), abs(y1)
            x2, y2 = x1 + width, y1 + height
            # extract the face
            face = pixels[y1:y2, x1:x2]
            # resize pixels to the model size
            image = Image.fromarray(face)
            image = image.resize(required_size)
            face_array = np.asarray(image)
            plt.imsave(os.path.join(savedirimage, img_name),face_array)
            # plt.imsave(os.path.join(savedirimage, 'face_img_{}.jpg'.format(index)),face_array)
            return True
    return False

from google.colab import drive
drive.mount('/content/drive/')



savedirimage='/content/drive/MyDrive/Project-AML/LAFITE_Flickr30k/Flickr30_LAFITE_Extracted_faces'# the path to save the extracted face images

path="/content/drive/MyDrive/Project-AML/LAFITE_Flickr30_face"

files=os.listdir(path)

len(files)

index =1013
for file in files[1013:10000]:
    if extract_face(os.path.join(path,file),file):
        print(index)
        index+=1

len(os.listdir(savedirimage))

