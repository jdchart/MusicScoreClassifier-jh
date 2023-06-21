#!/usr/bin/python
import sys, os, inspect

from argparse import ArgumentParser

import keras
import numpy
import skimage
from keras.utils import plot_model
from scipy import ndimage
from PIL import Image

import imageio

from skimage.transform import resize

def classify_images(model_path, image_paths):
    returnData = {"images" : []}

    # Load classifier
    classifier = keras.models.load_model(model_path)
    #classifier.summary()
    input_shape = classifier.input_shape[1:4]

    for img in image_paths:
        # Load image
        input_image = imageio.imread(img, mode="RGB")

        # Image preprocessing
        normalized_input_image = resize(input_image, output_shape=input_shape, preserve_range=True)
        normalized_input_image = normalized_input_image.astype(numpy.float32)


        # Classification
        scores = classifier.predict(numpy.array([normalized_input_image])).flatten()
        print(" Class scores: {0}".format(numpy.array2string(scores, formatter={'float_kind': lambda x: "%0.2f" % x})))
        class_with_highest_probability = numpy.where(scores == scores.max())[0][0]

        class_names = ['other', 'score']
        print(" Image is most likely: {0} (certainty: {1:0.2f})".format(class_names[class_with_highest_probability],
                                                                        scores[class_with_highest_probability]))
        
        returnData["images"].append({
            "path" : img,
            "scores" : [to_python_float(scores[0]), to_python_float(scores[1])],
            "highest_prob" : to_python_float(class_with_highest_probability),
            "class" : class_names[class_with_highest_probability],
            "certainty" : to_python_float(scores[class_with_highest_probability])
        })

    return returnData

def to_python_float(npInput):
    return round(npInput.item(), 4)