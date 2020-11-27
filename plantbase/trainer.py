from data import get_data
from utils import compute_success_ratio

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
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras import optimizers
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Activation, Flatten, Reshape
from tensorflow.keras.callbacks import EarlyStopping


class Trainer():

    ESTIMATOR = 'CNN_basic'
    EXPERIMENT_NAME = 'PlantBaseTrainer'

    def __init__(self, train, val):
        self.train_generator = train_generator
        self.val_generator = val_generator

    def get_estimator(self):
        estimator = self.kwargs.get('estimator', self.ESTIMATOR)
        if estimator == 'CNN_basic':
            model = Sequential([
                  layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
                  layers.Conv2D(16, 3, input_shape=(img_height, img_width, 3),padding='same', activation='relu'),
                  layers.MaxPooling2D(),
                  layers.Conv2D(32, 3, padding='same', activation='relu'),
                  layers.MaxPooling2D(),
                  layers.Conv2D(64, 3, padding='same', activation='relu'),
                  layers.MaxPooling2D(),
                  layers.Flatten(),
                  layers.Dense(64, activation='relu'),
                  layers.Dense(16)
                ])
            model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        elif estimator == 'vgg16':
            pass

        elif: estimator == 'vgg19'
            pass
        else:
            pass

        # add in mlflow stuff
        return model


    def set_pipeline(self):
        self.set_pipeline = Pipeline(steps=[('rgs', self.get_estimator())])

    def train(self):
        pipeline = self.set_pipeline()
        es = EarlyStopping(monitor='val_loss', patience=5, mode='min')
        pipeline.fit(train_generator = self.train_generator,
                    steps_per_epoch = self.train_generator.samples // 32,
                    validation_data = self.val_generator,
                    validation_steps = self.val_generator.samples // 32,
                    #class_weight=class_weight,
                    epochs = 10,
                    EarlyStopping = es
                    )

    def evaluate(self):
        rmse_train = self.compute_rmse(self.X_train, self.y_train)
        self.mlflow_log_metric("rmse_train", rmse_train)
        if self.split:
            rmse_val = self.compute_rmse(self.X_val, self.y_val, show=True)
            self.mlflow_log_metric("rmse_val", rmse_val)
            print(colored("rmse train: {} || rmse val: {}".format(rmse_train, rmse_val), "blue"))
        else:
            print(colored("rmse train: {}".format(rmse_train), "blue"))

if __name__ == '__main__':
    params = dict()
    train_val = get_data(**params)
    train_generator = train_val[0]
    val_generator = train_val[1]
    t = Trainer(train=train, val=val, **params)
    t.train()
