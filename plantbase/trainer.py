from data import get_data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import tensorflow
import os
from PIL import Image
import glob
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras import optimizers
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Activation, Flatten, Reshape
from tensorflow.keras.callbacks import EarlyStopping


class Trainer():

    ESTIMATOR = 'CNN_basic'
    EXPERIMENT_NAME = 'PlantBaseTrainer'

    def __init__(self, train, val):
        self.train = train
        self.val = val

    def get_estimator(self):
        estimator = self.kwargs.get('estimator', self.ESTIMATOR)
        if estimator == 'CNN_basic':
            model = Sequential()
            model.add(Conv2D(30, (5,5), strides=(1,1), padding='valid', input_shape=(256,256, 3), activation='relu'))
            model.add(MaxPooling2D(3))
            model.add(Conv2D(60, (2, 2), padding='same', activation='relu'))
            model.add(MaxPooling2D(3))
            model.add(Conv2D(50, (2, 2), padding='same', activation='relu'))
            model.add(MaxPooling2D(3))
            model.add(Flatten())
            model.add(Dense(25))
            model.add(Activation('softmax'))
            model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        else:
            pass

    def set_pipeline(self):
        self.set_pipeline = Pipeline(steps=[('rgs', self.get_estimator())])

    def train(self):
        self.set_pipeline()
        es = EarlyStopping(monitor='val_loss', patience=5, mode='min')
        self.pipeline.fit(training_data = self.train,
                            validation_data = self.val,
                            callbacks=[es],
                            epochs=100,
                            batch_size=32)


if __name__ == '__main__':
    params = dict()
    train_val = get_data(**params)
    train = train_val[0]
    val = train_val[1]
    t = Trainer(train=train, val=val, **params)
    t.train()
